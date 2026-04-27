"""Det generation smoke + Det_Bswmd.arxml byte-equal vs V25.10 reference.

Det is the second BSW module brought online (after MemIf). Its templates use
the cross-module `EcucPartition` global, so this test guards against
regressions where the EcucPartition default disappears from CodeGenerator.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent.parent
CORE = ROOT / 'core'
SAMPLE = ROOT / 'samples' / 'Demo_S32K148'
OUT = Path('/tmp/test_det_gen')

EXPECTED_FILES = (
    'Det_Cfg.h', 'Det_Cfg.c',
    'Det_Externals.h', 'Det_Externals.c',
    'Det_Bswmd.arxml',
)


def _filter(text: str) -> str:
    return '\n'.join(
        l for l in text.splitlines() if not re.search(r'@(date|toolVersion)', l)
    )


@pytest.fixture(scope='module', autouse=True)
def run_generator_once():
    if OUT.exists():
        shutil.rmtree(OUT)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    p = subprocess.run(
        [sys.executable, '-m', 'generator', '-g', 'Det',
         '-i', str(SAMPLE), '-o', str(OUT)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )
    assert p.returncode == 0, f'Det generator failed:\n{p.stdout}\n{p.stderr}'
    yield


def test_det_emits_all_five_files():
    for name in EXPECTED_FILES:
        assert (OUT / name).is_file(), f'missing Det output: {name}'


def test_det_bswmd_byte_equal_to_reference():
    ours = (OUT / 'Det_Bswmd.arxml').read_text()
    ref  = (SAMPLE / 'bswmds' / 'Det_Bswmd.arxml').read_text()
    assert _filter(ours) == _filter(ref), 'Det_Bswmd.arxml differs from V25.10 reference'


def test_det_bswmd_uses_default_empty_partition():
    """Default EcucPartition='' produces 'VAR_CLEARED__UNSPECIFIED' (double _).

    This is the V25.10 behaviour when no EcucPartition is configured. Guards
    against regressions where the global is renamed or removed.
    """
    bswmd = (OUT / 'Det_Bswmd.arxml').read_text()
    assert 'VAR_CLEARED__UNSPECIFIED' in bswmd
