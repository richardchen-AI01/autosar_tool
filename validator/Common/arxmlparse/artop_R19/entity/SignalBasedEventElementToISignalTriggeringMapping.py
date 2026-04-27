# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SignalBasedEventElementToISignalTriggeringMapping.py
from .AbstractSignalBasedToISignalTriggeringMapping import AbstractSignalBasedToISignalTriggeringMapping

class SignalBasedEventElementToISignalTriggeringMapping(AbstractSignalBasedToISignalTriggeringMapping):

    def __init__(self):
        super().__init__()
        from .ServiceInstanceToSignalMapping import ServiceInstanceToSignalMapping
        from .DataPrototypeInServiceInterfaceRef import DataPrototypeInServiceInterfaceRef
        from .DataFilter import DataFilter
        from .ISignalTriggering import ISignalTriggering
        self._artop_transmissionTrigger = None
        self._artop_serviceInstanceToSignalMapping = None
        self._artop_dataPrototypeInServiceInterfaceRef = None
        self._artop_filter = None
        self._artop_iSignalTriggeringRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_serviceInstanceToSignalMapping': '"SERVICE-INSTANCE-TO-SIGNAL-MAPPING"', 
         '_artop_dataPrototypeInServiceInterfaceRef': '"DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF"', 
         '_artop_filter': '"DATA-FILTER"', 
         '_artop_iSignalTriggeringRef': '"I-SIGNAL-TRIGGERING"'})

    @property
    def transmissionTrigger_(self):
        if self._artop_transmissionTrigger:
            if self._artop_transmissionTrigger == "true":
                return True
            return False
        else:
            return self._artop_transmissionTrigger

    @property
    def ref_serviceInstanceToSignalMapping_(self):
        return self._artop_serviceInstanceToSignalMapping

    @property
    def serviceInstanceToSignalMapping_(self):
        if self._artop_serviceInstanceToSignalMapping is not None:
            if hasattr(self._artop_serviceInstanceToSignalMapping, "uuid"):
                return self._artop_serviceInstanceToSignalMapping.uuid
        return

    @property
    def ref_dataPrototypeInServiceInterfaceRef_(self):
        return self._artop_dataPrototypeInServiceInterfaceRef

    @property
    def dataPrototypeInServiceInterfaceRef_(self):
        if self._artop_dataPrototypeInServiceInterfaceRef is not None:
            if hasattr(self._artop_dataPrototypeInServiceInterfaceRef, "uuid"):
                return self._artop_dataPrototypeInServiceInterfaceRef.uuid
        return

    @property
    def ref_filter_(self):
        return self._artop_filter

    @property
    def filter_(self):
        if self._artop_filter is not None:
            if hasattr(self._artop_filter, "uuid"):
                return self._artop_filter.uuid
        return

    @property
    def ref_iSignalTriggering_(self):
        return self._artop_iSignalTriggeringRef

    @property
    def iSignalTriggering_(self):
        if self._artop_iSignalTriggeringRef is not None:
            if hasattr(self._artop_iSignalTriggeringRef, "uuid"):
                return self._artop_iSignalTriggeringRef.uuid
        return
