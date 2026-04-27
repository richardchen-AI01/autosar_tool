"""End-to-end tests for MemIf cross-module validation rules."""
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent.parent
CORE = ROOT / 'core'
SAMPLES = ROOT / 'samples'


def _run_validator(module: str, sample: Path) -> tuple[int, str]:
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    p = subprocess.run(
        [sys.executable, '-m', 'validator', '-m', module, '-i', str(sample)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )
    return p.returncode, p.stdout + p.stderr


def test_baseline_demo_is_clean():
    code, log = _run_validator('MemIf', SAMPLES / 'Demo_S32K148')
    assert 'critical: 0 error: 0 warning: 0' in log, \
        f'baseline expected clean but got log:\n{log}'
    assert code == 0


def test_BAD_2170_fires_TCPP_2170():
    bad = SAMPLES / 'Demo_S32K148_BAD_2170'
    if not bad.exists():
        pytest.skip(f'{bad} missing — set up via tools/test_memif_full.sh first')
    code, log = _run_validator('MemIf', bad)
    assert 'TCPP_2170' in log, \
        f'expected Rule_BSW_MemIf_TCPP_2170 to fire but log:\n{log}'
    assert code != 0, 'validator should exit non-zero on rule violation'


def test_BAD_2171_fires_TCPP_2171():
    bad = SAMPLES / 'Demo_S32K148_BAD_2171'
    if not bad.exists():
        pytest.skip(f'{bad} missing — set up via tools/test_memif_full.sh first')
    code, log = _run_validator('MemIf', bad)
    assert 'TCPP_2171' in log, \
        f'expected Rule_BSW_MemIf_TCPP_2171 to fire but log:\n{log}'
    assert code != 0
