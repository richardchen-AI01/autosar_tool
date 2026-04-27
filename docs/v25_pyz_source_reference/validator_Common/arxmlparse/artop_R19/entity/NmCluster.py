# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmCluster.py
from .Identifiable import Identifiable

class NmCluster(Identifiable):

    def __init__(self):
        super().__init__()
        from .NmConfig import NmConfig
        from .CommunicationCluster import CommunicationCluster
        from .NmNode import NmNode
        from .VariationPoint import VariationPoint
        self._artop_nmChannelId = None
        self._artop_nmChannelSleepMaster = None
        self._artop_nmNodeDetectionEnabled = None
        self._artop_nmNodeIdEnabled = None
        self._artop_nmPncParticipation = None
        self._artop_nmRepeatMsgIndEnabled = None
        self._artop_nmSynchronizingNetwork = None
        self._artop_nmConfig = None
        self._artop_communicationClusterRef = None
        self._artop_nmNode = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nmConfig': '"NM-CONFIG"', 
         '_artop_communicationClusterRef': '"COMMUNICATION-CLUSTER"', 
         '_artop_nmNode': '"NM-NODE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def nmChannelId_(self):
        return self._artop_nmChannelId

    @property
    def nmChannelSleepMaster_(self):
        if self._artop_nmChannelSleepMaster:
            if self._artop_nmChannelSleepMaster == "true":
                return True
            return False
        else:
            return self._artop_nmChannelSleepMaster

    @property
    def nmNodeDetectionEnabled_(self):
        if self._artop_nmNodeDetectionEnabled:
            if self._artop_nmNodeDetectionEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmNodeDetectionEnabled

    @property
    def nmNodeIdEnabled_(self):
        if self._artop_nmNodeIdEnabled:
            if self._artop_nmNodeIdEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmNodeIdEnabled

    @property
    def nmPncParticipation_(self):
        if self._artop_nmPncParticipation:
            if self._artop_nmPncParticipation == "true":
                return True
            return False
        else:
            return self._artop_nmPncParticipation

    @property
    def nmRepeatMsgIndEnabled_(self):
        if self._artop_nmRepeatMsgIndEnabled:
            if self._artop_nmRepeatMsgIndEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmRepeatMsgIndEnabled

    @property
    def nmSynchronizingNetwork_(self):
        if self._artop_nmSynchronizingNetwork:
            if self._artop_nmSynchronizingNetwork == "true":
                return True
            return False
        else:
            return self._artop_nmSynchronizingNetwork

    @property
    def ref_nmConfig_(self):
        return self._artop_nmConfig

    @property
    def nmConfig_(self):
        if self._artop_nmConfig is not None:
            if hasattr(self._artop_nmConfig, "uuid"):
                return self._artop_nmConfig.uuid
        return

    @property
    def ref_communicationCluster_(self):
        return self._artop_communicationClusterRef

    @property
    def communicationCluster_(self):
        if self._artop_communicationClusterRef is not None:
            if hasattr(self._artop_communicationClusterRef, "uuid"):
                return self._artop_communicationClusterRef.uuid
        return

    @property
    def nmNodes_NmNode(self):
        return self._artop_nmNode

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
