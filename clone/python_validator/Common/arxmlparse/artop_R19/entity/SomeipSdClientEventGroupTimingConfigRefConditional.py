# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdClientEventGroupTimingConfigRefConditional.py
from .ARObject import ARObject

class SomeipSdClientEventGroupTimingConfigRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ConsumedEventGroup import ConsumedEventGroup
        from .SomeipSdClientEventGroupTimingConfig import SomeipSdClientEventGroupTimingConfig
        from .VariationPoint import VariationPoint
        self._artop_consumedEventGroup = None
        self._artop_someipSdClientEventGroupTimingConfigRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_consumedEventGroup':"CONSUMED-EVENT-GROUP", 
         '_artop_someipSdClientEventGroupTimingConfigRef':"SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_consumedEventGroup_(self):
        return self._artop_consumedEventGroup

    @property
    def consumedEventGroup_(self):
        if self._artop_consumedEventGroup is not None:
            if hasattr(self._artop_consumedEventGroup, "uuid"):
                return self._artop_consumedEventGroup.uuid
        return

    @property
    def ref_someipSdClientEventGroupTimingConfig_(self):
        return self._artop_someipSdClientEventGroupTimingConfigRef

    @property
    def someipSdClientEventGroupTimingConfig_(self):
        if self._artop_someipSdClientEventGroupTimingConfigRef is not None:
            if hasattr(self._artop_someipSdClientEventGroupTimingConfigRef, "uuid"):
                return self._artop_someipSdClientEventGroupTimingConfigRef.uuid
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
