"""arxmlparse.loader — minimal ECUC ARXML loader.

Reads `<workspace>/BSW_Builder/<MCU>/<Module>.arxml` files and populates
the global `def_elements` dict in `Common.arxmlparse.artop` so that
`getBswContainerByEnum(BP.X)` returns matching containers.

V25.10 uses ARTOP / Sphinx EMF for full model loading. We only need
ECUC parameter values to produce identical .c/.h output, so we parse
the bare minimum:

  ECUC-MODULE-CONFIGURATION-VALUES
    └─ ECUC-CONTAINER-VALUE
         ├─ DEFINITION-REF (full ECUC path)
         ├─ SHORT-NAME
         ├─ PARAMETER-VALUES
         │    ├─ ECUC-NUMERICAL-PARAM-VALUE  (booleans/integers/floats)
         │    │    ├─ DEFINITION-REF
         │    │    └─ VALUE
         │    └─ ECUC-TEXTUAL-PARAM-VALUE   (strings/enums/refs)
         │         ├─ DEFINITION-REF
         │         └─ VALUE
         └─ SUB-CONTAINERS (recursive)

Each parsed element becomes a SimpleNamespace-style object with:
  shortName, definition_, parameterValues_EcucParameterValue, subContainers_EcucContainerValue
matching the attribute names BswBase.getAttrValue() expects.
"""
from __future__ import annotations
from pathlib import Path
from typing import Any, List, Optional
import xml.etree.ElementTree as ET

from Common.arxmlparse import artop

NS = '{http://autosar.org/schema/r4.0}'


# -------------------------------------------------------------- model objects

class _DefRef:
    """Stand-in for an ECUC param/container definition reference object.
    What V25.10 EMF gives:  obj.shortName == 'MemIfGeneral'  obj.shortName_ same.
    """
    __slots__ = ('shortName', 'shortName_', 'fullPath', 'dest')

    def __init__(self, full_path: str, dest: str = '') -> None:
        self.fullPath = full_path
        self.dest = dest
        leaf = full_path.rsplit('/', 1)[-1] if '/' in full_path else full_path
        self.shortName = leaf
        self.shortName_ = leaf

    def __repr__(self) -> str:
        return f'<DefRef {self.fullPath!r}>'


class _ParameterValue:
    """ECUC-NUMERICAL-PARAM-VALUE / ECUC-TEXTUAL-PARAM-VALUE / ECUC-REFERENCE-VALUE.

    For numerical/textual: `value` is a string (the parameter value).
    For reference: `value` is the target path string (from VALUE-REF).
    `is_reference` flags reference-type params so getAttrValue can return list
    semantics for them (matching V25.10 behavior).
    """
    __slots__ = ('definition_', 'ref_definition_', 'value', 'value_', 'is_reference')

    def __init__(self, def_path: str, dest: str, value: str, is_reference: bool = False) -> None:
        d = _DefRef(def_path, dest)
        self.definition_ = d
        self.ref_definition_ = d
        self.value = value
        self.value_ = value
        self.is_reference = is_reference


class _Container:
    """ECUC-CONTAINER-VALUE."""
    __slots__ = ('shortName', 'shortName_', 'definition_', 'ref_definition_',
                 'parameterValues_EcucParameterValue',
                 'subContainers_EcucContainerValue', 'parent_')

    def __init__(self, short_name: str, def_path: str, dest: str) -> None:
        self.shortName = short_name
        self.shortName_ = short_name
        d = _DefRef(def_path, dest)
        self.definition_ = d
        self.ref_definition_ = d
        self.parameterValues_EcucParameterValue: List[_ParameterValue] = []
        self.subContainers_EcucContainerValue: List['_Container'] = []
        self.parent_: Optional['_Container'] = None

    def eContainer(self) -> Optional['_Container']:
        return self.parent_

    def getSubContainer(self, name: str) -> List['_Container']:
        """Return list of sub-containers whose definition shortName matches `name`.

        V25.10 MemIf.py uses this:
            NvMBlockDescriptor.getSubContainer('NvMTargetBlockReference')
        """
        return [c for c in self.subContainers_EcucContainerValue
                if c.definition_.shortName == name or c.shortName == name]

    def getAttrValue(self, key: Any) -> Optional[str]:
        """Look up a parameter value on this container.
        Mirrors BswBase.getAttrValue contract — accepts BP enum, path, or short name."""
        from Common.BswBase import BswBase
        # Reuse BswBase logic by temporarily wrapping
        return BswBase(self).getAttrValue(key)

    def __repr__(self) -> str:
        return f'<Container {self.definition_.fullPath!r}>'


class _Module:
    """ECUC-MODULE-CONFIGURATION-VALUES."""
    __slots__ = ('shortName', 'shortName_', 'definition_', 'containers')

    def __init__(self, short_name: str, def_path: str) -> None:
        self.shortName = short_name
        self.shortName_ = short_name
        self.definition_ = _DefRef(def_path, 'ECUC-MODULE-DEF')
        self.containers: List[_Container] = []


