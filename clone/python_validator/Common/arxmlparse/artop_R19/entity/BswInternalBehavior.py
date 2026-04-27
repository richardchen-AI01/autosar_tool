# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswInternalBehavior.py
from .InternalBehavior import InternalBehavior

class BswInternalBehavior(InternalBehavior):

    def __init__(self):
        super().__init__()
        from .BswModuleDescription import BswModuleDescription
        from .VariableDataPrototype import VariableDataPrototype
        from .BswPerInstanceMemoryPolicy import BswPerInstanceMemoryPolicy
        from .BswClientPolicy import BswClientPolicy
        from .BswExclusiveAreaPolicy import BswExclusiveAreaPolicy
        from .IncludedDataTypeSet import IncludedDataTypeSet
        from .BswInternalTriggeringPointPolicy import BswInternalTriggeringPointPolicy
        from .BswParameterPolicy import BswParameterPolicy
        from .BswReleasedTriggerPolicy import BswReleasedTriggerPolicy
        from .BswDataSendPolicy import BswDataSendPolicy
        from .VariationPointProxy import VariationPointProxy
        from .BswInternalTriggeringPoint import BswInternalTriggeringPoint
        from .BswModuleEntity import BswModuleEntity
        from .BswEvent import BswEvent
        from .BswTriggerDirectImplementation import BswTriggerDirectImplementation
        from .BswModeSenderPolicy import BswModeSenderPolicy
        from .BswModeReceiverPolicy import BswModeReceiverPolicy
        from .BswServiceDependency import BswServiceDependency
        from .ParameterDataPrototype import ParameterDataPrototype
        from .BswSchedulerNamePrefix import BswSchedulerNamePrefix
        from .BswDataReceptionPolicy import BswDataReceptionPolicy
        from .BswDistinguishedPartition import BswDistinguishedPartition
        self._artop_bswModuleDescription = None
        self._artop_arTypedPerInstanceMemory = []
        self._artop_bswPerInstanceMemoryPolicy = []
        self._artop_clientPolicy = []
        self._artop_exclusiveAreaPolicy = []
        self._artop_includedDataTypeSet = []
        self._artop_internalTriggeringPointPolicy = []
        self._artop_parameterPolicy = []
        self._artop_releasedTriggerPolicy = []
        self._artop_sendPolicy = []
        self._artop_variationPointProxy = []
        self._artop_internalTriggeringPoint = []
        self._artop_entity = []
        self._artop_event = []
        self._artop_triggerDirectImplementation = []
        self._artop_modeSenderPolicy = []
        self._artop_modeReceiverPolicy = []
        self._artop_serviceDependency = []
        self._artop_perInstanceParameter = []
        self._artop_schedulerNamePrefix = []
        self._artop_receptionPolicy = []
        self._artop_distinguishedPartition = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswModuleDescription': '"BSW-MODULE-DESCRIPTION"', 
         '_artop_arTypedPerInstanceMemory': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_bswPerInstanceMemoryPolicy': '"BSW-PER-INSTANCE-MEMORY-POLICY"', 
         '_artop_clientPolicy': '"BSW-CLIENT-POLICY"', 
         '_artop_exclusiveAreaPolicy': '"BSW-EXCLUSIVE-AREA-POLICY"', 
         '_artop_includedDataTypeSet': '"INCLUDED-DATA-TYPE-SET"', 
         '_artop_internalTriggeringPointPolicy': '"BSW-INTERNAL-TRIGGERING-POINT-POLICY"', 
         '_artop_parameterPolicy': '"BSW-PARAMETER-POLICY"', 
         '_artop_releasedTriggerPolicy': '"BSW-RELEASED-TRIGGER-POLICY"', 
         '_artop_sendPolicy': '"BSW-DATA-SEND-POLICY"', 
         '_artop_variationPointProxy': '"VARIATION-POINT-PROXY"', 
         '_artop_internalTriggeringPoint': '"BSW-INTERNAL-TRIGGERING-POINT"', 
         '_artop_entity': '"BSW-MODULE-ENTITY"', 
         '_artop_event': '"BSW-EVENT"', 
         '_artop_triggerDirectImplementation': '"BSW-TRIGGER-DIRECT-IMPLEMENTATION"', 
         '_artop_modeSenderPolicy': '"BSW-MODE-SENDER-POLICY"', 
         '_artop_modeReceiverPolicy': '"BSW-MODE-RECEIVER-POLICY"', 
         '_artop_serviceDependency': '"BSW-SERVICE-DEPENDENCY"', 
         '_artop_perInstanceParameter': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_schedulerNamePrefix': '"BSW-SCHEDULER-NAME-PREFIX"', 
         '_artop_receptionPolicy': '"BSW-DATA-RECEPTION-POLICY"', 
         '_artop_distinguishedPartition': '"BSW-DISTINGUISHED-PARTITION"'})

    @property
    def ref_bswModuleDescription_(self):
        return self._artop_bswModuleDescription

    @property
    def bswModuleDescription_(self):
        if self._artop_bswModuleDescription is not None:
            if hasattr(self._artop_bswModuleDescription, "uuid"):
                return self._artop_bswModuleDescription.uuid
        return

    @property
    def arTypedPerInstanceMemories_VariableDataPrototype(self):
        return self._artop_arTypedPerInstanceMemory

    @property
    def bswPerInstanceMemoryPolicies_BswPerInstanceMemoryPolicy(self):
        return self._artop_bswPerInstanceMemoryPolicy

    @property
    def clientPolicies_BswClientPolicy(self):
        return self._artop_clientPolicy

    @property
    def exclusiveAreaPolicies_BswExclusiveAreaPolicy(self):
        return self._artop_exclusiveAreaPolicy

    @property
    def includedDataTypeSets_IncludedDataTypeSet(self):
        return self._artop_includedDataTypeSet

    @property
    def internalTriggeringPointPolicies_BswInternalTriggeringPointPolicy(self):
        return self._artop_internalTriggeringPointPolicy

    @property
    def parameterPolicies_BswParameterPolicy(self):
        return self._artop_parameterPolicy

    @property
    def releasedTriggerPolicies_BswReleasedTriggerPolicy(self):
        return self._artop_releasedTriggerPolicy

    @property
    def sendPolicies_BswDataSendPolicy(self):
        return self._artop_sendPolicy

    @property
    def variationPointProxies_VariationPointProxy(self):
        return self._artop_variationPointProxy

    @property
    def internalTriggeringPoints_BswInternalTriggeringPoint(self):
        return self._artop_internalTriggeringPoint

    @property
    def entities_BswModuleEntity(self):
        return self._artop_entity

    @property
    def events_BswEvent(self):
        return self._artop_event

    @property
    def triggerDirectImplementations_BswTriggerDirectImplementation(self):
        return self._artop_triggerDirectImplementation

    @property
    def modeSenderPolicies_BswModeSenderPolicy(self):
        return self._artop_modeSenderPolicy

    @property
    def modeReceiverPolicies_BswModeReceiverPolicy(self):
        return self._artop_modeReceiverPolicy

    @property
    def serviceDependencies_BswServiceDependency(self):
        return self._artop_serviceDependency

    @property
    def perInstanceParameters_ParameterDataPrototype(self):
        return self._artop_perInstanceParameter

    @property
    def schedulerNamePrefixs_BswSchedulerNamePrefix(self):
        return self._artop_schedulerNamePrefix

    @property
    def receptionPolicies_BswDataReceptionPolicy(self):
        return self._artop_receptionPolicy

    @property
    def distinguishedPartitions_BswDistinguishedPartition(self):
        return self._artop_distinguishedPartition
