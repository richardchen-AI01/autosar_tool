"""Tests for MemIf.derivedNumberOfDevices.

Counterpart of iSoft's MemIfGeneralEaMapSupport / FeeMapSupportEnable
function-extensions — counts NvM-referenced backends to inform the future
IDE form auto-fill.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

from Common.arxmlparse import artop
from Common.arxmlparse.loader import load_project


REPO = Path(__file__).resolve().parent.parent.parent
SAMPLE = REPO / 'samples' / 'Demo_S32K148'

# generator/modules is not on the default PYTHONPATH; the test_memif_full.sh
# wrapper adds it, but tests should be self-sufficient.
sys.path.insert(0, str(REPO / 'generator' / 'modules'))


@pytest.fixture(scope='module', autouse=True)
def _load_demo():
    artop.def_elements.clear()
    artop.all_objects.clear()
    artop.by_path.clear()
    load_project(SAMPLE)


def test_derived_is_int_in_range():
    from MemIf.src.MemIf import MemIf
    n = MemIf().derivedNumberOfDevices
    assert isinstance(n, int)
    assert 0 <= n <= 2


def test_derived_equals_sum_of_checks():
    from MemIf.src.MemIf import MemIf
    m = MemIf()
    assert m.derivedNumberOfDevices == int(m.checkFee) + int(m.checkEa)


def test_demo_s32k148_has_fee_only():
    """Demo_S32K148 references Fee but not Ea — derived should be 1."""
    from MemIf.src.MemIf import MemIf
    m = MemIf()
    assert m.checkFee is True
    assert m.checkEa is False
    assert m.derivedNumberOfDevices == 1
