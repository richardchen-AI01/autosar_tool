# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInstanceToMachineMapping.py
from .UploadablePackageElement import UploadablePackageElement

class ServiceInstanceToMachineMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .CommunicationConnector import CommunicationConnector
        from .SecOcSecureComProps import SecOcSecureComProps
        from .SecureComProps import SecureComProps
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        self._artop_communicationConnectorRef = None
        self._artop_secOcComPropsForMulticastRef = []
        self._artop_secureComPropsForTcpRef = []
        self._artop_secureComPropsForUdpRef = []
        self._artop_serviceInstanceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_communicationConnectorRef': '"COMMUNICATION-CONNECTOR"', 
         '_artop_secOcComPropsForMulticastRef': '"SEC-OC-SECURE-COM-PROPS"', 
         '_artop_secureComPropsForTcpRef': '"SECURE-COM-PROPS"', 
         '_artop_secureComPropsForUdpRef': '"SECURE-COM-PROPS"', 
         '_artop_serviceInstanceRef': '"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"'})

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
        return

    @property
    def ref_secOcComPropsForMulticasts_(self):
        return self._artop_secOcComPropsForMulticastRef

    @property
    def secOcComPropsForMulticasts_(self):
        return self._artop_secOcComPropsForMulticastRef

    @property
    def ref_secureComPropsForTcps_(self):
        return self._artop_secureComPropsForTcpRef

    @property
    def secureComPropsForTcps_(self):
        return self._artop_secureComPropsForTcpRef

    @property
    def ref_secureComPropsForUdps_(self):
        return self._artop_secureComPropsForUdpRef

    @property
    def secureComPropsForUdps_(self):
        return self._artop_secureComPropsForUdpRef

    @property
    def ref_serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstances_(self):
        return self._artop_serviceInstanceRef
