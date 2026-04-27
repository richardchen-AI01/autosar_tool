"""J2Filters — replaces V25.10 Common/J2Filters.pyd.

API surface (see autosar-cfg/_pyd_analysis/J2Filters.md):
  formatDescription, listStrip, getDict, appendItemToDict,
  bitAnd, length, asList, filter, extend

These are Jinja2 custom filters that templates can use, e.g.:
  {{ description | formatDescription(80) }}

D1 STATUS: minimal Jinja2-compatible implementations.
"""
from __future__ import annotations
from typing import Any, Dict, Iterable, List


def formatDescription(text: str, line_length: int = 80) -> str:
    """Wrap a description string into doxygen-style multi-line comment.
    D1: just return as-is (M2 will wrap properly)."""
    return text or ''


def listStrip(seq: Iterable[Any]) -> List[Any]:
    """Strip whitespace from each element in a list of strings."""
    return [str(x).strip() if isinstance(x, str) else x for x in seq]


def getDict(d: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """Dict.get equivalent for Jinja2."""
    return d.get(key, default) if isinstance(d, dict) else default


def appendItemToDict(d: Dict[Any, list], key: Any, item: Any) -> Dict[Any, list]:
    """Append item to dict[key] list, creating list if absent."""
    d.setdefault(key, []).append(item)
    return d


def bitAnd(a: int, b: int) -> int:
    """Jinja2-friendly bitwise AND."""
    return int(a) & int(b)


def asList(x: Any) -> List[Any]:
    """Wrap scalar into single-element list; passthrough lists/tuples."""
    if isinstance(x, (list, tuple)):
        return list(x)
    if x is None:
        return []
    return [x]


def length(x: Any) -> int:
    """Length, defaulting to 0 for None / non-sized."""
    try:
        return len(x)
    except TypeError:
        return 0


# ---------------------------------------------------------------------------
# Registration helper called by CodeGenerator.generateCode
# ---------------------------------------------------------------------------

def register_filters(env) -> None:
    """Register all our filters into a Jinja2 Environment."""
    env.filters['formatDescription'] = formatDescription
    env.filters['listStrip'] = listStrip
    env.filters['getDict'] = getDict
    env.filters['appendItemToDict'] = appendItemToDict
    env.filters['bitAnd'] = bitAnd
    env.filters['asList'] = asList
    env.filters['length'] = length
