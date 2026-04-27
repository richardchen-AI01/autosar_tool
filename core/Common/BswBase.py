"""BswBase — replaces V25.10 Common/BswBase.pyd (Cython native, closed-source).

API surface from PE strings (see autosar-cfg/_pyd_analysis/BswBase.md):
  Container, getAttrValue, getSubContainer, getIndex, getWholeIndex, getParentContainer

Behavior contract reverse-engineered from MemIfRules.py callsites
(see docs §2.4.1):
  - getAttrValue(BP_member): BP_member is an enum.Enum with .value (full
    AUTOSAR path) and .shortName (leaf). Internally does container lookup.

D1 STATUS: walking-skeleton stub. M2 will fill the real EMF model walk.
"""

from typing import Any, List, Optional


class _RefTarget(str):
    """A resolved (or path-only) ECUC reference target.

    Subclass of ``str`` so existing callers that compare/print/format paths
    keep working. Adds V25.10 BswBase wrapper API on top:

      - ``.shortName_`` / ``.shortName``: leaf of the path
      - ``.ref_type_.shortName_``: DEST element type (e.g. ``ECUC-CONTAINER-VALUE``)
      - ``.getAttrValue(BP)`` / ``.getSubContainer(name)`` / ``.getParentContainer()``:
        proxy to the resolved target container looked up in
        ``Common.arxmlparse.artop.by_path``.

    Resolution is lazy + cached so we don't pay the dict lookup unless a
    method actually wants the target object. If by_path doesn't know the path
    (e.g. workspace doesn't include the referenced module), proxy methods
    return None / [] gracefully instead of raising — V25.10 closed-source
    BswBase has the same forgiving shape.
    """
    __slots__ = ('_dest', '_resolved_cache', '_resolved_done')

    def __new__(cls, path: str, dest: str = ''):
        obj = super().__new__(cls, path)
        obj._dest = dest
        obj._resolved_cache = None
        obj._resolved_done = False
        return obj

    def _resolve(self) -> Any:
        if not self._resolved_done:
            from Common.arxmlparse import artop
            self._resolved_cache = artop.by_path.get(str(self))
            self._resolved_done = True
        return self._resolved_cache

    @property
    def shortName_(self) -> str:
        s = str(self)
        return s.rsplit('/', 1)[-1] if '/' in s else s

    @property
    def shortName(self) -> str:
        return self.shortName_

    @property
    def ref_type_(self) -> Any:
        d = self._dest
        return type('_RefDest', (), {'shortName_': d, 'shortName': d})()

    def getAttrValue(self, key: Any) -> Any:
        target = self._resolve()
        return target.getAttrValue(key) if target is not None else None

    def getSubContainer(self, name: str) -> List[Any]:
        target = self._resolve()
        if target is None:
            return []
        return target.getSubContainer(name)

    def getParentContainer(self) -> Optional[Any]:
        target = self._resolve()
        if target is None:
            return None
        # Containers expose eContainer() / parent_; modules don't have a parent.
        if hasattr(target, 'eContainer'):
            return target.eContainer()
        return getattr(target, 'parent_', None)


class _RefList(list):
    """List of ``_RefTarget`` items with V25.10 single-ref wrapper accessors.

    V25.10's BswBase.getAttrValue returned (a) a list of wrapper objects for
    multi-cardinality refs, (b) a single wrapper object exposing
    ``.shortName_`` / ``.shortName`` / ``.ref_type_`` for single-cardinality
    refs. Two distinct return shapes was awkward; we collapse both into one
    type:

      - Acts as a regular list (iteration, indexing, ``len``, truth) of
        ``_RefTarget`` items — string-comparable AND wrapper-API-rich.
        Preserves call sites that loop ``for ref in getAttrValue(...)``.
      - Also exposes ``.shortName_`` / ``.shortName`` / ``.ref_type_`` /
        ``.getAttrValue(...)`` / ``.getParentContainer()`` proxying to the
        first element — what V25.10 callsites like
        ``BswImplementation.shortName_`` and
        ``temp.getParentContainer().shortName_`` expect for singleton refs.
        Empty list yields ``''`` / ``None`` / ``[]`` so
        ``if obj and obj.shortName_ == 'X'`` short-circuits cleanly.
    """

    @property
    def _first(self) -> Optional[_RefTarget]:
        return self[0] if self else None

    @property
    def shortName_(self) -> str:
        f = self._first
        return f.shortName_ if f is not None else ''

    @property
    def shortName(self) -> str:
        return self.shortName_

    @property
    def ref_type_(self) -> Any:
        f = self._first
        if f is not None:
            return f.ref_type_
        return type('_RefDest', (), {'shortName_': '', 'shortName': ''})()

    def getAttrValue(self, key: Any) -> Any:
        f = self._first
        return f.getAttrValue(key) if f is not None else None

    def getSubContainer(self, name: str) -> List[Any]:
        f = self._first
        return f.getSubContainer(name) if f is not None else []

    def getParentContainer(self) -> Optional[Any]:
        f = self._first
        return f.getParentContainer() if f is not None else None


