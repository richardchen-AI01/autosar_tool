#!/usr/bin/env python3
"""reference_diff.py — compare our generator output vs V25.10 reference output.

Used as the canonical M2.1 / M2.2 / M3.1 检查脚本.

Workflow:
  1. Run our `python -m generator -g <Module> -i samples/Demo_S32K148 -o /tmp/our_out`
  2. Locate V25.10 reference output (usually under
     reference/autosar-cfg/.../config/ — the user must produce these once
     by running V25.10's actual ORIENTAISBswGen.exe; OR there's a known
     `reference/v25_10_demo_s32k148/<Module>_Cfg.{c,h}` snapshot dir).
  3. Diff each pair of files (filtered: drop /* Generated ... */ lines etc.)
  4. Print summary and exit 0 if all pass, 1 if any diff.

Usage:
    tools/reference_diff.py --modules MemIf,Det,NvM,Ea,Fee
    tools/reference_diff.py --modules MemIf --strict        # don't filter timestamps
    tools/reference_diff.py --module MemIf --our /tmp/out --ref reference/v25_10/...

Exit codes:
    0 — all module outputs identical (after filtering)
    1 — at least one module differs
    2 — usage / setup error
"""
from __future__ import annotations
import argparse
import difflib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / 'samples'
REFERENCE_ROOT = ROOT / 'reference' / 'autosar-cfg'

# Lines that should be filtered before diff (timestamps, generator version,
# anything that legitimately differs but doesn't change semantics).
FILTER_PATTERNS = [
    re.compile(r'/\*.*Generated.*by.*\*/', re.IGNORECASE),
    re.compile(r'/\*.*?\d{4}[/-]\d{2}[/-]\d{2}.*?\*/'),
    re.compile(r'\* Generation Date.*'),
    re.compile(r'\* Tool Version.*'),
    re.compile(r'\* iSOFT.*'),
]

# How V25.10 reference outputs are organised on disk.
# Pattern: reference/.../<demo>/config/<Module>_{Cfg,Lcfg}.{c,h}
def find_reference_files(module: str, sample: str = 'Demo_S32K148') -> List[Path]:
    """Search for V25.10-generated <Module>_{Cfg,Lcfg}.{c,h} under reference/."""
    candidates = []
    if not REFERENCE_ROOT.exists():
        return candidates
    # _Cfg = pre-compile / _Lcfg = link-time post-compile config (NvM 等多产物模块)
    for suffix in ('Cfg', 'Lcfg'):
        for ext in ('h', 'c'):
            for p in REFERENCE_ROOT.rglob(f'{module}_{suffix}.{ext}'):
                if 'config' in p.parts and sample.lower() in str(p).lower():
                    candidates.append(p)
    # sort: Cfg.h, Cfg.c, Lcfg.h, Lcfg.c — 稳定显示顺序
    candidates.sort(key=lambda p: ('Lcfg' in p.stem, p.suffix != '.h', str(p)))
    return candidates


def filter_lines(text: str, strict: bool) -> str:
    """Drop noise lines (timestamps etc.) unless strict mode is on."""
    if strict:
        return text
    out = []
    for line in text.splitlines():
        if any(p.search(line) for p in FILTER_PATTERNS):
            continue
        out.append(line)
    return '\n'.join(out) + ('\n' if text.endswith('\n') else '')


def diff_files(ours: Path, ref: Path, strict: bool) -> Tuple[bool, str]:
    """Compare two text files; returns (identical?, diff text)."""
    if not ours.exists():
        return False, f'OUR file missing: {ours}'
    if not ref.exists():
        return False, f'REF file missing: {ref}'
    a = filter_lines(ours.read_text(errors='replace'), strict)
    b = filter_lines(ref.read_text(errors='replace'), strict)
    if a == b:
        return True, ''
    diff = '\n'.join(difflib.unified_diff(
        b.splitlines(), a.splitlines(),
        fromfile=str(ref), tofile=str(ours), lineterm='', n=3,
    ))
    return False, diff


def run_generator(module: str, sample_dir: Path, out_dir: Path) -> Tuple[bool, str]:
    """Invoke our `python -m generator -g <module> -i <sample_dir> -o <out_dir>`.
    Returns (success?, captured stdout/stderr)."""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    extras = f'{ROOT/"core"}:{ROOT/"generator"}'
    env['PYTHONPATH'] = f'{extras}:{pp}' if pp else extras
    cmd = [sys.executable, '-m', 'generator',
           '-g', module, '-i', str(sample_dir), '-o', str(out_dir)]
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=120)
    return p.returncode == 0, (p.stdout + p.stderr)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--modules', default='MemIf',
                    help='comma-separated module list (default: MemIf)')
    ap.add_argument('--sample', default='Demo_S32K148',
                    help='sample workspace name under samples/')
    ap.add_argument('--strict', action='store_true',
                    help="don't filter timestamps/generator-version lines")
    ap.add_argument('--no-run', action='store_true',
                    help='skip running generator; use existing --our dir')
    ap.add_argument('--our', default=None,
                    help='our generator output dir (default: /tmp/v01_<module>)')
    ap.add_argument('--verbose', '-v', action='store_true')
    args = ap.parse_args()

    modules = [m.strip() for m in args.modules.split(',') if m.strip()]
    sample_dir = SAMPLES / args.sample
    if not sample_dir.exists():
        print(f'ERROR: sample workspace not found: {sample_dir}', file=sys.stderr)
        return 2

    overall_pass = True
    summary: List[Tuple[str, str, bool, str]] = []  # (module, file, ok, note)

    for module in modules:
        out_dir = Path(args.our) if args.our else Path(f'/tmp/v01_{module}')
        if not args.no_run:
            ok, log = run_generator(module, sample_dir, out_dir)
            if not ok:
                overall_pass = False
                summary.append((module, '<generator>', False, 'generator failed'))
                if args.verbose:
                    print(f'\n--- generator log for {module} ---\n{log}')
                continue
            elif args.verbose:
                print(f'\n--- generator log for {module} ---\n{log}')

        ref_files = find_reference_files(module, args.sample)
        if not ref_files:
            summary.append((module, '<reference>', False,
                            f'no V25.10 reference found under {REFERENCE_ROOT}'))
            overall_pass = False
            continue

        for ref in ref_files:
            ours = out_dir / ref.name
            ok, diff = diff_files(ours, ref, args.strict)
            summary.append((module, ref.name, ok, diff if not ok else ''))
            if not ok:
                overall_pass = False

    # ----- print summary -----
    print()
    print('='*70)
    print(f'  reference_diff: {len(modules)} module(s), strict={args.strict}')
    print('='*70)
    last_mod = None
    for mod, fname, ok, note in summary:
        if mod != last_mod:
            print(f'\n  {mod}')
            last_mod = mod
        mark = '\033[32mOK\033[0m  ' if ok else '\033[31mFAIL\033[0m'
        print(f'    [{mark}] {fname}')
        if not ok and note:
            for line in note.splitlines()[:20]:
                print(f'        {line}')
            if len(note.splitlines()) > 20:
                print(f'        ...({len(note.splitlines())-20} more lines)')

    print()
    if overall_pass:
        print('  RESULT: \033[32mALL PASS\033[0m')
        return 0
    else:
        print('  RESULT: \033[31mFAIL\033[0m')
        return 1


if __name__ == '__main__':
    sys.exit(main())
