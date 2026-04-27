# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TracedFailure.py
from .Identifiable import Identifiable

class TracedFailure(Identifiable):

    def __init__(self):
        super().__init__()
        from .ErrorTracerNeeds import ErrorTracerNeeds
        from .VariationPoint import VariationPoint
        self._artop_id = None
        self._artop_errorTracerNeeds = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_errorTracerNeeds':"ERROR-TRACER-NEEDS", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def id_(self):
        return self._artop_id

    @property
    def ref_errorTracerNeeds_(self):
        return self._artop_errorTracerNeeds

    @property
    def errorTracerNeeds_(self):
        if self._artop_errorTracerNeeds is not None:
            if hasattr(self._artop_errorTracerNeeds, "uuid"):
                return self._artop_errorTracerNeeds.uuid
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
