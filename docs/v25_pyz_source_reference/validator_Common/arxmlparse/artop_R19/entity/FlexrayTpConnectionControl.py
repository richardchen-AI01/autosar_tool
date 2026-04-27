# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayTpConnectionControl.py
from .Identifiable import Identifiable

class FlexrayTpConnectionControl(Identifiable):

    def __init__(self):
        super().__init__()
        from .FlexrayTpConfig import FlexrayTpConfig
        from .VariationPoint import VariationPoint
        self._artop_ackType = None
        self._artop_maxAr = None
        self._artop_maxAs = None
        self._artop_maxBufferSize = None
        self._artop_maxFcWait = None
        self._artop_maxFrIf = None
        self._artop_maxNumberOfNpduPerCycle = None
        self._artop_maxRetries = None
        self._artop_separationCycleExponent = None
        self._artop_timeBr = None
        self._artop_timeBuffer = None
        self._artop_timeCs = None
        self._artop_timeFrIf = None
        self._artop_timeoutAr = None
        self._artop_timeoutAs = None
        self._artop_timeoutBr = None
        self._artop_timeoutBs = None
        self._artop_timeoutCr = None
        self._artop_timeoutCs = None
        self._artop_flexrayTpConfig = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flexrayTpConfig':"FLEXRAY-TP-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ackType_(self):
        return self._artop_ackType

    @property
    def maxAr_(self):
        if self._artop_maxAr:
            return int(self._artop_maxAr)
        return self._artop_maxAr

    @property
    def maxAs_(self):
        if self._artop_maxAs:
            return int(self._artop_maxAs)
        return self._artop_maxAs

    @property
    def maxBufferSize_(self):
        if self._artop_maxBufferSize:
            return int(self._artop_maxBufferSize)
        return self._artop_maxBufferSize

    @property
    def maxFcWait_(self):
        if self._artop_maxFcWait:
            return int(self._artop_maxFcWait)
        return self._artop_maxFcWait

    @property
    def maxFrIf_(self):
        if self._artop_maxFrIf:
            return int(self._artop_maxFrIf)
        return self._artop_maxFrIf

    @property
    def maxNumberOfNpduPerCycle_(self):
        if self._artop_maxNumberOfNpduPerCycle:
            return int(self._artop_maxNumberOfNpduPerCycle)
        return self._artop_maxNumberOfNpduPerCycle

    @property
    def maxRetries_(self):
        if self._artop_maxRetries:
            return int(self._artop_maxRetries)
        return self._artop_maxRetries

    @property
    def separationCycleExponent_(self):
        if self._artop_separationCycleExponent:
            return int(self._artop_separationCycleExponent)
        return self._artop_separationCycleExponent

    @property
    def timeBr_(self):
        return self._artop_timeBr

    @property
    def timeBuffer_(self):
        return self._artop_timeBuffer

    @property
    def timeCs_(self):
        return self._artop_timeCs

    @property
    def timeFrIf_(self):
        return self._artop_timeFrIf

    @property
    def timeoutAr_(self):
        return self._artop_timeoutAr

    @property
    def timeoutAs_(self):
        return self._artop_timeoutAs

    @property
    def timeoutBr_(self):
        return self._artop_timeoutBr

    @property
    def timeoutBs_(self):
        return self._artop_timeoutBs

    @property
    def timeoutCr_(self):
        return self._artop_timeoutCr

    @property
    def timeoutCs_(self):
        return self._artop_timeoutCs

    @property
    def ref_flexrayTpConfig_(self):
        return self._artop_flexrayTpConfig

    @property
    def flexrayTpConfig_(self):
        if self._artop_flexrayTpConfig is not None:
            if hasattr(self._artop_flexrayTpConfig, "uuid"):
                return self._artop_flexrayTpConfig.uuid
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
