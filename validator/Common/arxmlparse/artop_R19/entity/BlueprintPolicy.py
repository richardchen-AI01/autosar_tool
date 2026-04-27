# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintPolicy.py
from .ARObject import ARObject

class BlueprintPolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .AtpBlueprint import AtpBlueprint
        self._artop_attributeName = None
        self._artop_atpBlueprint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_atpBlueprint": "ATP-BLUEPRINT"})

    @property
    def attributeName_(self):
        return self._artop_attributeName

    @property
    def ref_atpBlueprint_(self):
        return self._artop_atpBlueprint

    @property
    def atpBlueprint_(self):
        if self._artop_atpBlueprint is not None:
            if hasattr(self._artop_atpBlueprint, "uuid"):
                return self._artop_atpBlueprint.uuid
        return
