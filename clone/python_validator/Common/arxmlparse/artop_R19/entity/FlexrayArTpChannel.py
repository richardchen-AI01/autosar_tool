# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayArTpChannel.py
from .ARObject import ARObject

class FlexrayArTpChannel(ARObject):

    def __init__(self):
        super().__init__()
        from .FlexrayArTpConfig import FlexrayArTpConfig
        from .NPdu import NPdu
        from .FlexrayArTpConnection import FlexrayArTpConnection
        from .VariationPoint import VariationPoint
        self._artop_ackType = None
        self._artop_cancellation = None
        self._artop_extendedAddressing = None
        self._artop_maxAr = None
        self._artop_maxAs = None
        self._artop_maxBs = None
        self._artop_maxBufferRequest = None
        self._artop_maxFcWait = None
        self._artop_maxFrIf = None
        self._artop_maxRetries = None
        self._artop_maximumMessageLength = None
        self._artop_minimumMulticastSeperationTime = None
        self._artop_minimumSeparationTime = None
        self._artop_multicastSegmentation = None
        self._artop_timeBr = None
        self._artop_timeBuffer = None
        self._artop_timeCs = None
        self._artop_timeFrIf = None
        self._artop_timeoutAr = None
        self._artop_timeoutAs = None
        self._artop_timeoutBs = None
        self._artop_timeoutCr = None
        self._artop_transmitCancellation = None
        self._artop_flexrayArTpConfig = None
        self._artop_flowControlPduRef = None
        self._artop_nPduRef = []
        self._artop_pduPool = []
        self._artop_tpConnection = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flexrayArTpConfig': '"FLEXRAY-AR-TP-CONFIG"', 
         '_artop_flowControlPduRef': '"N-PDU"', 
         '_artop_nPduRef': '"N-PDU"', 
         '_artop_pduPool': '"N-PDU"', 
         '_artop_tpConnection': '"FLEXRAY-AR-TP-CONNECTION"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ackType_(self):
        return self._artop_ackType

    @property
    def cancellation_(self):
        if self._artop_cancellation:
            if self._artop_cancellation == "true":
                return True
            return False
        else:
            return self._artop_cancellation

    @property
    def extendedAddressing_(self):
        if self._artop_extendedAddressing:
            if self._artop_extendedAddressing == "true":
                return True
            return False
        else:
            return self._artop_extendedAddressing

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
    def maxBs_(self):
        if self._artop_maxBs:
            return int(self._artop_maxBs)
        return self._artop_maxBs

    @property
    def maxBufferRequest_(self):
        if self._artop_maxBufferRequest:
            return int(self._artop_maxBufferRequest)
        return self._artop_maxBufferRequest

    @property
    def maxFcWait_(self):
        return self._artop_maxFcWait

    @property
    def maxFrIf_(self):
        if self._artop_maxFrIf:
            return int(self._artop_maxFrIf)
        return self._artop_maxFrIf

    @property
    def maxRetries_(self):
        if self._artop_maxRetries:
            return int(self._artop_maxRetries)
        return self._artop_maxRetries

    @property
    def maximumMessageLength_(self):
        return self._artop_maximumMessageLength

    @property
    def minimumMulticastSeperationTime_(self):
        return self._artop_minimumMulticastSeperationTime

    @property
    def minimumSeparationTime_(self):
        return self._artop_minimumSeparationTime

    @property
    def multicastSegmentation_(self):
        if self._artop_multicastSegmentation:
            if self._artop_multicastSegmentation == "true":
                return True
            return False
        else:
            return self._artop_multicastSegmentation

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
    def timeoutBs_(self):
        return self._artop_timeoutBs

    @property
    def timeoutCr_(self):
        return self._artop_timeoutCr

    @property
    def transmitCancellation_(self):
        if self._artop_transmitCancellation:
            if self._artop_transmitCancellation == "true":
                return True
            return False
        else:
            return self._artop_transmitCancellation

    @property
    def ref_flexrayArTpConfig_(self):
        return self._artop_flexrayArTpConfig

    @property
    def flexrayArTpConfig_(self):
        if self._artop_flexrayArTpConfig is not None:
            if hasattr(self._artop_flexrayArTpConfig, "uuid"):
                return self._artop_flexrayArTpConfig.uuid
        return

    @property
    def ref_flowControlPdu_(self):
        return self._artop_flowControlPduRef

    @property
    def flowControlPdu_(self):
        if self._artop_flowControlPduRef is not None:
            if hasattr(self._artop_flowControlPduRef, "uuid"):
                return self._artop_flowControlPduRef.uuid
        return

    @property
    def ref_nPdus_(self):
        return self._artop_nPduRef

    @property
    def nPdus_(self):
        return self._artop_nPduRef

    @property
    def pduPools_NPdu(self):
        return self._artop_pduPool

    @property
    def tpConnections_FlexrayArTpConnection(self):
        return self._artop_tpConnection

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
