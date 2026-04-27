# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucDefinitionCollection.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class EcucDefinitionCollection(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .EcucModuleDef import EcucModuleDef
        self._artop_moduleRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_moduleRef": "ECUC-MODULE-DEF"})

    @property
    def ref_modules_(self):
        return self._artop_moduleRef

    @property
    def modules_(self):
        return self._artop_moduleRef
