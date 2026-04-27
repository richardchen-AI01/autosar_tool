# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SystemMapping.py
from .Identifiable import Identifiable

class SystemMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .System import System
        from .ApplicationPartitionToEcuPartitionMapping import ApplicationPartitionToEcuPartitionMapping
        from .ComManagementMapping import ComManagementMapping
        from .CryptoServiceMapping import CryptoServiceMapping
        from .DataMapping import DataMapping
        from .ECUMapping import ECUMapping
        from .J1939ControllerApplicationToJ1939NmNodeMapping import J1939ControllerApplicationToJ1939NmNodeMapping
        from .MappingConstraint import MappingConstraint
        from .PncMapping import PncMapping
        from .EcuResourceEstimation import EcuResourceEstimation
        from .SignalPathConstraint import SignalPathConstraint
        from .SwcToImplMapping import SwcToImplMapping
        from .SwcToEcuMapping import SwcToEcuMapping
        from .SwcToApplicationPartitionMapping import SwcToApplicationPartitionMapping
        from .VariationPoint import VariationPoint
        self._artop_system = None
        self._artop_applicationPartitionToEcuPartitionMapping = []
        self._artop_comManagementMapping = []
        self._artop_cryptoServiceMapping = []
        self._artop_dataMapping = []
        self._artop_ecuResourceMapping = []
        self._artop_j1939ControllerApplicationToJ1939NmNodeMapping = []
        self._artop_mappingConstraint = []
        self._artop_pncMapping = []
        self._artop_resourceEstimation = []
        self._artop_signalPathConstraint = []
        self._artop_swImplMapping = []
        self._artop_swMapping = []
        self._artop_swcToApplicationPartitionMapping = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_system': '"SYSTEM"', 
         '_artop_applicationPartitionToEcuPartitionMapping': '"APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING"', 
         '_artop_comManagementMapping': '"COM-MANAGEMENT-MAPPING"', 
         '_artop_cryptoServiceMapping': '"CRYPTO-SERVICE-MAPPING"', 
         '_artop_dataMapping': '"DATA-MAPPING"', 
         '_artop_ecuResourceMapping': '"ECU-MAPPING"', 
         '_artop_j1939ControllerApplicationToJ1939NmNodeMapping': '"J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING"', 
         '_artop_mappingConstraint': '"MAPPING-CONSTRAINT"', 
         '_artop_pncMapping': '"PNC-MAPPING"', 
         '_artop_resourceEstimation': '"ECU-RESOURCE-ESTIMATION"', 
         '_artop_signalPathConstraint': '"SIGNAL-PATH-CONSTRAINT"', 
         '_artop_swImplMapping': '"SWC-TO-IMPL-MAPPING"', 
         '_artop_swMapping': '"SWC-TO-ECU-MAPPING"', 
         '_artop_swcToApplicationPartitionMapping': '"SWC-TO-APPLICATION-PARTITION-MAPPING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_system_(self):
        return self._artop_system

    @property
    def system_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def applicationPartitionToEcuPartitionMappings_ApplicationPartitionToEcuPartitionMapping(self):
        return self._artop_applicationPartitionToEcuPartitionMapping

    @property
    def comManagementMappings_ComManagementMapping(self):
        return self._artop_comManagementMapping

    @property
    def cryptoServiceMappings_CryptoServiceMapping(self):
        return self._artop_cryptoServiceMapping

    @property
    def dataMappings_DataMapping(self):
        return self._artop_dataMapping

    @property
    def ecuResourceMappings_ECUMapping(self):
        return self._artop_ecuResourceMapping

    @property
    def j1939ControllerApplicationToJ1939NmNodeMappings_J1939ControllerApplicationToJ1939NmNodeMapping(self):
        return self._artop_j1939ControllerApplicationToJ1939NmNodeMapping

    @property
    def mappingConstraints_MappingConstraint(self):
        return self._artop_mappingConstraint

    @property
    def pncMappings_PncMapping(self):
        return self._artop_pncMapping

    @property
    def resourceEstimations_EcuResourceEstimation(self):
        return self._artop_resourceEstimation

    @property
    def signalPathConstraints_SignalPathConstraint(self):
        return self._artop_signalPathConstraint

    @property
    def swImplMappings_SwcToImplMapping(self):
        return self._artop_swImplMapping

    @property
    def swMappings_SwcToEcuMapping(self):
        return self._artop_swMapping

    @property
    def swcToApplicationPartitionMappings_SwcToApplicationPartitionMapping(self):
        return self._artop_swcToApplicationPartitionMapping

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
