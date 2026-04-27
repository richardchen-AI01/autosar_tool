# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractServiceInstance.py
from .Identifiable import Identifiable

class AbstractServiceInstance(Identifiable):

    def __init__(self):
        super().__init__()
        from .ServiceInstanceCollectionSet import ServiceInstanceCollectionSet
        from .TagWithOptionalValue import TagWithOptionalValue
        from .PduActivationRoutingGroup import PduActivationRoutingGroup
        from .SoAdRoutingGroup import SoAdRoutingGroup
        from .VariationPoint import VariationPoint
        self._artop_majorVersion = None
        self._artop_serviceInstanceCollectionSet = None
        self._artop_capabilityRecord = []
        self._artop_methodActivationRoutingGroup = []
        self._artop_routingGroupRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_serviceInstanceCollectionSet': '"SERVICE-INSTANCE-COLLECTION-SET"', 
         '_artop_capabilityRecord': '"TAG-WITH-OPTIONAL-VALUE"', 
         '_artop_methodActivationRoutingGroup': '"PDU-ACTIVATION-ROUTING-GROUP"', 
         '_artop_routingGroupRef': '"SO-AD-ROUTING-GROUP"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def majorVersion_(self):
        return self._artop_majorVersion

    @property
    def ref_serviceInstanceCollectionSet_(self):
        return self._artop_serviceInstanceCollectionSet

    @property
    def serviceInstanceCollectionSet_(self):
        if self._artop_serviceInstanceCollectionSet is not None:
            if hasattr(self._artop_serviceInstanceCollectionSet, "uuid"):
                return self._artop_serviceInstanceCollectionSet.uuid
        return

    @property
    def capabilityRecords_TagWithOptionalValue(self):
        return self._artop_capabilityRecord

    @property
    def methodActivationRoutingGroups_PduActivationRoutingGroup(self):
        return self._artop_methodActivationRoutingGroup

    @property
    def ref_routingGroups_(self):
        return self._artop_routingGroupRef

    @property
    def routingGroups_(self):
        return self._artop_routingGroupRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
