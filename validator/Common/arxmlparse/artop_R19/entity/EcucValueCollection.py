# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucValueCollection.py
from .ARElement import ARElement

class EcucValueCollection(ARElement):

    def __init__(self):
        super().__init__()
        from .System import System
        from .EcucModuleConfigurationValuesRefConditional import EcucModuleConfigurationValuesRefConditional
        self._artop_ecuExtractRef = None
        self._artop_ecucValue = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecuExtractRef':"SYSTEM", 
         '_artop_ecucValue':"ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"})

    @property
    def ref_ecuExtract_(self):
        return self._artop_ecuExtractRef

    @property
    def ecuExtract_(self):
        if self._artop_ecuExtractRef is not None:
            if hasattr(self._artop_ecuExtractRef, "uuid"):
                return self._artop_ecuExtractRef.uuid
        return

    @property
    def ecucValues_EcucModuleConfigurationValuesRefConditional(self):
        return self._artop_ecucValue
