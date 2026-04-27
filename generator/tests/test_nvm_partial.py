"""NvM partial-progress smoke tests.

NvM is not yet end-to-end byte-equal to V25.10 — it needs a ref-target
resolution layer (single-cardinality ECUC-REFERENCE-VALUE → resolved target
container, not just the path string). Tracking ticket: docs/sprint_logs/D2.md
known-issues table → "NvM" row.

These tests pin the ground we *have* gained so we don't lose it:
  1. NvM domain class constructs without error against Demo_S32K148
  2. checkRTE / checkiRTE properties resolve (not raise)
  3. NvM_Cfg.h template renders successfully (uses BswBase.shortName_
     delegation introduced together with this test)

Run alongside test_memif_generation.py and test_det_generation.py.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent.parent
CORE = ROOT / 'core'
SAMPLE = ROOT / 'samples' / 'Demo_S32K148'


def _env() -> dict:
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    extra = f'{CORE}:{ROOT / "generator/modules"}'
    env['PYTHONPATH'] = extra + (':' + pp if pp else '')
    return env


def test_nvm_constructs():
    """`NvM()` builds against Demo_S32K148 ECUC config without raising."""
    code = (
        "from Common.arxmlparse.loader import load_project\n"
        "from pathlib import Path\n"
        f"load_project(Path('{SAMPLE}'))\n"
        "from NvM.src.NvM import NvM\n"
        "n = NvM()\n"
        "assert n.NvMCommon is not None\n"
        "assert n.NvMBlockDescriptor and len(n.NvMBlockDescriptor) > 0\n"
        "print('OK', len(n.NvMBlockDescriptor))\n"
    )
    p = subprocess.run([sys.executable, '-c', code],
                       capture_output=True, text=True, timeout=30,
                       env=_env(), cwd=str(ROOT))
    assert p.returncode == 0, f'NvM construct failed:\n{p.stdout}\n{p.stderr}'
    assert p.stdout.startswith('OK '), p.stdout


def test_nvm_checkrte_irte_resolve():
    """V25.10's _RefList wrapper lets ``BswImplementation.shortName_`` work,
    which makes `checkiRTE` walk to completion instead of AttributeError-ing.
    """
    code = (
        "from Common.arxmlparse.loader import load_project\n"
        "from pathlib import Path\n"
        f"load_project(Path('{SAMPLE}'))\n"
        "from NvM.src.NvM import NvM\n"
        "n = NvM()\n"
        "_ = n.checkRTE\n"
        "_ = n.checkiRTE\n"
        "print('OK')\n"
    )
    p = subprocess.run([sys.executable, '-c', code],
                       capture_output=True, text=True, timeout=30,
                       env=_env(), cwd=str(ROOT))
    assert p.returncode == 0, f'check[i]RTE raised:\n{p.stdout}\n{p.stderr}'


def test_nvm_cfg_h_renders():
    """First file in NvM's FilesList — must render successfully (not crash)."""
    out = Path('/tmp/test_nvm_partial')
    if out.exists():
        shutil.rmtree(out)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    p = subprocess.run(
        [sys.executable, '-m', 'generator', '-g', 'NvM',
         '-i', str(SAMPLE), '-o', str(out)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )
    # Generator may exit non-zero overall (later templates need ref-target
    # resolution we haven't built yet) — but the first file should land.
    assert (out / 'NvM_Cfg.h').is_file(), \
        f'NvM_Cfg.h was not produced.\nstdout:\n{p.stdout}\nstderr:\n{p.stderr}'
    h = (out / 'NvM_Cfg.h').read_text()
    # spot-check: derived block-descriptor #defines came through (means
    # BswBase.shortName_ delegation worked)
    assert '#define NvMConf_NvMBlockDescriptor_' in h, \
        f'expected NvMConf_NvMBlockDescriptor_ macros in NvM_Cfg.h:\n{h[:600]}'


@pytest.mark.xfail(reason='NvM ref-target resolution not implemented yet '
                          '(needs single-cardinality Ref → target container '
                          'lookup). Tracked in docs/sprint_logs/D2.md.')
def test_nvm_lcfg_c_renders_TODO():
    """NvM_Lcfg.c needs `temp.getParentContainer().shortName_` style access on
    a Ref-resolved target container. Pinned as xfail until we land that.
    """
    out = Path('/tmp/test_nvm_partial_lcfg')
    if out.exists():
        shutil.rmtree(out)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    subprocess.run(
        [sys.executable, '-m', 'generator', '-g', 'NvM',
         '-i', str(SAMPLE), '-o', str(out)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )
    assert (out / 'NvM_Lcfg.c').is_file()
