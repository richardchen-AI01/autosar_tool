# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticIndicator.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticIndicator(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .DiagnosticIndicatorTypeEnumValueVariationPoint import DiagnosticIndicatorTypeEnumValueVariationPoint
        self._artop_healingCycleCounterThreshold = None
        self._artop_type = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_healingCycleCounterThreshold':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_type':"DIAGNOSTIC-INDICATOR-TYPE-ENUM-VALUE-VARIATION-POINT"})

    @property
    def ref_healingCycleCounterThreshold_(self):
        return self._artop_healingCycleCounterThreshold

    @property
    def healingCycleCounterThreshold_(self):
        if self._artop_healingCycleCounterThreshold is not None:
            if hasattr(self._artop_healingCycleCounterThreshold, "uuid"):
                return self._artop_healingCycleCounterThreshold.uuid
        return

    @property
    def ref_type_(self):
        return self._artop_type

    @property
    def type_(self):
        if self._artop_type is not None:
            if hasattr(self._artop_type, "uuid"):
                return self._artop_type.uuid
        return
