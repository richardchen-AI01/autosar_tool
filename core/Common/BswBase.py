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


class BswBase:
    """Base class for every BSW module's domain model class.

    `Container` constructor argument is the ECUC container EObject
    (autosar40.ecucdescription.EcucContainerValue). For walking skeleton
    we accept any object and store as `self.container`.
    """

    def __init__(self, Container: Any = None) -> None:
        self.container = Container

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
        for pv in pvs:
            d = getattr(pv, 'ref_definition_', None) or getattr(pv, 'definition_', None)
            if d is not None and getattr(d, 'shortName', None) == short_name:
                matches.append(getattr(pv, 'value_', None) or getattr(pv, 'value', None))
                if getattr(pv, 'is_reference', False):
                    any_is_reference = True

        if any_is_reference:
            return matches  # could be []; iteration-friendly
        if len(matches) > 1:
            return matches
        if matches:
            return matches[0]
        # No matches: heuristic — if the key looks like a reference-type param
        # (shortName ends in 'Ref' / 'Refs'), return [] rather than None so
        # callers `for x in result:` works without None-checks. Mirrors V25.10
        # closed-source behavior (Cython BswBase.pyd is schema-aware).
        if short_name.endswith(('Ref', 'Refs')):
            return []
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
