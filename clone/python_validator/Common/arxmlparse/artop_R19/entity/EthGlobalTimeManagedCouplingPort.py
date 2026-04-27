# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthGlobalTimeManagedCouplingPort.py
from .ARObject import ARObject

class EthGlobalTimeManagedCouplingPort(ARObject):

    def __init__(self):
        super().__init__()
        from .EthGlobalTimeDomainProps import EthGlobalTimeDomainProps
        from .CouplingPort import CouplingPort
        self._artop_pdelayLatencyThreshold = None
        self._artop_pdelayRequestPeriod = None
        self._artop_pdelayRespAndRespFollowUpTimeout = None
        self._artop_pdelayResponseEnabled = None
        self._artop_ethGlobalTimeDomainProps = None
        self._artop_couplingPortRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ethGlobalTimeDomainProps':"ETH-GLOBAL-TIME-DOMAIN-PROPS", 
         '_artop_couplingPortRef':"COUPLING-PORT"})

    @property
    def pdelayLatencyThreshold_(self):
        return self._artop_pdelayLatencyThreshold

    @property
    def pdelayRequestPeriod_(self):
        return self._artop_pdelayRequestPeriod

    @property
    def pdelayRespAndRespFollowUpTimeout_(self):
        return self._artop_pdelayRespAndRespFollowUpTimeout

    @property
    def pdelayResponseEnabled_(self):
        if self._artop_pdelayResponseEnabled:
            if self._artop_pdelayResponseEnabled == "true":
                return True
            return False
        else:
            return self._artop_pdelayResponseEnabled

    @property
    def ref_ethGlobalTimeDomainProps_(self):
        return self._artop_ethGlobalTimeDomainProps

    @property
    def ethGlobalTimeDomainProps_(self):
        if self._artop_ethGlobalTimeDomainProps is not None:
            if hasattr(self._artop_ethGlobalTimeDomainProps, "uuid"):
                return self._artop_ethGlobalTimeDomainProps.uuid
        return

    @property
    def ref_couplingPort_(self):
        return self._artop_couplingPortRef

    @property
    def couplingPort_(self):
        if self._artop_couplingPortRef is not None:
            if hasattr(self._artop_couplingPortRef, "uuid"):
                return self._artop_couplingPortRef.uuid
        return
