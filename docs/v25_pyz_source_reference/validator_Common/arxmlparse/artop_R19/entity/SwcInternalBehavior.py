# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcInternalBehavior.py
from .InternalBehavior import InternalBehavior

class SwcInternalBehavior(InternalBehavior):

    def __init__(self):
        super().__init__()
        from .AtomicSwComponentType import AtomicSwComponentType
        from .VariableDataPrototype import VariableDataPrototype
        from .RTEEvent import RTEEvent
        from .SwcExclusiveAreaPolicy import SwcExclusiveAreaPolicy
        from .IncludedDataTypeSet import IncludedDataTypeSet
        from .IncludedModeDeclarationGroupSet import IncludedModeDeclarationGroupSet
        from .InstantiationDataDefProps import InstantiationDataDefProps
        from .PerInstanceMemory import PerInstanceMemory
        from .ParameterDataPrototype import ParameterDataPrototype
        from .PortAPIOption import PortAPIOption
        from .RunnableEntity import RunnableEntity
        from .SwcServiceDependency import SwcServiceDependency
        from .VariationPointProxy import VariationPointProxy
        from .VariationPoint import VariationPoint
        self._artop_handleTerminationAndRestart = None
        self._artop_supportsMultipleInstantiation = None
        self._artop_atomicSwComponentType = None
        self._artop_arTypedPerInstanceMemory = []
        self._artop_event = []
        self._artop_exclusiveAreaPolicy = []
        self._artop_explicitInterRunnableVariable = []
        self._artop_implicitInterRunnableVariable = []
        self._artop_includedDataTypeSet = []
        self._artop_includedModeDeclarationGroupSet = []
        self._artop_instantiationDataDefProps = []
        self._artop_perInstanceMemory = []
        self._artop_perInstanceParameter = []
        self._artop_portApiOption = []
        self._artop_runnable = []
        self._artop_serviceDependency = []
        self._artop_sharedParameter = []
        self._artop_variationPointProxy = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"', 
         '_artop_arTypedPerInstanceMemory': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_event': '"RTE-EVENT"', 
         '_artop_exclusiveAreaPolicy': '"SWC-EXCLUSIVE-AREA-POLICY"', 
         '_artop_explicitInterRunnableVariable': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_implicitInterRunnableVariable': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_includedDataTypeSet': '"INCLUDED-DATA-TYPE-SET"', 
         '_artop_includedModeDeclarationGroupSet': '"INCLUDED-MODE-DECLARATION-GROUP-SET"', 
         '_artop_instantiationDataDefProps': '"INSTANTIATION-DATA-DEF-PROPS"', 
         '_artop_perInstanceMemory': '"PER-INSTANCE-MEMORY"', 
         '_artop_perInstanceParameter': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_portApiOption': '"PORT-API-OPTION"', 
         '_artop_runnable': '"RUNNABLE-ENTITY"', 
         '_artop_serviceDependency': '"SWC-SERVICE-DEPENDENCY"', 
         '_artop_sharedParameter': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_variationPointProxy': '"VARIATION-POINT-PROXY"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def handleTerminationAndRestart_(self):
        return self._artop_handleTerminationAndRestart

    @property
    def supportsMultipleInstantiation_(self):
        if self._artop_supportsMultipleInstantiation:
            if self._artop_supportsMultipleInstantiation == "true":
                return True
            return False
        else:
            return self._artop_supportsMultipleInstantiation

    @property
    def ref_atomicSwComponentType_(self):
        return self._artop_atomicSwComponentType

    @property
    def atomicSwComponentType_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return

    @property
    def arTypedPerInstanceMemories_VariableDataPrototype(self):
        return self._artop_arTypedPerInstanceMemory

    @property
    def events_RTEEvent(self):
        return self._artop_event

    @property
    def exclusiveAreaPolicies_SwcExclusiveAreaPolicy(self):
        return self._artop_exclusiveAreaPolicy

    @property
    def explicitInterRunnableVariables_VariableDataPrototype(self):
        return self._artop_explicitInterRunnableVariable

    @property
    def implicitInterRunnableVariables_VariableDataPrototype(self):
        return self._artop_implicitInterRunnableVariable

    @property
    def includedDataTypeSets_IncludedDataTypeSet(self):
        return self._artop_includedDataTypeSet

    @property
    def includedModeDeclarationGroupSets_IncludedModeDeclarationGroupSet(self):
        return self._artop_includedModeDeclarationGroupSet

    @property
    def instantiationDataDefProps_InstantiationDataDefProps(self):
        return self._artop_instantiationDataDefProps

    @property
    def perInstanceMemories_PerInstanceMemory(self):
        return self._artop_perInstanceMemory

    @property
    def perInstanceParameters_ParameterDataPrototype(self):
        return self._artop_perInstanceParameter

    @property
    def portAPIOptions_PortAPIOption(self):
        return self._artop_portApiOption

    @property
    def runnables_RunnableEntity(self):
        return self._artop_runnable

    @property
    def serviceDependencies_SwcServiceDependency(self):
        return self._artop_serviceDependency

    @property
    def sharedParameters_ParameterDataPrototype(self):
        return self._artop_sharedParameter

    @property
    def variationPointProxies_VariationPointProxy(self):
        return self._artop_variationPointProxy

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
