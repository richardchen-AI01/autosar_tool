"""End-to-end tests for MemIf code generation against V25.10 reference."""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent.parent
CORE = ROOT / 'core'
GENERATOR = ROOT / 'generator'
SAMPLE = ROOT / 'samples' / 'Demo_S32K148'
OUT = Path('/tmp/test_memif_gen')


def _run_generator(module: str, sample: Path, out: Path) -> str:
    """Returns stdout+stderr."""
    if out.exists():
        shutil.rmtree(out)
    env = os.environ.copy()
    pp = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(CORE) + (':' + pp if pp else '')
    p = subprocess.run(
        [sys.executable, '-m', 'generator', '-g', module, '-i', str(sample), '-o', str(out)],
        capture_output=True, text=True, timeout=60, env=env, cwd=str(ROOT),
    )
    assert p.returncode == 0, f'generator failed: {p.stdout}\n{p.stderr}'
    return p.stdout + p.stderr


def _filter(text: str) -> str:
    """Drop expected timestamp/tool-version lines for diff comparison."""
    return '\n'.join(
        l for l in text.splitlines()
        if not re.search(r'@(date|toolVersion)', l)
    )


@pytest.fixture(scope='module', autouse=True)
def run_generator_once():
    """Run generator once, share output across all tests in this module."""
    _run_generator('MemIf', SAMPLE, OUT)
    yield
    # Cleanup left to OS /tmp


def test_generator_produces_three_files():
    for name in ('MemIf_Cfg.h', 'MemIf_Cfg.c', 'MemIf_Bswmd.arxml'):
        assert (OUT / name).is_file(), f'missing output: {name}'


def test_h_file_matches_reference_byte_identical():
    ours = (OUT / 'MemIf_Cfg.h').read_text()
    ref  = (SAMPLE / 'config' / 'MemIf_Cfg.h').read_text()
    assert _filter(ours) == _filter(ref), 'MemIf_Cfg.h differs from V25.10 reference'


def test_c_file_matches_reference_byte_identical():
    ours = (OUT / 'MemIf_Cfg.c').read_text()
    ref  = (SAMPLE / 'config' / 'MemIf_Cfg.c').read_text()
    assert _filter(ours) == _filter(ref), 'MemIf_Cfg.c differs from V25.10 reference'


def test_h_contains_expected_macros():
    h = (OUT / 'MemIf_Cfg.h').read_text()
    for macro in ('MEMIF_DEV_ERROR_DETECT', 'MEMIF_NUMBER_OF_DEVICES',
                  'MEMIF_VERSION_INFO_API', 'MEMIF_MODULE_VERSION'):
        assert f'#define {macro}' in h, f'macro {macro} missing'


def test_docs_15_patch_module_version_value():
    """docs §15 end-to-end patch: MemIfModuleVersion flowed to generated code."""
    h = (OUT / 'MemIf_Cfg.h').read_text()
    assert '#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"' in h, \
        'docs §15 MemIfModuleVersion patch did not reach generated header'


def test_output_is_crlf_to_match_v25_10():
    """V25.10 outputs CRLF (Windows). We must too for byte-identical comparison."""
    raw = (OUT / 'MemIf_Cfg.h').read_bytes()
    assert b'\r\n' in raw[:200], 'expected CRLF line endings to match V25.10'
