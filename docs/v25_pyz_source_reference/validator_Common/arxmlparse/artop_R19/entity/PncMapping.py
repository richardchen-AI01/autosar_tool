# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PncMapping.py
from .Describable import Describable

class PncMapping(Describable):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .PncMappingIdent import PncMappingIdent
        from .PhysicalChannel import PhysicalChannel
        from .ConsumedProvidedServiceInstanceGroupRefConditional import ConsumedProvidedServiceInstanceGroupRefConditional
        from .ISignalIPduGroup import ISignalIPduGroup
        from .PdurIPduGroup import PdurIPduGroup
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        from .PortGroupInSystemInstanceRef import PortGroupInSystemInstanceRef
        from .FrameTriggering import FrameTriggering
        from .VariationPoint import VariationPoint
        self._artop_pncIdentifier = None
        self._artop_pncWakeupEnable = None
        self._artop_shortLabel = None
        self._artop_systemMapping = None
        self._artop_ident = None
        self._artop_physicalChannelRef = []
        self._artop_pncConsumedProvidedServiceInstanceGroup = []
        self._artop_pncGroupRef = []
        self._artop_pncPdurGroupRef = []
        self._artop_serviceInstanceRef = []
        self._artop_vfcIref = []
        self._artop_wakeupFrameRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_ident': '"PNC-MAPPING-IDENT"', 
         '_artop_physicalChannelRef': '"PHYSICAL-CHANNEL"', 
         '_artop_pncConsumedProvidedServiceInstanceGroup': '"CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL"', 
         '_artop_pncGroupRef': '"I-SIGNAL-I-PDU-GROUP"', 
         '_artop_pncPdurGroupRef': '"PDUR-I-PDU-GROUP"', 
         '_artop_serviceInstanceRef': '"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"', 
         '_artop_vfcIref': '"PORT-GROUP-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_wakeupFrameRef': '"FRAME-TRIGGERING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def pncIdentifier_(self):
        return self._artop_pncIdentifier

    @property
    def pncWakeupEnable_(self):
        if self._artop_pncWakeupEnable:
            if self._artop_pncWakeupEnable == "true":
                return True
            return False
        else:
            return self._artop_pncWakeupEnable

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_systemMapping_(self):
        return self._artop_systemMapping

    @property
    def systemMapping_(self):
        if self._artop_systemMapping is not None:
            if hasattr(self._artop_systemMapping, "uuid"):
                return self._artop_systemMapping.uuid
        return

    @property
    def ref_ident_(self):
        return self._artop_ident

    @property
    def ident_(self):
        if self._artop_ident is not None:
            if hasattr(self._artop_ident, "uuid"):
                return self._artop_ident.uuid
        return

    @property
    def ref_physicalChannels_(self):
        return self._artop_physicalChannelRef

    @property
    def physicalChannels_(self):
        return self._artop_physicalChannelRef

    @property
    def pncConsumedProvidedServiceInstanceGroups_ConsumedProvidedServiceInstanceGroupRefConditional(self):
        return self._artop_pncConsumedProvidedServiceInstanceGroup

    @property
    def ref_pncGroups_(self):
        return self._artop_pncGroupRef

    @property
    def pncGroups_(self):
        return self._artop_pncGroupRef

    @property
    def ref_pncPdurGroups_(self):
        return self._artop_pncPdurGroupRef

    @property
    def pncPdurGroups_(self):
        return self._artop_pncPdurGroupRef

    @property
    def ref_serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def vfcs_PortGroupInSystemInstanceRef(self):
        return self._artop_vfcIref

    @property
    def ref_wakeupFrames_(self):
        return self._artop_wakeupFrameRef

    @property
    def wakeupFrames_(self):
        return self._artop_wakeupFrameRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
