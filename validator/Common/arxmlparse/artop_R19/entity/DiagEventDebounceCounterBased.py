# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagEventDebounceCounterBased.py
from .DiagEventDebounceAlgorithm import DiagEventDebounceAlgorithm

class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):

    def __init__(self):
        super().__init__()
        from .IntegerValueVariationPoint import IntegerValueVariationPoint
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        self._artop_counterBasedFdcThresholdStorageValue = None
        self._artop_counterDecrementStepSize = None
        self._artop_counterFailedThreshold = None
        self._artop_counterIncrementStepSize = None
        self._artop_counterJumpDown = None
        self._artop_counterJumpDownValue = None
        self._artop_counterJumpUp = None
        self._artop_counterJumpUpValue = None
        self._artop_counterPassedThreshold = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_counterDecrementStepSize': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_counterFailedThreshold': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_counterIncrementStepSize': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_counterJumpDown': '"BOOLEAN-VALUE-VARIATION-POINT"', 
         '_artop_counterJumpDownValue': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_counterJumpUp': '"BOOLEAN-VALUE-VARIATION-POINT"', 
         '_artop_counterJumpUpValue': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_counterPassedThreshold': '"INTEGER-VALUE-VARIATION-POINT"'})

    @property
    def counterBasedFdcThresholdStorageValue_(self):
        if self._artop_counterBasedFdcThresholdStorageValue:
            return int(self._artop_counterBasedFdcThresholdStorageValue)
        return self._artop_counterBasedFdcThresholdStorageValue

    @property
    def ref_counterDecrementStepSize_(self):
        return self._artop_counterDecrementStepSize

    @property
    def counterDecrementStepSize_(self):
        if self._artop_counterDecrementStepSize is not None:
            if hasattr(self._artop_counterDecrementStepSize, "uuid"):
                return self._artop_counterDecrementStepSize.uuid
        return

    @property
    def ref_counterFailedThreshold_(self):
        return self._artop_counterFailedThreshold

    @property
    def counterFailedThreshold_(self):
        if self._artop_counterFailedThreshold is not None:
            if hasattr(self._artop_counterFailedThreshold, "uuid"):
                return self._artop_counterFailedThreshold.uuid
        return

    @property
    def ref_counterIncrementStepSize_(self):
        return self._artop_counterIncrementStepSize

    @property
    def counterIncrementStepSize_(self):
        if self._artop_counterIncrementStepSize is not None:
            if hasattr(self._artop_counterIncrementStepSize, "uuid"):
                return self._artop_counterIncrementStepSize.uuid
        return

    @property
    def ref_counterJumpDown_(self):
        return self._artop_counterJumpDown

    @property
    def counterJumpDown_(self):
        if self._artop_counterJumpDown is not None:
            if hasattr(self._artop_counterJumpDown, "uuid"):
                return self._artop_counterJumpDown.uuid
        return

    @property
    def ref_counterJumpDownValue_(self):
        return self._artop_counterJumpDownValue

    @property
    def counterJumpDownValue_(self):
        if self._artop_counterJumpDownValue is not None:
            if hasattr(self._artop_counterJumpDownValue, "uuid"):
                return self._artop_counterJumpDownValue.uuid
        return

    @property
    def ref_counterJumpUp_(self):
        return self._artop_counterJumpUp

    @property
    def counterJumpUp_(self):
        if self._artop_counterJumpUp is not None:
            if hasattr(self._artop_counterJumpUp, "uuid"):
                return self._artop_counterJumpUp.uuid
        return

    @property
    def ref_counterJumpUpValue_(self):
        return self._artop_counterJumpUpValue

    @property
    def counterJumpUpValue_(self):
        if self._artop_counterJumpUpValue is not None:
            if hasattr(self._artop_counterJumpUpValue, "uuid"):
                return self._artop_counterJumpUpValue.uuid
        return

    @property
    def ref_counterPassedThreshold_(self):
        return self._artop_counterPassedThreshold

    @property
    def counterPassedThreshold_(self):
        if self._artop_counterPassedThreshold is not None:
            if hasattr(self._artop_counterPassedThreshold, "uuid"):
                return self._artop_counterPassedThreshold.uuid
        return
