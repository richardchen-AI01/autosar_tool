# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthGlobalTimeDomainProps.py
from .AbstractGlobalTimeDomainProps import AbstractGlobalTimeDomainProps

class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):

    def __init__(self):
        super().__init__()
        from .EthTSynCrcFlags import EthTSynCrcFlags
        from .EthGlobalTimeManagedCouplingPort import EthGlobalTimeManagedCouplingPort
        self._artop_destinationPhysicalAddress = None
        self._artop_fupDataIdList = None
        self._artop_messageCompliance = None
        self._artop_vlanPriority = None
        self._artop_crcFlags = None
        self._artop_managedCouplingPort = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_crcFlags':"ETH-T-SYN-CRC-FLAGS", 
         '_artop_managedCouplingPort':"ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT"})

    @property
    def destinationPhysicalAddress_(self):
        return self._artop_destinationPhysicalAddress

    @property
    def fupDataIdList_(self):
        return self._artop_fupDataIdList

    @property
    def messageCompliance_(self):
        return self._artop_messageCompliance

    @property
    def vlanPriority_(self):
        return self._artop_vlanPriority

    @property
    def ref_crcFlags_(self):
        return self._artop_crcFlags

    @property
    def crcFlags_(self):
        if self._artop_crcFlags is not None:
            if hasattr(self._artop_crcFlags, "uuid"):
                return self._artop_crcFlags.uuid
        return

    @property
    def managedCouplingPorts_EthGlobalTimeManagedCouplingPort(self):
        return self._artop_managedCouplingPort
