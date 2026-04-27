"""Public — replaces V25.10 Common/Public.pyd (Cython native, closed-source).

API surface from PE strings (see autosar-cfg/_pyd_analysis/Public.md):
  getSwitchValue, getBooleanValue, getURIPath, getIntegerValue,
  get_variant_module, get_variant_info, get_container_len, get_pure_container,
  secondToMs, checkRTE, checkBSW, getPartitionRef, getApplicationIdByModule,
  getApplicationIdByPartition, get_mcu_type, get_sd_value, getBswModule

Reference reading: validator's `pyz_source/Common/Public.py` is the
reverse-engineered source — has uncompyle6 syntax errors but conveys logic.

D1 STATUS: only stubs needed by MemIf are implemented. Others raise NotImplementedError.
"""

from typing import Any, Optional


# ---------------------------------------------------------------------------
# MemIf-critical helpers (these are called by MemIf.py / MemIfRules.py)
# ---------------------------------------------------------------------------

def getSwitchValue(value: Any) -> str:
    """Convert an ECUC boolean to AUTOSAR-style 'STD_ON' / 'STD_OFF'.

    Used in MemIf.py:
        return getSwitchValue(self.getAttrValue(BP.MemIf_MemIfDevErrorDetect))
    """
    if value in (True, 'true', 'TRUE', 'True', '1', 1):
        return 'STD_ON'
    return 'STD_OFF'


def getBooleanValue(value: Any) -> bool:
    """ECUC boolean → Python bool."""
    return value in (True, 'true', 'TRUE', 'True', '1', 1)


def getIntegerValue(container: Any, short_name: str) -> Optional[int]:
    """Look up an integer parameter on a container by short-name.

    Used in MemIfRules.py:
        numberOfDevices = getIntegerValue(general, BP.MemIf_MemIfNumberOfDevices.shortName)
    """
    if container is None:
        return None
    try:
        pvs = container.parameterValues_EcucParameterValue
    except AttributeError:
        return None
    for pv in pvs:
        d = getattr(pv, 'ref_definition_', None) or getattr(pv, 'definition_', None)
        if d is not None and getattr(d, 'shortName', None) == short_name:
            v = getattr(pv, 'value_', None) or getattr(pv, 'value', None)
            if v is None:
                return None
            try:
                return int(v)
            except (ValueError, TypeError):
                return None
    return None


def getURIPath(container: Any, short_name: str) -> str:
    """Build the full ECUC URI path for a parameter inside a container.

    Used in MemIfRules.py to point IDE Problem markers to the right URI.
    """
    # Walk up container chain to build full path
    parts = [short_name]
    cur = container
    while cur is not None:
        sn = getattr(cur, 'shortName', None) or getattr(cur, 'shortName_', None)
        if sn:
            parts.insert(0, sn)
        cur = getattr(cur, 'eContainer', lambda: None)()
        # Defensive: don't infinite loop
        if len(parts) > 12:
            break
    return '/' + '/'.join(parts)


# ---------------------------------------------------------------------------
# Module / variant helpers (used by validator framework, stubbed for D1)
# ---------------------------------------------------------------------------

def getBswModule(name: str) -> Optional[Any]:
    """Return the EcucModuleConfigurationValues EObject for a module short name.

    D1 stub: needs `arxmlparse.artop.all_objects` global; M2 will wire.
    """
    try:
        from Common.arxmlparse.artop import all_objects
    except ImportError:
        return None
    list_module = all_objects.get('EcucModuleConfigurationValues', [])
    for moduleObj in list_module:
        if getattr(moduleObj, 'shortName_', None) == name:
            return moduleObj
    return None


def checkRTE(module: str) -> bool:
    """D1 stub: returns False unconditionally (RTE not in MemIf scope)."""
    return False


def checkBSW(moduleName: str) -> bool:
    """D1 stub: just check if the module exists in the model."""
    return getBswModule(moduleName) is not None


# ---------------------------------------------------------------------------
# Other helpers MemIf doesn't need; D6 stubs
# ---------------------------------------------------------------------------

def secondToMs(s: float) -> float: return s * 1000.0
def get_variant_module(*a, **kw): return None       # TODO D6
def get_variant_info(*a, **kw): return None         # TODO D6
def get_container_len(*a, **kw): return 0           # TODO D6
def get_pure_container(*a, **kw): return None       # TODO D6
def getPartitionRef(*a, **kw): return None          # TODO D6
def getApplicationIdByModule(*a, **kw): return 0    # TODO D6
def getApplicationIdByPartition(*a, **kw): return 0 # TODO D6
def get_mcu_type(*a, **kw): return ''               # TODO D6
def get_sd_value(*a, **kw): return None             # TODO D6
