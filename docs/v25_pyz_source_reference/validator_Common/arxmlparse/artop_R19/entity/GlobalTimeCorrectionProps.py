# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeCorrectionProps.py
from .ARObject import ARObject

class GlobalTimeCorrectionProps(ARObject):

    def __init__(self):
        super().__init__()
        from .GlobalTimeDomain import GlobalTimeDomain
        self._artop_offsetCorrectionAdaptionInterval = None
        self._artop_offsetCorrectionJumpThreshold = None
        self._artop_rateCorrectionMeasurementDuration = None
        self._artop_rateCorrectionsPerMeasurementDuration = None
        self._artop_globalTimeDomain = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_globalTimeDomain": "GLOBAL-TIME-DOMAIN"})

    @property
    def offsetCorrectionAdaptionInterval_(self):
        return self._artop_offsetCorrectionAdaptionInterval

    @property
    def offsetCorrectionJumpThreshold_(self):
        return self._artop_offsetCorrectionJumpThreshold

    @property
    def rateCorrectionMeasurementDuration_(self):
        return self._artop_rateCorrectionMeasurementDuration

    @property
    def rateCorrectionsPerMeasurementDuration_(self):
        return self._artop_rateCorrectionsPerMeasurementDuration

    @property
    def ref_globalTimeDomain_(self):
        return self._artop_globalTimeDomain

    @property
    def globalTimeDomain_(self):
        if self._artop_globalTimeDomain is not None:
            if hasattr(self._artop_globalTimeDomain, "uuid"):
                return self._artop_globalTimeDomain.uuid
        return