# -------------------------------------------------------------- parsing

def _parse_container(elem: ET.Element, parent: Optional[_Container] = None) -> _Container:
    """Recursively parse one ECUC-CONTAINER-VALUE element."""
    short_name = elem.findtext(f'{NS}SHORT-NAME', default='').strip()
    def_ref_elem = elem.find(f'{NS}DEFINITION-REF')
    def_path = (def_ref_elem.text or '').strip() if def_ref_elem is not None else ''
    dest = def_ref_elem.get('DEST', '') if def_ref_elem is not None else ''

    cont = _Container(short_name, def_path, dest)
    cont.parent_ = parent

    pvs_elem = elem.find(f'{NS}PARAMETER-VALUES')
    if pvs_elem is not None:
        for pv_elem in pvs_elem:
            tag = pv_elem.tag.split('}', 1)[-1]
            if tag in ('ECUC-NUMERICAL-PARAM-VALUE', 'ECUC-TEXTUAL-PARAM-VALUE'):
                pv_def = pv_elem.find(f'{NS}DEFINITION-REF')
                pv_def_path = (pv_def.text or '').strip() if pv_def is not None else ''
                pv_dest = pv_def.get('DEST', '') if pv_def is not None else ''
                value_elem = pv_elem.find(f'{NS}VALUE')
                value = (value_elem.text or '').strip() if value_elem is not None else ''
                cont.parameterValues_EcucParameterValue.append(
                    _ParameterValue(pv_def_path, pv_dest, value, is_reference=False)
                )

    # ECUC-REFERENCE-VALUE: e.g. NvMNameOfFeeBlock → /S32K148/Fee/FeeBlockConfig_X
    refs_elem = elem.find(f'{NS}REFERENCE-VALUES')
    if refs_elem is not None:
        for ref_elem in refs_elem.findall(f'{NS}ECUC-REFERENCE-VALUE'):
            rdef = ref_elem.find(f'{NS}DEFINITION-REF')
            rdef_path = (rdef.text or '').strip() if rdef is not None else ''
            rdest = rdef.get('DEST', '') if rdef is not None else ''
            vref = ref_elem.find(f'{NS}VALUE-REF')
            vref_target = (vref.text or '').strip() if vref is not None else ''
            cont.parameterValues_EcucParameterValue.append(
                _ParameterValue(rdef_path, rdest, vref_target, is_reference=True)
            )

    sub_elem = elem.find(f'{NS}SUB-CONTAINERS')
    if sub_elem is not None:
        for sub in sub_elem.findall(f'{NS}ECUC-CONTAINER-VALUE'):
            cont.subContainers_EcucContainerValue.append(_parse_container(sub, cont))

    return cont


def _parse_module(elem: ET.Element) -> _Module:
    """Parse one ECUC-MODULE-CONFIGURATION-VALUES element."""
    short_name = elem.findtext(f'{NS}SHORT-NAME', default='').strip()
    def_ref_elem = elem.find(f'{NS}DEFINITION-REF')
    def_path = (def_ref_elem.text or '').strip() if def_ref_elem is not None else ''
    mod = _Module(short_name, def_path)
    cont_elem = elem.find(f'{NS}CONTAINERS')
    if cont_elem is not None:
        for c in cont_elem.findall(f'{NS}ECUC-CONTAINER-VALUE'):
            mod.containers.append(_parse_container(c, parent=None))
    return mod


# -------------------------------------------------------------- public API

def load_project(project_path: str | Path) -> List[_Module]:
    """Walk every .arxml under <project_path>/BSW_Builder/<MCU>/, parse each,
    and **register every container** under its DEFINITION-REF path in
    `Common.arxmlparse.artop.def_elements`.

    Returns list of parsed _Module objects (rarely needed by callers).
    """
    project_path = Path(project_path)
    bsw_root = project_path / 'BSW_Builder'
    if not bsw_root.exists():
        # Some projects use bswmds/ or top-level .arxml
        bsw_root = project_path

    modules: List[_Module] = []
    for arxml_path in bsw_root.rglob('*.arxml'):
        try:
            tree = ET.parse(str(arxml_path))
        except ET.ParseError as e:
            print(f'[WARN] {arxml_path}: parse error {e}')
            continue
        for mod_elem in tree.iter(f'{NS}ECUC-MODULE-CONFIGURATION-VALUES'):
            mod = _parse_module(mod_elem)
            modules.append(mod)
            # register each container at its DEFINITION-REF path
            for c in mod.containers:
                _register_container_recursive(c)
            # also register at module level
            artop.def_elements.setdefault(mod.definition_.fullPath, []).append(mod)
            # populate all_objects too (validator uses this)
            artop.all_objects.setdefault('EcucModuleConfigurationValues', []).append(mod)
    return modules


def _register_container_recursive(c: _Container) -> None:
    artop.def_elements.setdefault(c.definition_.fullPath, []).append(c)
    artop.all_objects.setdefault('EcucContainerValue', []).append(c)
    for sub in c.subContainers_EcucContainerValue:
        _register_container_recursive(sub)
