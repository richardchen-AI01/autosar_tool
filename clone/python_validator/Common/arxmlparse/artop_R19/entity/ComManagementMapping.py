# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComManagementMapping.py
from .Identifiable import Identifiable

class ComManagementMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .ISignalIPduGroup import ISignalIPduGroup
        from .PortGroupInSystemInstanceRef import PortGroupInSystemInstanceRef
        from .PhysicalChannel import PhysicalChannel
        from .VariationPoint import VariationPoint
        self._artop_systemMapping = None
        self._artop_comManagementGroupRef = []
        self._artop_comManagementPortGroupIref = []
        self._artop_physicalChannelRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_comManagementGroupRef': '"I-SIGNAL-I-PDU-GROUP"', 
         '_artop_comManagementPortGroupIref': '"PORT-GROUP-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_physicalChannelRef': '"PHYSICAL-CHANNEL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def ref_comManagementGroups_(self):
        return self._artop_comManagementGroupRef

    @property
    def comManagementGroups_(self):
        return self._artop_comManagementGroupRef

    @property
    def comManagementPortGroups_PortGroupInSystemInstanceRef(self):
        return self._artop_comManagementPortGroupIref

    @property
    def ref_physicalChannels_(self):
        return self._artop_physicalChannelRef

    @property
    def physicalChannels_(self):
        return self._artop_physicalChannelRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
