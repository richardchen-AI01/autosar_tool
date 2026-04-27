# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcuInstance.py
from .FibexElement import FibexElement

class EcuInstance(FibexElement):

    def __init__(self):
        super().__init__()
        from .ISignalIPduGroup import ISignalIPduGroup
        from .ConsumedProvidedServiceInstanceGroupRefConditional import ConsumedProvidedServiceInstanceGroupRefConditional
        from .PdurIPduGroup import PdurIPduGroup
        from .CanTpAddress import CanTpAddress
        from .ClientIdRange import ClientIdRange
        from .CommunicationController import CommunicationController
        from .CommunicationConnector import CommunicationConnector
        from .DiagnosticEcuProps import DiagnosticEcuProps
        from .DltConfig import DltConfig
        from .DoIpConfig import DoIpConfig
        from .EcuInstanceProps import EcuInstanceProps
        from .EcuPartition import EcuPartition
        from .TpAddress import TpAddress
        self._artop_comConfigurationGwTimeBase = None
        self._artop_comConfigurationRxTimeBase = None
        self._artop_comConfigurationTxTimeBase = None
        self._artop_comEnableMdtForCyclicTransmission = None
        self._artop_diagnosticAddress = None
        self._artop_ethSwitchPortGroupDerivation = None
        self._artop_pnResetTime = None
        self._artop_pncPrepareSleepTimer = None
        self._artop_pncSynchronousWakeup = None
        self._artop_sleepModeSupported = None
        self._artop_v2XSupported = None
        self._artop_wakeUpOverBusSupported = None
        self._artop_associatedComIPduGroupRef = []
        self._artop_associatedConsumedProvidedServiceInstanceGroup = []
        self._artop_associatedPdurIPduGroupRef = []
        self._artop_canTpAddressRef = []
        self._artop_clientIdRange = None
        self._artop_commController = []
        self._artop_connector = []
        self._artop_diagnosticProps = None
        self._artop_dltConfig = None
        self._artop_doIpConfig = None
        self._artop_ecuInstanceProps = []
        self._artop_partition = []
        self._artop_tpAddressRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_associatedComIPduGroupRef': '"I-SIGNAL-I-PDU-GROUP"', 
         '_artop_associatedConsumedProvidedServiceInstanceGroup': '"CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL"', 
         '_artop_associatedPdurIPduGroupRef': '"PDUR-I-PDU-GROUP"', 
         '_artop_canTpAddressRef': '"CAN-TP-ADDRESS"', 
         '_artop_clientIdRange': '"CLIENT-ID-RANGE"', 
         '_artop_commController': '"COMMUNICATION-CONTROLLER"', 
         '_artop_connector': '"COMMUNICATION-CONNECTOR"', 
         '_artop_diagnosticProps': '"DIAGNOSTIC-ECU-PROPS"', 
         '_artop_dltConfig': '"DLT-CONFIG"', 
         '_artop_doIpConfig': '"DO-IP-CONFIG"', 
         '_artop_ecuInstanceProps': '"ECU-INSTANCE-PROPS"', 
         '_artop_partition': '"ECU-PARTITION"', 
         '_artop_tpAddressRef': '"TP-ADDRESS"'})

    @property
    def comConfigurationGwTimeBase_(self):
        return self._artop_comConfigurationGwTimeBase

    @property
    def comConfigurationRxTimeBase_(self):
        return self._artop_comConfigurationRxTimeBase

    @property
    def comConfigurationTxTimeBase_(self):
        return self._artop_comConfigurationTxTimeBase

    @property
    def comEnableMdtForCyclicTransmission_(self):
        if self._artop_comEnableMdtForCyclicTransmission:
            if self._artop_comEnableMdtForCyclicTransmission == "true":
                return True
            return False
        else:
            return self._artop_comEnableMdtForCyclicTransmission

    @property
    def diagnosticAddress_(self):
        if self._artop_diagnosticAddress:
            return int(self._artop_diagnosticAddress)
        return self._artop_diagnosticAddress

    @property
    def ethSwitchPortGroupDerivation_(self):
        if self._artop_ethSwitchPortGroupDerivation:
            if self._artop_ethSwitchPortGroupDerivation == "true":
                return True
            return False
        else:
            return self._artop_ethSwitchPortGroupDerivation

    @property
    def pnResetTime_(self):
        return self._artop_pnResetTime

    @property
    def pncPrepareSleepTimer_(self):
        return self._artop_pncPrepareSleepTimer

    @property
    def pncSynchronousWakeup_(self):
        if self._artop_pncSynchronousWakeup:
            if self._artop_pncSynchronousWakeup == "true":
                return True
            return False
        else:
            return self._artop_pncSynchronousWakeup

    @property
    def sleepModeSupported_(self):
        if self._artop_sleepModeSupported:
            if self._artop_sleepModeSupported == "true":
                return True
            return False
        else:
            return self._artop_sleepModeSupported

    @property
    def v2XSupported_(self):
        return self._artop_v2XSupported

    @property
    def wakeUpOverBusSupported_(self):
        if self._artop_wakeUpOverBusSupported:
            if self._artop_wakeUpOverBusSupported == "true":
                return True
            return False
        else:
            return self._artop_wakeUpOverBusSupported

    @property
    def ref_associatedComIPduGroups_(self):
        return self._artop_associatedComIPduGroupRef

    @property
    def associatedComIPduGroups_(self):
        return self._artop_associatedComIPduGroupRef

    @property
    def associatedConsumedProvidedServiceInstanceGroups_ConsumedProvidedServiceInstanceGroupRefConditional(self):
        return self._artop_associatedConsumedProvidedServiceInstanceGroup

    @property
    def ref_associatedPdurIPduGroups_(self):
        return self._artop_associatedPdurIPduGroupRef

    @property
    def associatedPdurIPduGroups_(self):
        return self._artop_associatedPdurIPduGroupRef

    @property
    def ref_canTpAddress_(self):
        return self._artop_canTpAddressRef

    @property
    def canTpAddress_(self):
        return self._artop_canTpAddressRef

    @property
    def ref_clientIdRange_(self):
        return self._artop_clientIdRange

    @property
    def clientIdRange_(self):
        if self._artop_clientIdRange is not None:
            if hasattr(self._artop_clientIdRange, "uuid"):
                return self._artop_clientIdRange.uuid
        return

    @property
    def commControllers_CommunicationController(self):
        return self._artop_commController

    @property
    def connectors_CommunicationConnector(self):
        return self._artop_connector

    @property
    def ref_diagnosticProps_(self):
        return self._artop_diagnosticProps

    @property
    def diagnosticProps_(self):
        if self._artop_diagnosticProps is not None:
            if hasattr(self._artop_diagnosticProps, "uuid"):
                return self._artop_diagnosticProps.uuid
        return

    @property
    def ref_dltConfig_(self):
        return self._artop_dltConfig

    @property
    def dltConfig_(self):
        if self._artop_dltConfig is not None:
            if hasattr(self._artop_dltConfig, "uuid"):
                return self._artop_dltConfig.uuid
        return

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
    def ecuInstanceProps_EcuInstanceProps(self):
        return self._artop_ecuInstanceProps

    @property
    def partitions_EcuPartition(self):
        return self._artop_partition

    @property
    def ref_tpAddress_(self):
        return self._artop_tpAddressRef

    @property
    def tpAddress_(self):
        return self._artop_tpAddressRef
