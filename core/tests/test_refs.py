"""Unit tests for ref-target resolution: _RefTarget, _RefList, artop.by_path.

These cover the contract added in D2 afternoon to unlock NvM end-to-end:

  - _RefTarget(str) is string-comparable but exposes V25.10 wrapper API
  - _RefList(list) acts as iterable-of-_RefTarget AND single-ref proxy
  - artop.by_path resolves instance paths to loaded EObjects
  - BswBase.shortName_ delegates to wrapped container
  - top-level container.parent_ points to its module (eContainer semantics)
"""
from __future__ import annotations

from pathlib import Path

import pytest

from Common.BswBase import BswBase, _RefList, _RefTarget
from Common.arxmlparse import artop
from Common.arxmlparse.loader import load_project


SAMPLE = Path(__file__).resolve().parent.parent.parent / 'samples' / 'Demo_S32K148'


@pytest.fixture(scope='module', autouse=True)
def _load_demo():
    artop.def_elements.clear()
    artop.all_objects.clear()
    artop.by_path.clear()
    load_project(SAMPLE)


# ----------------------------------------------------------------- _RefTarget

def test_reftarget_is_string_comparable():
    rt = _RefTarget('/S32K148/Fee/FeeBlockConfiguration_0')
    assert rt == '/S32K148/Fee/FeeBlockConfiguration_0'
    assert hash(rt) == hash('/S32K148/Fee/FeeBlockConfiguration_0')
    assert isinstance(rt, str)


def test_reftarget_shortname_returns_leaf():
    rt = _RefTarget('/S32K148/Fee/FeeBlockConfiguration_0')
    assert rt.shortName_ == 'FeeBlockConfiguration_0'
    assert rt.shortName == 'FeeBlockConfiguration_0'


def test_reftarget_ref_type_exposes_dest():
    rt = _RefTarget('/foo/bar', dest='ECUC-CONTAINER-VALUE')
    assert rt.ref_type_.shortName_ == 'ECUC-CONTAINER-VALUE'
    assert rt.ref_type_.shortName == 'ECUC-CONTAINER-VALUE'


def test_reftarget_resolves_to_loaded_container():
    """A real path from the demo workspace resolves; getParentContainer
    walks to the module."""
    paths = [p for p in artop.by_path if p.startswith('/S32K148/Fee/FeeBlockConfiguration_')]
    assert paths, 'demo should have FeeBlockConfiguration_* containers'
    rt = _RefTarget(paths[0])
    parent = rt.getParentContainer()
    assert parent is not None, 'top-level container.parent_ should point to module'
    assert getattr(parent, 'shortName_', None) in {'Fee', 'Fee_62'}


def test_reftarget_unresolvable_path_returns_none_gracefully():
    rt = _RefTarget('/totally/made/up/path')
    assert rt.getAttrValue('anything') is None
    assert rt.getSubContainer('anything') == []
    assert rt.getParentContainer() is None


# ----------------------------------------------------------------- _RefList

def test_reflist_iterates_as_list_of_reftargets():
    items = [_RefTarget(f'/S32K148/Fee/Block_{i}') for i in range(3)]
    rl = _RefList(items)
    assert len(rl) == 3
    for x in rl:
        assert isinstance(x, _RefTarget)


def test_reflist_first_proxy_for_singleton_callsites():
    rl = _RefList([_RefTarget('/S32K148/Foo/Bar')])
    assert rl.shortName_ == 'Bar'  # mirrors BswImplementation.shortName_


def test_reflist_empty_short_circuits_safely():
    rl = _RefList()
    assert not rl
    assert rl.shortName_ == ''
    assert rl.getAttrValue('x') is None
    assert rl.getSubContainer('x') == []
    assert rl.getParentContainer() is None


# ------------------------------------------------------------ BswBase delegate

def test_bswbase_shortname_delegates_to_container():
    """BswBase wrappers (NvMBlockDescriptor etc.) need .shortName_ to fall
    through to the wrapped container."""
    paths = [p for p in artop.by_path if '/Fee/FeeBlockConfiguration_' in p]
    container = artop.by_path[paths[0]]
    wrapper = BswBase(container)
    assert wrapper.shortName_ == container.shortName_
    assert wrapper.shortName == container.shortName


def test_bswbase_shortname_when_no_container():
    """Empty wrapper exposes safe empty-string defaults."""
    wrapper = BswBase()
    assert wrapper.shortName_ == ''
    assert wrapper.shortName == ''


# -------------------------------------------------------------- artop.by_path

def test_by_path_indexes_modules_and_containers():
    """Loaded demo populated by_path with both module and container entries."""
    # at least a Fee module (or Fee_62) entry
    module_paths = [p for p in artop.by_path if p.count('/') == 2]
    assert module_paths, 'expected /<package>/<module> entries'
    # at least one container under a module
    container_paths = [p for p in artop.by_path if p.count('/') >= 3]
    assert container_paths, 'expected /<package>/<module>/<container>... entries'
