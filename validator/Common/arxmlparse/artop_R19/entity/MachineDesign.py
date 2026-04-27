# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MachineDesign.py
from .FibexElement import FibexElement
from .AtpStructureElement import AtpStructureElement

class MachineDesign(AtpStructureElement, FibexElement):

    def __init__(self):
        super().__init__()
        from .CommunicationConnector import CommunicationConnector
        from .ServiceDiscoveryConfiguration import ServiceDiscoveryConfiguration
        self._artop_accessControl = None
        self._artop_pnResetTimer = None
        self._artop_communicationConnector = []
        self._artop_serviceDiscoverConfig = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_communicationConnector':"COMMUNICATION-CONNECTOR", 
         '_artop_serviceDiscoverConfig':"SERVICE-DISCOVERY-CONFIGURATION"})

    @property
    def accessControl_(self):
        return self._artop_accessControl

    @property
    def pnResetTimer_(self):
        return self._artop_pnResetTimer

    @property
    def communicationConnectors_CommunicationConnector(self):
        return self._artop_communicationConnector

    @property
    def serviceDiscoverConfigs_ServiceDiscoveryConfiguration(self):
        return self._artop_serviceDiscoverConfig
