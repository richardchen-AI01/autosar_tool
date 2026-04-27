# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdServerEventGroupTimingConfigRefConditional.py
from .ARObject import ARObject

class SomeipSdServerEventGroupTimingConfigRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .EventHandler import EventHandler
        from .SomeipSdServerEventGroupTimingConfig import SomeipSdServerEventGroupTimingConfig
        from .VariationPoint import VariationPoint
        self._artop_eventHandler = None
        self._artop_someipSdServerEventGroupTimingConfigRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_eventHandler':"EVENT-HANDLER", 
         '_artop_someipSdServerEventGroupTimingConfigRef':"SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_eventHandler_(self):
        return self._artop_eventHandler

    @property
    def eventHandler_(self):
        if self._artop_eventHandler is not None:
            if hasattr(self._artop_eventHandler, "uuid"):
                return self._artop_eventHandler.uuid
        return

    @property
    def ref_someipSdServerEventGroupTimingConfig_(self):
        return self._artop_someipSdServerEventGroupTimingConfigRef

    @property
    def someipSdServerEventGroupTimingConfig_(self):
        if self._artop_someipSdServerEventGroupTimingConfigRef is not None:
            if hasattr(self._artop_someipSdServerEventGroupTimingConfigRef, "uuid"):
                return self._artop_someipSdServerEventGroupTimingConfigRef.uuid
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
