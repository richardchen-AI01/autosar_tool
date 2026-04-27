# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInstanceToSignalMapping.py
from .Identifiable import Identifiable

class ServiceInstanceToSignalMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ServiceInstanceToSignalMappingSet import ServiceInstanceToSignalMappingSet
        from .SignalBasedEventElementToISignalTriggeringMapping import SignalBasedEventElementToISignalTriggeringMapping
        from .SignalBasedFieldToISignalTriggeringMapping import SignalBasedFieldToISignalTriggeringMapping
        from .SignalBasedMethodToISignalTriggeringMapping import SignalBasedMethodToISignalTriggeringMapping
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        self._artop_serviceInstanceToSignalMappingSet = None
        self._artop_eventElementMapping = []
        self._artop_fieldMapping = []
        self._artop_methodMapping = None
        self._artop_serviceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_serviceInstanceToSignalMappingSet': '"SERVICE-INSTANCE-TO-SIGNAL-MAPPING-SET"', 
         '_artop_eventElementMapping': '"SIGNAL-BASED-EVENT-ELEMENT-TO-I-SIGNAL-TRIGGERING-MAPPING"', 
         '_artop_fieldMapping': '"SIGNAL-BASED-FIELD-TO-I-SIGNAL-TRIGGERING-MAPPING"', 
         '_artop_methodMapping': '"SIGNAL-BASED-METHOD-TO-I-SIGNAL-TRIGGERING-MAPPING"', 
         '_artop_serviceInstanceRef': '"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"'})

    @property
    def ref_serviceInstanceToSignalMappingSet_(self):
        return self._artop_serviceInstanceToSignalMappingSet

    @property
    def serviceInstanceToSignalMappingSet_(self):
        if self._artop_serviceInstanceToSignalMappingSet is not None:
            if hasattr(self._artop_serviceInstanceToSignalMappingSet, "uuid"):
                return self._artop_serviceInstanceToSignalMappingSet.uuid
        return

    @property
    def eventElementMappings_SignalBasedEventElementToISignalTriggeringMapping(self):
        return self._artop_eventElementMapping

    @property
    def fieldMappings_SignalBasedFieldToISignalTriggeringMapping(self):
        return self._artop_fieldMapping

    @property
    def ref_methodMapping_(self):
        return self._artop_methodMapping

    @property
    def methodMapping_(self):
        if self._artop_methodMapping is not None:
            if hasattr(self._artop_methodMapping, "uuid"):
                return self._artop_methodMapping.uuid
        return

    @property
    def ref_serviceInstance_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstance_(self):
        if self._artop_serviceInstanceRef is not None:
            if hasattr(self._artop_serviceInstanceRef, "uuid"):
                return self._artop_serviceInstanceRef.uuid
        return
