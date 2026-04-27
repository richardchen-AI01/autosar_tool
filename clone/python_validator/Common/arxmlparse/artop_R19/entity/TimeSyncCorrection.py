# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeSyncCorrection.py
from .ARObject import ARObject

class TimeSyncCorrection(ARObject):

    def __init__(self):
        super().__init__()
        from .SynchronizedMasterTimeBase import SynchronizedMasterTimeBase
        self._artop_allowMasterRateCorrection = None
        self._artop_offsetCorrectionAdaptionInterval = None
        self._artop_offsetCorrectionJumpThreshold = None
        self._artop_rateCorrectionsPerMeasurementDuration = None
        self._artop_rateDeviationMeasurementDuration = None
        self._artop_synchronizedMasterTimeBase = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_synchronizedMasterTimeBase": "SYNCHRONIZED-MASTER-TIME-BASE"})

    @property
    def allowMasterRateCorrection_(self):
        if self._artop_allowMasterRateCorrection:
            if self._artop_allowMasterRateCorrection == "true":
                return True
            return False
        else:
            return self._artop_allowMasterRateCorrection

    @property
    def offsetCorrectionAdaptionInterval_(self):
        return self._artop_offsetCorrectionAdaptionInterval

    @property
    def offsetCorrectionJumpThreshold_(self):
        return self._artop_offsetCorrectionJumpThreshold

    @property
    def rateCorrectionsPerMeasurementDuration_(self):
        return self._artop_rateCorrectionsPerMeasurementDuration

    @property
    def rateDeviationMeasurementDuration_(self):
        return self._artop_rateDeviationMeasurementDuration

    @property
    def ref_synchronizedMasterTimeBase_(self):
        return self._artop_synchronizedMasterTimeBase

    @property
    def synchronizedMasterTimeBase_(self):
        if self._artop_synchronizedMasterTimeBase is not None:
            if hasattr(self._artop_synchronizedMasterTimeBase, "uuid"):
                return self._artop_synchronizedMasterTimeBase.uuid
        return
