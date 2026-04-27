"""BswModuleCache — V25.10 Common/arxmlparse/cache/BswModuleCache.py.

Originally a thin wrapper that calls ARTOP's `def_elements` dict to look
up containers by full ECUC path.

Used in MemIf.py:
    tempMemIfGeneral = getBswContainerByEnum(BP.MemIf_MemIfGeneral)
    self.MemIfGeneral = MemIfGeneral(tempMemIfGeneral[0]) if tempMemIfGeneral else None

D1 STATUS: stub returning [] (MemIf will skip MemIfGeneral creation; harmless
for walking-skeleton). M2 will wire to a real ARTOP loader holding all
EObjects keyed by full path.
"""
from typing import Any, List


def getBswContainerByEnum(bp_member: Any) -> List[Any]:
    """Return list of EObjects matching `bp_member`'s ECUC path.

    `bp_member` is expected to be a BP enum member (BswPath.X).
    Falls back to the raw path string in `.value`, then `.value_path`.
    """
    try:
        from Common.arxmlparse.artop import def_elements
    except ImportError:
        return []
    # Try multiple ways to get the path string out of bp_member
    path = (getattr(bp_member, 'value_path', None) or
            (getattr(bp_member, 'value', None) if isinstance(getattr(bp_member, 'value', None), str)
             else getattr(getattr(bp_member, 'value', None), 'value', None)))
    if path is None:
        return []
    return def_elements.get(path, [])
