"""Smoke tests for core/Common/* — verify all helpers can be imported and have the
public API surface that V25.10 reverse-engineering documented."""
import sys
from pathlib import Path

# Add core/ to path so `from Common.X import ...` works without env tweaks
_CORE = Path(__file__).resolve().parent.parent
if str(_CORE) not in sys.path:
    sys.path.insert(0, str(_CORE))

import pytest


def test_all_13_native_helpers_importable():
    """Every Common.* module that V25.10 had as a .pyd must have a Python equivalent here."""
    import importlib
    for mod_name in [
        'BswBase', 'Public', 'CodeGenerator', 'Context', 'J2Filters',
        'ArgParser', 'ConfigParser', 'Constant', 'IncGen',
        'logger', 'main', 'PerformanceMonitor', 'Utils',
    ]:
        mod = importlib.import_module(f'Common.{mod_name}')
        assert mod is not None, f'Common.{mod_name} not importable'


def test_BswBase_has_5_public_methods():
    from Common.BswBase import BswBase
    for name in ['getAttrValue', 'getSubContainer', 'getIndex',
                 'getWholeIndex', 'getParentContainer']:
        assert hasattr(BswBase, name), f'BswBase missing {name}'


def test_BswBase_can_construct_and_use_with_None_container():
    from Common.BswBase import BswBase
    b = BswBase(None)
    assert b.getAttrValue('anything') is None
    assert b.getSubContainer('anything') == []
    assert b.getParentContainer() is None


def test_Public_getSwitchValue_canonical_outputs():
    from Common.Public import getSwitchValue, getBooleanValue
    assert getSwitchValue('true') == 'STD_ON'
    assert getSwitchValue('false') == 'STD_OFF'
    assert getSwitchValue(True) == 'STD_ON'
    assert getSwitchValue(False) == 'STD_OFF'
    assert getSwitchValue(None) == 'STD_OFF'
    assert getBooleanValue('true') is True
    assert getBooleanValue('false') is False


def test_BswPath_enum_full_count():
    from Common.arxmlparse.constant.BswPathConstant import BswPath
    members = [a for a in dir(BswPath) if not a.startswith('_') and not a.startswith('shortName')]
    # V25.10 has 6870 entries (verified by extraction)
    assert len(members) > 6000, f'BswPath has only {len(members)} members; expected > 6000'


def test_BswPath_member_has_value_and_shortName():
    from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
    m = BP.MemIf_MemIfGeneral
    assert m.value == '/AUTOSAR/MemIf/MemIfGeneral'
    assert m.shortName == 'MemIfGeneral'


def test_J2Filters_register_filters_runs():
    from jinja2 import Environment
    from Common.J2Filters import register_filters
    env = Environment()
    register_filters(env)
    for name in ['formatDescription', 'listStrip', 'getDict', 'bitAnd', 'asList']:
        assert name in env.filters
