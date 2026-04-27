# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimingDescription.py
from .Identifiable import Identifiable

class TimingDescription(Identifiable):

    def __init__(self):
        super().__init__()
        from .TimingExtension import TimingExtension
        from .VariationPoint import VariationPoint
        self._artop_timingExtension = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_timingExtension':"TIMING-EXTENSION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_timingExtension_(self):
        return self._artop_timingExtension

    @property
    def timingExtension_(self):
        if self._artop_timingExtension is not None:
            if hasattr(self._artop_timingExtension, "uuid"):
                return self._artop_timingExtension.uuid
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