class BswBase:
    """Base class for every BSW module's domain model class.

    `Container` constructor argument is the ECUC container EObject
    (autosar40.ecucdescription.EcucContainerValue). For walking skeleton
    we accept any object and store as `self.container`.
    """

    def __init__(self, Container: Any = None) -> None:
        self.container = Container

    # ------------------------------------------------------------ delegated
    # V25.10 BswBase exposed the underlying ECUC container's identity through
    # ``.shortName_`` / ``.shortName`` (mirroring EMF's eShortName). Templates
    # like NvM_Cfg.h use ``NvMBlockDescriptor[i].shortName_`` to embed the
    # block's short-name into ``#define`` macros, so subclasses that wrap a
    # container need this delegation to work uniformly.

    @property
    def shortName_(self) -> Any:
        c = self.container
        if c is None:
            return ''
        return getattr(c, 'shortName_', None) or getattr(c, 'shortName', '') or ''

    @property
    def shortName(self) -> Any:
        return self.shortName_

    # ------------------------------------------------------------ public API

    def getAttrValue(self, key: Any) -> Any:
        """Look up parameter value(s) on the container by BswPath enum key.

        Mirrors V25.10 behavior:
          - Scalar params (numerical/textual): returns single string, or None.
          - Reference params (ECUC-REFERENCE-VALUE): returns list of target
            paths (possibly empty), so callers `for x in result` works.

        Reference detection uses the loader-set `is_reference` flag on each
        parameter value object.
        """
        if self.container is None:
            return None
        try:
            pvs = self.container.parameterValues_EcucParameterValue
        except AttributeError:
            return None
        short_name = self._extract_short_name(key)
        if not short_name:
            return None

        matches: list = []
        any_is_reference = False
        ref_dest = ''
        for pv in pvs:
            d = getattr(pv, 'ref_definition_', None) or getattr(pv, 'definition_', None)
            if d is not None and getattr(d, 'shortName', None) == short_name:
                value = getattr(pv, 'value_', None) or getattr(pv, 'value', None)
                if getattr(pv, 'is_reference', False):
                    any_is_reference = True
                    ref_dest = getattr(d, 'dest', '') or ref_dest
                    matches.append(_RefTarget(value or '', ref_dest))
                else:
                    matches.append(value)

        if any_is_reference:
            return _RefList(matches)  # supports iteration AND .shortName_
        if len(matches) > 1:
            return matches
        if matches:
            return matches[0]
        # No matches: heuristic — if the key looks like a reference-type param
        # (shortName ends in 'Ref' / 'Refs'), return _RefList([]) rather than
        # None so callers `for x in result:` works without None-checks AND
        # `result.shortName_` short-circuits cleanly. Mirrors V25.10 closed-
        # source behavior (Cython BswBase.pyd is schema-aware).
        if short_name.endswith(('Ref', 'Refs')):
            return _RefList()
        return None

    def getSubContainer(self, name: str) -> List[Any]:
        """Return list of child containers matching `name` (short-name).

        D1 stub: returns [].
        """
        if self.container is None:
            return []
        try:
            subs = self.container.subContainers_EcucContainerValue
        except AttributeError:
            return []
        return [c for c in subs
                if getattr(c, 'shortName', None) == name
                or getattr(c, 'shortName_', None) == name]

    def getIndex(self) -> int:
        """Return container's index among siblings of same type. D1 stub: 0."""
        return 0

    def getWholeIndex(self) -> int:
        """Return container's absolute index. D1 stub: 0."""
        return 0

    def getParentContainer(self) -> Optional[Any]:
        """Return parent container EObject. D1 stub: None."""
        if self.container is None:
            return None
        return getattr(self.container, 'eContainer', lambda: None)()

    # ------------------------------------------------------------ internals

    @staticmethod
    def _extract_short_name(key: Any) -> Optional[str]:
        """key may be a BP enum member (preferred), a path string, or a short name.

        Resolution order:
          1) key.shortName attribute (BP enum case)
          2) key.value attribute, last path segment after '/'
          3) plain string, last path segment after '/'
          4) plain string, used as-is
        """
        sn = getattr(key, 'shortName', None)
        if sn:
            return sn
        v = getattr(key, 'value', None)
        if isinstance(v, str):
            return v.rsplit('/', 1)[-1]
        if isinstance(key, str):
            if '/' in key:
                return key.rsplit('/', 1)[-1]
            return key
        return None
