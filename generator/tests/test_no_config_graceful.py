"""Generator should exit cleanly (rc=0) when a module has no ECUC config in
the workspace, not crash with an UndefinedError from template rendering.

Demo_S32K148 has no Ea.arxml — perfect fixture.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CORE = ROOT / 'core'
SAMPLE = ROOT / 'samples' / 'Demo_S32K148'


def _run(module: str, out: Path):
    if out.exists():
        shutil.rmtree(out)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    return subprocess.run(
        [sys.executable, '-m', 'generator', '-g', module,
         '-i', str(SAMPLE), '-o', str(out)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )


def test_ea_unconfigured_workspace_exits_cleanly():
    out = Path('/tmp/test_ea_unconfigured')
    p = _run('Ea', out)
    assert p.returncode == 0, f'Ea on Ea-less workspace should exit 0, got {p.returncode}\n{p.stdout}\n{p.stderr}'
    assert 'No ECUC configuration for Ea' in p.stdout, \
        f'expected "No ECUC configuration" message, got:\n{p.stdout}'
    # Output dir should exist but be empty (or absent — both fine).
    if out.exists():
        assert not any(out.iterdir()), f'expected empty output dir, found: {list(out.iterdir())}'
