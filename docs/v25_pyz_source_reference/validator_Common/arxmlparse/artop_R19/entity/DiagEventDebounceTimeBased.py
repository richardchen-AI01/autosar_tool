# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagEventDebounceTimeBased.py
from .DiagEventDebounceAlgorithm import DiagEventDebounceAlgorithm

class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):

    def __init__(self):
        super().__init__()
        from .TimeValueValueVariationPoint import TimeValueValueVariationPoint
        self._artop_timeBasedFdcThresholdStorageValue = None
        self._artop_timeFailedThreshold = None
        self._artop_timePassedThreshold = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_timeBasedFdcThresholdStorageValue':"TIME-VALUE-VALUE-VARIATION-POINT", 
         '_artop_timeFailedThreshold':"TIME-VALUE-VALUE-VARIATION-POINT", 
         '_artop_timePassedThreshold':"TIME-VALUE-VALUE-VARIATION-POINT"})

    @property
    def ref_timeBasedFdcThresholdStorageValue_(self):
        return self._artop_timeBasedFdcThresholdStorageValue

    @property
    def timeBasedFdcThresholdStorageValue_(self):
        if self._artop_timeBasedFdcThresholdStorageValue is not None:
            if hasattr(self._artop_timeBasedFdcThresholdStorageValue, "uuid"):
                return self._artop_timeBasedFdcThresholdStorageValue.uuid
        return

    @property
    def ref_timeFailedThreshold_(self):
        return self._artop_timeFailedThreshold

    @property
    def timeFailedThreshold_(self):
        if self._artop_timeFailedThreshold is not None:
            if hasattr(self._artop_timeFailedThreshold, "uuid"):
                return self._artop_timeFailedThreshold.uuid
        return

    @property
    def ref_timePassedThreshold_(self):
        return self._artop_timePassedThreshold

    @property
    def timePassedThreshold_(self):
        if self._artop_timePassedThreshold is not None:
            if hasattr(self._artop_timePassedThreshold, "uuid"):
                return self._artop_timePassedThreshold.uuid
        return
