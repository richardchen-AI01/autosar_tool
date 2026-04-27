# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucModuleConfigurationValuesRefConditional.py
from .ARObject import ARObject

class EcucModuleConfigurationValuesRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .EcucValueCollection import EcucValueCollection
        from .EcucModuleConfigurationValues import EcucModuleConfigurationValues
        from .VariationPoint import VariationPoint
        self._artop_ecucValueCollection = None
        self._artop_ecucModuleConfigurationValuesRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucValueCollection':"ECUC-VALUE-COLLECTION", 
         '_artop_ecucModuleConfigurationValuesRef':"ECUC-MODULE-CONFIGURATION-VALUES", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_ecucValueCollection_(self):
        return self._artop_ecucValueCollection

    @property
    def ecucValueCollection_(self):
        if self._artop_ecucValueCollection is not None:
            if hasattr(self._artop_ecucValueCollection, "uuid"):
                return self._artop_ecucValueCollection.uuid
        return

    @property
    def ref_ecucModuleConfigurationValues_(self):
        return self._artop_ecucModuleConfigurationValuesRef

    @property
    def ecucModuleConfigurationValues_(self):
        if self._artop_ecucModuleConfigurationValuesRef is not None:
            if hasattr(self._artop_ecucModuleConfigurationValuesRef, "uuid"):
                return self._artop_ecucModuleConfigurationValuesRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
