# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintMapping.py
from .AtpBlueprintMapping import AtpBlueprintMapping

class BlueprintMapping(AtpBlueprintMapping):

    def __init__(self):
        super().__init__()
        from .AtpBlueprint import AtpBlueprint
        from .AtpBlueprintable import AtpBlueprintable
        self._artop_blueprintRef = None
        self._artop_derivedObjectRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_blueprintRef':"ATP-BLUEPRINT", 
         '_artop_derivedObjectRef':"ATP-BLUEPRINTABLE"})

    @property
    def ref_blueprint_(self):
        return self._artop_blueprintRef

    @property
    def blueprint_(self):
        if self._artop_blueprintRef is not None:
            if hasattr(self._artop_blueprintRef, "uuid"):
                return self._artop_blueprintRef.uuid
        return

    @property
    def ref_derivedObject_(self):
        return self._artop_derivedObjectRef

    @property
    def derivedObject_(self):
        if self._artop_derivedObjectRef is not None:
            if hasattr(self._artop_derivedObjectRef, "uuid"):
                return self._artop_derivedObjectRef.uuid
        return
