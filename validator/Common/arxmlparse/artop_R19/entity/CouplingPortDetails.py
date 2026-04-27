# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortDetails.py
from .ARObject import ARObject

class CouplingPortDetails(ARObject):

    def __init__(self):
        super().__init__()
        from .CouplingPort import CouplingPort
        from .CouplingPortStructuralElement import CouplingPortStructuralElement
        from .EthernetPriorityRegeneration import EthernetPriorityRegeneration
        from .CouplingPortTrafficClassAssignment import CouplingPortTrafficClassAssignment
        from .GlobalTimeCouplingPortProps import GlobalTimeCouplingPortProps
        from .CouplingPortScheduler import CouplingPortScheduler
        from .CouplingPortRatePolicy import CouplingPortRatePolicy
        self._artop_couplingPort = None
        self._artop_couplingPortStructuralElement = []
        self._artop_ethernetPriorityRegeneration = []
        self._artop_ethernetTrafficClassAssignment = []
        self._artop_globalTimeProps = None
        self._artop_lastEgressSchedulerRef = None
        self._artop_ratePolicy = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_couplingPort': '"COUPLING-PORT"', 
         '_artop_couplingPortStructuralElement': '"COUPLING-PORT-STRUCTURAL-ELEMENT"', 
         '_artop_ethernetPriorityRegeneration': '"ETHERNET-PRIORITY-REGENERATION"', 
         '_artop_ethernetTrafficClassAssignment': '"COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT"', 
         '_artop_globalTimeProps': '"GLOBAL-TIME-COUPLING-PORT-PROPS"', 
         '_artop_lastEgressSchedulerRef': '"COUPLING-PORT-SCHEDULER"', 
         '_artop_ratePolicy': '"COUPLING-PORT-RATE-POLICY"'})

    @property
    def ref_couplingPort_(self):
        return self._artop_couplingPort

    @property
    def couplingPort_(self):
        if self._artop_couplingPort is not None:
            if hasattr(self._artop_couplingPort, "uuid"):
                return self._artop_couplingPort.uuid
        return

    @property
    def couplingPortStructuralElements_CouplingPortStructuralElement(self):
        return self._artop_couplingPortStructuralElement

    @property
    def ethernetPriorityRegenerations_EthernetPriorityRegeneration(self):
        return self._artop_ethernetPriorityRegeneration

    @property
    def ethernetTrafficClassAssignments_CouplingPortTrafficClassAssignment(self):
        return self._artop_ethernetTrafficClassAssignment

    @property
    def ref_globalTimeProps_(self):
        return self._artop_globalTimeProps

    @property
    def globalTimeProps_(self):
        if self._artop_globalTimeProps is not None:
            if hasattr(self._artop_globalTimeProps, "uuid"):
                return self._artop_globalTimeProps.uuid
        return

    @property
    def ref_lastEgressScheduler_(self):
        return self._artop_lastEgressSchedulerRef

    @property
    def lastEgressScheduler_(self):
        if self._artop_lastEgressSchedulerRef is not None:
            if hasattr(self._artop_lastEgressSchedulerRef, "uuid"):
                return self._artop_lastEgressSchedulerRef.uuid
        return

    @property
    def ratePolicies_CouplingPortRatePolicy(self):
        return self._artop_ratePolicy
