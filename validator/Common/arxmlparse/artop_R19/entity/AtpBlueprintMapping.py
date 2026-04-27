# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AtpBlueprintMapping.py
from .ARObject import ARObject

class AtpBlueprintMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .BlueprintMappingSet import BlueprintMappingSet
        self._artop_blueprintMappingSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_blueprintMappingSet": "BLUEPRINT-MAPPING-SET"})

    @property
    def ref_blueprintMappingSet_(self):
        return self._artop_blueprintMappingSet

    @property
    def blueprintMappingSet_(self):
        if self._artop_blueprintMappingSet is not None:
            if hasattr(self._artop_blueprintMappingSet, "uuid"):
                return self._artop_blueprintMappingSet.uuid
        return
