# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleCallPoint.py
from .Referrable import Referrable

class BswModuleCallPoint(Referrable):

    def __init__(self):
        super().__init__()
        from .BswModuleEntity import BswModuleEntity
        from .BswDistinguishedPartition import BswDistinguishedPartition
        from .VariationPoint import VariationPoint
        self._artop_bswModuleEntity = None
        self._artop_contextLimitationRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bswModuleEntity':"BSW-MODULE-ENTITY", 
         '_artop_contextLimitationRef':"BSW-DISTINGUISHED-PARTITION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_bswModuleEntity_(self):
        return self._artop_bswModuleEntity

    @property
    def bswModuleEntity_(self):
        if self._artop_bswModuleEntity is not None:
            if hasattr(self._artop_bswModuleEntity, "uuid"):
                return self._artop_bswModuleEntity.uuid
        return

    @property
    def ref_contextLimitations_(self):
        return self._artop_contextLimitationRef

    @property
    def contextLimitations_(self):
        return self._artop_contextLimitationRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
