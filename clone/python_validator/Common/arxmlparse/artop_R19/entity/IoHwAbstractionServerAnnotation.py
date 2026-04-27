# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IoHwAbstractionServerAnnotation.py
from .GeneralAnnotation import GeneralAnnotation

class IoHwAbstractionServerAnnotation(GeneralAnnotation):

    def __init__(self):
        super().__init__()
        from .PortPrototype import PortPrototype
        from .MultidimensionalTime import MultidimensionalTime
        from .ArgumentDataPrototype import ArgumentDataPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .Trigger import Trigger
        self._artop_bswResolution = None
        self._artop_filteringDebouncing = None
        self._artop_pulseTest = None
        self._artop_portPrototype = None
        self._artop_age = None
        self._artop_argumentRef = None
        self._artop_dataElementRef = None
        self._artop_failureMonitoringRef = None
        self._artop_triggerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_portPrototype': '"PORT-PROTOTYPE"', 
         '_artop_age': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_argumentRef': '"ARGUMENT-DATA-PROTOTYPE"', 
         '_artop_dataElementRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_failureMonitoringRef': '"PORT-PROTOTYPE"', 
         '_artop_triggerRef': '"TRIGGER"'})

    @property
    def bswResolution_(self):
        if self._artop_bswResolution:
            return float(self._artop_bswResolution)
        return self._artop_bswResolution

    @property
    def filteringDebouncing_(self):
        return self._artop_filteringDebouncing

    @property
    def pulseTest_(self):
        return self._artop_pulseTest

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototype

    @property
    def portPrototype_(self):
        if self._artop_portPrototype is not None:
            if hasattr(self._artop_portPrototype, "uuid"):
                return self._artop_portPrototype.uuid
        return

    @property
    def ref_age_(self):
        return self._artop_age

    @property
    def age_(self):
        if self._artop_age is not None:
            if hasattr(self._artop_age, "uuid"):
                return self._artop_age.uuid
        return

    @property
    def ref_argument_(self):
        return self._artop_argumentRef

    @property
    def argument_(self):
        if self._artop_argumentRef is not None:
            if hasattr(self._artop_argumentRef, "uuid"):
                return self._artop_argumentRef.uuid
        return

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return

    @property
    def ref_failureMonitoring_(self):
        return self._artop_failureMonitoringRef

    @property
    def failureMonitoring_(self):
        if self._artop_failureMonitoringRef is not None:
            if hasattr(self._artop_failureMonitoringRef, "uuid"):
                return self._artop_failureMonitoringRef.uuid
        return

    @property
    def ref_trigger_(self):
        return self._artop_triggerRef

    @property
    def trigger_(self):
        if self._artop_triggerRef is not None:
            if hasattr(self._artop_triggerRef, "uuid"):
                return self._artop_triggerRef.uuid
        return
