# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpNetworkConfiguration.py
from .ARObject import ARObject

class DoIpNetworkConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .DoIpInstantiation import DoIpInstantiation
        from .EthernetNetworkConfiguration import EthernetNetworkConfiguration
        self._artop_eidUseMac = None
        self._artop_isActivationLineDependent = None
        self._artop_maxInitialVehicleAnnouncementTime = None
        self._artop_maxTesterConnections = None
        self._artop_networkInterfaceId = None
        self._artop_tcpAliveCheckResponseTimeout = None
        self._artop_tcpGeneralInactivityTime = None
        self._artop_tcpInitialInactivityTime = None
        self._artop_vehicleAnnouncementCount = None
        self._artop_vehicleAnnouncementInterval = None
        self._artop_vehicleIdentificationSyncStatus = None
        self._artop_doIpInstantiation = None
        self._artop_networkConfiguration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_doIpInstantiation':"DO-IP-INSTANTIATION", 
         '_artop_networkConfiguration':"ETHERNET-NETWORK-CONFIGURATION"})

    @property
    def eidUseMac_(self):
        if self._artop_eidUseMac:
            if self._artop_eidUseMac == "true":
                return True
            return False
        else:
            return self._artop_eidUseMac

    @property
    def isActivationLineDependent_(self):
        if self._artop_isActivationLineDependent:
            if self._artop_isActivationLineDependent == "true":
                return True
            return False
        else:
            return self._artop_isActivationLineDependent

    @property
    def maxInitialVehicleAnnouncementTime_(self):
        return self._artop_maxInitialVehicleAnnouncementTime

    @property
    def maxTesterConnections_(self):
        return self._artop_maxTesterConnections

    @property
    def networkInterfaceId_(self):
        return self._artop_networkInterfaceId

    @property
    def tcpAliveCheckResponseTimeout_(self):
        return self._artop_tcpAliveCheckResponseTimeout

    @property
    def tcpGeneralInactivityTime_(self):
        return self._artop_tcpGeneralInactivityTime

    @property
    def tcpInitialInactivityTime_(self):
        return self._artop_tcpInitialInactivityTime

    @property
    def vehicleAnnouncementCount_(self):
        return self._artop_vehicleAnnouncementCount

    @property
    def vehicleAnnouncementInterval_(self):
        return self._artop_vehicleAnnouncementInterval

    @property
    def vehicleIdentificationSyncStatus_(self):
        if self._artop_vehicleIdentificationSyncStatus:
            if self._artop_vehicleIdentificationSyncStatus == "true":
                return True
            return False
        else:
            return self._artop_vehicleIdentificationSyncStatus

    @property
    def ref_doIpInstantiation_(self):
        return self._artop_doIpInstantiation

    @property
    def doIpInstantiation_(self):
        if self._artop_doIpInstantiation is not None:
            if hasattr(self._artop_doIpInstantiation, "uuid"):
                return self._artop_doIpInstantiation.uuid
        return

    @property
    def ref_networkConfiguration_(self):
        return self._artop_networkConfiguration

    @property
    def networkConfiguration_(self):
        if self._artop_networkConfiguration is not None:
            if hasattr(self._artop_networkConfiguration, "uuid"):
                return self._artop_networkConfiguration.uuid
        return
