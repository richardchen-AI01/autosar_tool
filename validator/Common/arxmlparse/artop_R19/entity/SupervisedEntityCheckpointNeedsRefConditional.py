# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SupervisedEntityCheckpointNeedsRefConditional.py
from .ARObject import ARObject

class SupervisedEntityCheckpointNeedsRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .SupervisedEntityNeeds import SupervisedEntityNeeds
        from .SupervisedEntityCheckpointNeeds import SupervisedEntityCheckpointNeeds
        from .VariationPoint import VariationPoint
        self._artop_supervisedEntityNeeds = None
        self._artop_supervisedEntityCheckpointNeedsRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_supervisedEntityNeeds':"SUPERVISED-ENTITY-NEEDS", 
         '_artop_supervisedEntityCheckpointNeedsRef':"SUPERVISED-ENTITY-CHECKPOINT-NEEDS", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_supervisedEntityNeeds_(self):
        return self._artop_supervisedEntityNeeds

    @property
    def supervisedEntityNeeds_(self):
        if self._artop_supervisedEntityNeeds is not None:
            if hasattr(self._artop_supervisedEntityNeeds, "uuid"):
                return self._artop_supervisedEntityNeeds.uuid
        return

    @property
    def ref_supervisedEntityCheckpointNeeds_(self):
        return self._artop_supervisedEntityCheckpointNeedsRef

    @property
    def supervisedEntityCheckpointNeeds_(self):
        if self._artop_supervisedEntityCheckpointNeedsRef is not None:
            if hasattr(self._artop_supervisedEntityCheckpointNeedsRef, "uuid"):
                return self._artop_supervisedEntityCheckpointNeedsRef.uuid
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
