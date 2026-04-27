"""arxmlparse.artop — global model holder.

V25.10 reverse-engineering shows this module exposes:
  - all_objects: dict[str, list]                  e.g. all_objects['EcucModuleConfigurationValues']
  - def_elements: dict[str, list]                  keyed by ECUC full path
  - EcucContainerValue, VariationPoint              type aliases / classes

D1: empty dicts so imports work; loader at M2 will populate.
"""
from typing import Any, Dict, List

#: All EObjects in the loaded model, keyed by AUTOSAR meta-class short name.
all_objects: Dict[str, List[Any]] = {}

#: ECUC ParamDef → list of EObjects matching that path.
def_elements: Dict[str, List[Any]] = {}

#: ECUC instance path → the (single) EObject living at that workspace path.
#: Populated by loader.load_project. Used to resolve ECUC-REFERENCE-VALUE
#: VALUE-REF targets (which are instance paths like /S32K148/Fee/FeeBlockX).
by_path: Dict[str, Any] = {}


# Type stubs (replaced by ARTOP / Sphinx EMF classes at M2)
class EcucContainerValue:  # noqa: N801 — match V25.10 naming
    pass


class VariationPoint:  # noqa: N801
    pass
