# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeDomain.py
from .FibexElement import FibexElement

class GlobalTimeDomain(FibexElement):

    def __init__(self):
        super().__init__()
        from .CommunicationCluster import CommunicationCluster
        from .GlobalTimeGateway import GlobalTimeGateway
        from .GlobalTimeCorrectionProps import GlobalTimeCorrectionProps
        from .AbstractGlobalTimeDomainProps import AbstractGlobalTimeDomainProps
        from .GlobalTimeMaster import GlobalTimeMaster
        from .GeneralPurposePdu import GeneralPurposePdu
        from .PduTriggering import PduTriggering
        from .GlobalTimeDomainRefConditional import GlobalTimeDomainRefConditional
        from .PduTriggeringRefConditional import PduTriggeringRefConditional
        from .GlobalTimeSlave import GlobalTimeSlave
        self._artop_debounceTime = None
        self._artop_domainId = None
        self._artop_followUpTimeoutValue = None
        self._artop_syncLossThreshold = None
        self._artop_syncLossTimeout = None
        self._artop_communicationClusterRef = []
        self._artop_gateway = []
        self._artop_globalTimeCorrectionProps = None
        self._artop_globalTimeDomainProperty = []
        self._artop_globalTimeDomainProps = None
        self._artop_globalTimeMaster = []
        self._artop_globalTimePduRef = None
        self._artop_globalTimePduTriggeringRef = None
        self._artop_globalTimeSubDomain = []
        self._artop_master = None
        self._artop_offsetTimeDomainRef = None
        self._artop_pduTriggering = []
        self._artop_slave = []
        self._artop_subDomainRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_communicationClusterRef': '"COMMUNICATION-CLUSTER"', 
         '_artop_gateway': '"GLOBAL-TIME-GATEWAY"', 
         '_artop_globalTimeCorrectionProps': '"GLOBAL-TIME-CORRECTION-PROPS"', 
         '_artop_globalTimeDomainProperty': '"ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS"', 
         '_artop_globalTimeDomainProps': '"ABSTRACT-GLOBAL-TIME-DOMAIN-PROPS"', 
         '_artop_globalTimeMaster': '"GLOBAL-TIME-MASTER"', 
         '_artop_globalTimePduRef': '"GENERAL-PURPOSE-PDU"', 
         '_artop_globalTimePduTriggeringRef': '"PDU-TRIGGERING"', 
         '_artop_globalTimeSubDomain': '"GLOBAL-TIME-DOMAIN-REF-CONDITIONAL"', 
         '_artop_master': '"GLOBAL-TIME-MASTER"', 
         '_artop_offsetTimeDomainRef': '"GLOBAL-TIME-DOMAIN"', 
         '_artop_pduTriggering': '"PDU-TRIGGERING-REF-CONDITIONAL"', 
         '_artop_slave': '"GLOBAL-TIME-SLAVE"', 
         '_artop_subDomainRef': '"GLOBAL-TIME-DOMAIN"'})

    @property
    def debounceTime_(self):
        return self._artop_debounceTime

    @property
    def domainId_(self):
        return self._artop_domainId

    @property
    def followUpTimeoutValue_(self):
        return self._artop_followUpTimeoutValue

    @property
    def syncLossThreshold_(self):
        return self._artop_syncLossThreshold

    @property
    def syncLossTimeout_(self):
        return self._artop_syncLossTimeout

    @property
    def ref_communicationClusters_(self):
        return self._artop_communicationClusterRef

    @property
    def communicationClusters_(self):
        return self._artop_communicationClusterRef

    @property
    def gateways_GlobalTimeGateway(self):
        return self._artop_gateway

    @property
    def ref_globalTimeCorrectionProps_(self):
        return self._artop_globalTimeCorrectionProps

    @property
    def globalTimeCorrectionProps_(self):
        if self._artop_globalTimeCorrectionProps is not None:
            if hasattr(self._artop_globalTimeCorrectionProps, "uuid"):
                return self._artop_globalTimeCorrectionProps.uuid
        return

    @property
    def globalTimeDomainProperties_AbstractGlobalTimeDomainProps(self):
        return self._artop_globalTimeDomainProperty

    @property
    def ref_globalTimeDomainProps_(self):
        return self._artop_globalTimeDomainProps

    @property
    def globalTimeDomainProps_(self):
        if self._artop_globalTimeDomainProps is not None:
            if hasattr(self._artop_globalTimeDomainProps, "uuid"):
                return self._artop_globalTimeDomainProps.uuid
        return

    @property
    def globalTimeMasters_GlobalTimeMaster(self):
        return self._artop_globalTimeMaster

    @property
    def ref_globalTimePdu_(self):
        return self._artop_globalTimePduRef

    @property
    def globalTimePdu_(self):
        if self._artop_globalTimePduRef is not None:
            if hasattr(self._artop_globalTimePduRef, "uuid"):
                return self._artop_globalTimePduRef.uuid
        return

    @property
    def ref_globalTimePduTriggering_(self):
        return self._artop_globalTimePduTriggeringRef

    @property
    def globalTimePduTriggering_(self):
        if self._artop_globalTimePduTriggeringRef is not None:
            if hasattr(self._artop_globalTimePduTriggeringRef, "uuid"):
                return self._artop_globalTimePduTriggeringRef.uuid
        return

    @property
    def globalTimeSubDomains_GlobalTimeDomainRefConditional(self):
        return self._artop_globalTimeSubDomain

    @property
    def ref_master_(self):
        return self._artop_master

    @property
    def master_(self):
        if self._artop_master is not None:
            if hasattr(self._artop_master, "uuid"):
                return self._artop_master.uuid
        return

    @property
    def ref_offsetTimeDomain_(self):
        return self._artop_offsetTimeDomainRef

    @property
    def offsetTimeDomain_(self):
        if self._artop_offsetTimeDomainRef is not None:
            if hasattr(self._artop_offsetTimeDomainRef, "uuid"):
                return self._artop_offsetTimeDomainRef.uuid
        return

    @property
    def pduTriggerings_PduTriggeringRefConditional(self):
        return self._artop_pduTriggering

    @property
    def slaves_GlobalTimeSlave(self):
        return self._artop_slave

    @property
    def ref_subDomains_(self):
        return self._artop_subDomainRef

    @property
    def subDomains_(self):
        return self._artop_subDomainRef
