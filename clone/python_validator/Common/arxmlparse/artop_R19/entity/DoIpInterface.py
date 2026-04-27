# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpInterface.py
from .Identifiable import Identifiable

class DoIpInterface(Identifiable):

    def __init__(self):
        super().__init__()
        from .DoIpConfig import DoIpConfig
        from .DoIpTpConfig import DoIpTpConfig
        from .SocketConnectionBundle import SocketConnectionBundle
        from .StaticSocketConnection import StaticSocketConnection
        self._artop_aliveCheckResponseTimeout = None
        self._artop_generalInactivityTime = None
        self._artop_initialInactivityTime = None
        self._artop_initialVehicleAnnouncementTime = None
        self._artop_isActivationLineDependent = None
        self._artop_maxTesterConnections = None
        self._artop_useMacAddressForIdentification = None
        self._artop_useVehicleIdentificationSyncStatus = None
        self._artop_vehicleAnnouncementCount = None
        self._artop_vehicleAnnouncementInterval = None
        self._artop_doIpConfig = None
        self._artop_doipChannelCollectionRef = None
        self._artop_doipConnectionRef = []
        self._artop_socketConnectionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_doIpConfig': '"DO-IP-CONFIG"', 
         '_artop_doipChannelCollectionRef': '"DO-IP-TP-CONFIG"', 
         '_artop_doipConnectionRef': '"SOCKET-CONNECTION-BUNDLE"', 
         '_artop_socketConnectionRef': '"STATIC-SOCKET-CONNECTION"'})

    @property
    def aliveCheckResponseTimeout_(self):
        return self._artop_aliveCheckResponseTimeout

    @property
    def generalInactivityTime_(self):
        return self._artop_generalInactivityTime

    @property
    def initialInactivityTime_(self):
        return self._artop_initialInactivityTime

    @property
    def initialVehicleAnnouncementTime_(self):
        return self._artop_initialVehicleAnnouncementTime

    @property
    def isActivationLineDependent_(self):
        if self._artop_isActivationLineDependent:
            if self._artop_isActivationLineDependent == "true":
                return True
            return False
        else:
            return self._artop_isActivationLineDependent

    @property
    def maxTesterConnections_(self):
        return self._artop_maxTesterConnections

    @property
    def useMacAddressForIdentification_(self):
        if self._artop_useMacAddressForIdentification:
            if self._artop_useMacAddressForIdentification == "true":
                return True
            return False
        else:
            return self._artop_useMacAddressForIdentification

    @property
    def useVehicleIdentificationSyncStatus_(self):
        if self._artop_useVehicleIdentificationSyncStatus:
            if self._artop_useVehicleIdentificationSyncStatus == "true":
                return True
            return False
        else:
            return self._artop_useVehicleIdentificationSyncStatus

    @property
    def vehicleAnnouncementCount_(self):
        return self._artop_vehicleAnnouncementCount

    @property
    def vehicleAnnouncementInterval_(self):
        return self._artop_vehicleAnnouncementInterval

    @property
    def ref_doIpConfig_(self):
        return self._artop_doIpConfig

    @property
    def doIpConfig_(self):
        if self._artop_doIpConfig is not None:
            if hasattr(self._artop_doIpConfig, "uuid"):
                return self._artop_doIpConfig.uuid
        return

    @property
    def ref_doipChannelCollection_(self):
        return self._artop_doipChannelCollectionRef

    @property
    def doipChannelCollection_(self):
        if self._artop_doipChannelCollectionRef is not None:
            if hasattr(self._artop_doipChannelCollectionRef, "uuid"):
                return self._artop_doipChannelCollectionRef.uuid
        return

    @property
    def ref_doipConnections_(self):
        return self._artop_doipConnectionRef

    @property
    def doipConnections_(self):
        return self._artop_doipConnectionRef

    @property
    def ref_socketConnections_(self):
        return self._artop_socketConnectionRef

    @property
    def socketConnections_(self):
        return self._artop_socketConnectionRef
