# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UdpNmCluster.py
from .NmCluster import NmCluster

class UdpNmCluster(NmCluster):

    def __init__(self):
        super().__init__()
        from .UdpNmNetworkConfiguration import UdpNmNetworkConfiguration
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        self._artop_nmCbvPosition = None
        self._artop_nmChannelActive = None
        self._artop_nmImmediateNmCycleTime = None
        self._artop_nmImmediateNmTransmissions = None
        self._artop_nmMessageTimeoutTime = None
        self._artop_nmMsgCycleTime = None
        self._artop_nmNetworkTimeout = None
        self._artop_nmNidPosition = None
        self._artop_nmRemoteSleepIndicationTime = None
        self._artop_nmRepeatMessageTime = None
        self._artop_nmUserDataLength = None
        self._artop_nmUserDataOffset = None
        self._artop_nmWaitBusSleepTime = None
        self._artop_networkConfiguration = None
        self._artop_vlanRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkConfiguration':"UDP-NM-NETWORK-CONFIGURATION", 
         '_artop_vlanRef':"ETHERNET-PHYSICAL-CHANNEL"})

    @property
    def nmCbvPosition_(self):
        if self._artop_nmCbvPosition:
            return int(self._artop_nmCbvPosition)
        return self._artop_nmCbvPosition

    @property
    def nmChannelActive_(self):
        if self._artop_nmChannelActive:
            if self._artop_nmChannelActive == "true":
                return True
            return False
        else:
            return self._artop_nmChannelActive

    @property
    def nmImmediateNmCycleTime_(self):
        return self._artop_nmImmediateNmCycleTime

    @property
    def nmImmediateNmTransmissions_(self):
        return self._artop_nmImmediateNmTransmissions

    @property
    def nmMessageTimeoutTime_(self):
        return self._artop_nmMessageTimeoutTime

    @property
    def nmMsgCycleTime_(self):
        return self._artop_nmMsgCycleTime

    @property
    def nmNetworkTimeout_(self):
        return self._artop_nmNetworkTimeout

    @property
    def nmNidPosition_(self):
        if self._artop_nmNidPosition:
            return int(self._artop_nmNidPosition)
        return self._artop_nmNidPosition

    @property
    def nmRemoteSleepIndicationTime_(self):
        return self._artop_nmRemoteSleepIndicationTime

    @property
    def nmRepeatMessageTime_(self):
        return self._artop_nmRepeatMessageTime

    @property
    def nmUserDataLength_(self):
        if self._artop_nmUserDataLength:
            return int(self._artop_nmUserDataLength)
        return self._artop_nmUserDataLength

    @property
    def nmUserDataOffset_(self):
        return self._artop_nmUserDataOffset

    @property
    def nmWaitBusSleepTime_(self):
        return self._artop_nmWaitBusSleepTime

    @property
    def ref_networkConfiguration_(self):
        return self._artop_networkConfiguration

    @property
    def networkConfiguration_(self):
        if self._artop_networkConfiguration is not None:
            if hasattr(self._artop_networkConfiguration, "uuid"):
                return self._artop_networkConfiguration.uuid
        return

    @property
    def ref_vlan_(self):
        return self._artop_vlanRef

    @property
    def vlan_(self):
        if self._artop_vlanRef is not None:
            if hasattr(self._artop_vlanRef, "uuid"):
                return self._artop_vlanRef.uuid
        return
