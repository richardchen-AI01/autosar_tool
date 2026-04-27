# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPort.py
from .Identifiable import Identifiable

class CouplingPort(Identifiable):

    def __init__(self):
        super().__init__()
        from .CouplingPortDetails import CouplingPortDetails
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        from .MacMulticastGroup import MacMulticastGroup
        from .PncMappingIdent import PncMappingIdent
        from .VlanMembership import VlanMembership
        from .VariationPoint import VariationPoint
        self._artop_connectionNegotiationBehavior = None
        self._artop_couplingPortRole = None
        self._artop_couplingPortSpeed = None
        self._artop_macLayerType = None
        self._artop_physicalLayerType = None
        self._artop_receiveActivity = None
        self._artop_couplingPortDetails = None
        self._artop_defaultVlanRef = None
        self._artop_macMulticastAddressRef = []
        self._artop_pncMappingRef = []
        self._artop_vlanMembership = []
        self._artop_vlanModifierRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_couplingPortDetails': '"COUPLING-PORT-DETAILS"', 
         '_artop_defaultVlanRef': '"ETHERNET-PHYSICAL-CHANNEL"', 
         '_artop_macMulticastAddressRef': '"MAC-MULTICAST-GROUP"', 
         '_artop_pncMappingRef': '"PNC-MAPPING-IDENT"', 
         '_artop_vlanMembership': '"VLAN-MEMBERSHIP"', 
         '_artop_vlanModifierRef': '"ETHERNET-PHYSICAL-CHANNEL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def connectionNegotiationBehavior_(self):
        return self._artop_connectionNegotiationBehavior

    @property
    def couplingPortRole_(self):
        return self._artop_couplingPortRole

    @property
    def couplingPortSpeed_(self):
        return self._artop_couplingPortSpeed

    @property
    def macLayerType_(self):
        return self._artop_macLayerType

    @property
    def physicalLayerType_(self):
        return self._artop_physicalLayerType

    @property
    def receiveActivity_(self):
        return self._artop_receiveActivity

    @property
    def ref_couplingPortDetails_(self):
        return self._artop_couplingPortDetails

    @property
    def couplingPortDetails_(self):
        if self._artop_couplingPortDetails is not None:
            if hasattr(self._artop_couplingPortDetails, "uuid"):
                return self._artop_couplingPortDetails.uuid
        return

    @property
    def ref_defaultVlan_(self):
        return self._artop_defaultVlanRef

    @property
    def defaultVlan_(self):
        if self._artop_defaultVlanRef is not None:
            if hasattr(self._artop_defaultVlanRef, "uuid"):
                return self._artop_defaultVlanRef.uuid
        return

    @property
    def ref_macMulticastAddress_(self):
        return self._artop_macMulticastAddressRef

    @property
    def macMulticastAddress_(self):
        return self._artop_macMulticastAddressRef

    @property
    def ref_pncMappings_(self):
        return self._artop_pncMappingRef

    @property
    def pncMappings_(self):
        return self._artop_pncMappingRef

    @property
    def vlanMemberships_VlanMembership(self):
        return self._artop_vlanMembership

    @property
    def ref_vlanModifier_(self):
        return self._artop_vlanModifierRef

    @property
    def vlanModifier_(self):
        if self._artop_vlanModifierRef is not None:
            if hasattr(self._artop_vlanModifierRef, "uuid"):
                return self._artop_vlanModifierRef.uuid
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
