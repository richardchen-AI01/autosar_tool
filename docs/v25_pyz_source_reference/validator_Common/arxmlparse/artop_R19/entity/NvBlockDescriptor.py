# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvBlockDescriptor.py
from .AtpStructureElement import AtpStructureElement

class NvBlockDescriptor(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .NvBlockSwComponentType import NvBlockSwComponentType
        from .RoleBasedPortAssignment import RoleBasedPortAssignment
        from .ConstantSpecificationMappingSet import ConstantSpecificationMappingSet
        from .DataTypeMappingSet import DataTypeMappingSet
        from .InstantiationDataDefProps import InstantiationDataDefProps
        from .ModeSwitchEventTriggeredActivity import ModeSwitchEventTriggeredActivity
        from .NvBlockDataMapping import NvBlockDataMapping
        from .NvBlockNeeds import NvBlockNeeds
        from .VariableDataPrototype import VariableDataPrototype
        from .ParameterDataPrototype import ParameterDataPrototype
        from .TimingEvent import TimingEvent
        from .RoleBasedDataAssignment import RoleBasedDataAssignment
        from .VariationPoint import VariationPoint
        self._artop_supportDirtyFlag = None
        self._artop_nvBlockSwComponentType = None
        self._artop_clientServerPort = []
        self._artop_constantValueMappingRef = []
        self._artop_dataTypeMappingRef = []
        self._artop_instantiationDataDefProps = []
        self._artop_modeSwitchEventTriggeredActivity = []
        self._artop_nvBlockDataMapping = []
        self._artop_nvBlockNeeds = None
        self._artop_ramBlock = None
        self._artop_romBlock = None
        self._artop_timingEventRef = None
        self._artop_writingStrategyRole = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_nvBlockSwComponentType': '"NV-BLOCK-SW-COMPONENT-TYPE"', 
         '_artop_clientServerPort': '"ROLE-BASED-PORT-ASSIGNMENT"', 
         '_artop_constantValueMappingRef': '"CONSTANT-SPECIFICATION-MAPPING-SET"', 
         '_artop_dataTypeMappingRef': '"DATA-TYPE-MAPPING-SET"', 
         '_artop_instantiationDataDefProps': '"INSTANTIATION-DATA-DEF-PROPS"', 
         '_artop_modeSwitchEventTriggeredActivity': '"MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY"', 
         '_artop_nvBlockDataMapping': '"NV-BLOCK-DATA-MAPPING"', 
         '_artop_nvBlockNeeds': '"NV-BLOCK-NEEDS"', 
         '_artop_ramBlock': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_romBlock': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_timingEventRef': '"TIMING-EVENT"', 
         '_artop_writingStrategyRole': '"ROLE-BASED-DATA-ASSIGNMENT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def supportDirtyFlag_(self):
        if self._artop_supportDirtyFlag:
            if self._artop_supportDirtyFlag == "true":
                return True
            return False
        else:
            return self._artop_supportDirtyFlag

    @property
    def ref_nvBlockSwComponentType_(self):
        return self._artop_nvBlockSwComponentType

    @property
    def nvBlockSwComponentType_(self):
        if self._artop_nvBlockSwComponentType is not None:
            if hasattr(self._artop_nvBlockSwComponentType, "uuid"):
                return self._artop_nvBlockSwComponentType.uuid
        return

    @property
    def clientServerPorts_RoleBasedPortAssignment(self):
        return self._artop_clientServerPort

    @property
    def ref_constantValueMappings_(self):
        return self._artop_constantValueMappingRef

    @property
    def constantValueMappings_(self):
        return self._artop_constantValueMappingRef

    @property
    def ref_dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def dataTypeMappings_(self):
        return self._artop_dataTypeMappingRef

    @property
    def instantiationDataDefProps_InstantiationDataDefProps(self):
        return self._artop_instantiationDataDefProps

    @property
    def modeSwitchEventTriggeredActivities_ModeSwitchEventTriggeredActivity(self):
        return self._artop_modeSwitchEventTriggeredActivity

    @property
    def nvBlockDataMappings_NvBlockDataMapping(self):
        return self._artop_nvBlockDataMapping

    @property
    def ref_nvBlockNeeds_(self):
        return self._artop_nvBlockNeeds

    @property
    def nvBlockNeeds_(self):
        if self._artop_nvBlockNeeds is not None:
            if hasattr(self._artop_nvBlockNeeds, "uuid"):
                return self._artop_nvBlockNeeds.uuid
        return

    @property
    def ref_ramBlock_(self):
        return self._artop_ramBlock

    @property
    def ramBlock_(self):
        if self._artop_ramBlock is not None:
            if hasattr(self._artop_ramBlock, "uuid"):
                return self._artop_ramBlock.uuid
        return

    @property
    def ref_romBlock_(self):
        return self._artop_romBlock

    @property
    def romBlock_(self):
        if self._artop_romBlock is not None:
            if hasattr(self._artop_romBlock, "uuid"):
                return self._artop_romBlock.uuid
        return

    @property
    def ref_timingEvent_(self):
        return self._artop_timingEventRef

    @property
    def timingEvent_(self):
        if self._artop_timingEventRef is not None:
            if hasattr(self._artop_timingEventRef, "uuid"):
                return self._artop_timingEventRef.uuid
        return

    @property
    def ref_writingStrategyRole_(self):
        return self._artop_writingStrategyRole

    @property
    def writingStrategyRole_(self):
        if self._artop_writingStrategyRole is not None:
            if hasattr(self._artop_writingStrategyRole, "uuid"):
                return self._artop_writingStrategyRole.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
