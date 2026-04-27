# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhysicalChannel.py
from .Identifiable import Identifiable

class PhysicalChannel(Identifiable):

    def __init__(self):
        super().__init__()
        from .CommunicationClusterContent import CommunicationClusterContent
        from .CommunicationConnectorRefConditional import CommunicationConnectorRefConditional
        from .FrameTriggering import FrameTriggering
        from .ISignalTriggering import ISignalTriggering
        from .PduTriggering import PduTriggering
        from .VariationPoint import VariationPoint
        self._artop_communicationClusterContent = None
        self._artop_commConnector = []
        self._artop_frameTriggering = []
        self._artop_iSignalTriggering = []
        self._artop_managedPhysicalChannelRef = []
        self._artop_pduTriggering = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_communicationClusterContent': '"COMMUNICATION-CLUSTER-CONTENT"', 
         '_artop_commConnector': '"COMMUNICATION-CONNECTOR-REF-CONDITIONAL"', 
         '_artop_frameTriggering': '"FRAME-TRIGGERING"', 
         '_artop_iSignalTriggering': '"I-SIGNAL-TRIGGERING"', 
         '_artop_managedPhysicalChannelRef': '"PHYSICAL-CHANNEL"', 
         '_artop_pduTriggering': '"PDU-TRIGGERING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_communicationClusterContent_(self):
        return self._artop_communicationClusterContent

    @property
    def communicationClusterContent_(self):
        if self._artop_communicationClusterContent is not None:
            if hasattr(self._artop_communicationClusterContent, "uuid"):
                return self._artop_communicationClusterContent.uuid
        return

    @property
    def commConnectors_CommunicationConnectorRefConditional(self):
        return self._artop_commConnector

    @property
    def frameTriggerings_FrameTriggering(self):
        return self._artop_frameTriggering

    @property
    def iSignalTriggerings_ISignalTriggering(self):
        return self._artop_iSignalTriggering

    @property
    def ref_managedPhysicalChannels_(self):
        return self._artop_managedPhysicalChannelRef

    @property
    def managedPhysicalChannels_(self):
        return self._artop_managedPhysicalChannelRef

    @property
    def pduTriggerings_PduTriggering(self):
        return self._artop_pduTriggering

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
