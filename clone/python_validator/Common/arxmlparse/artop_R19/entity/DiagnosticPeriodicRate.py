# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticPeriodicRate.py
from .ARObject import ARObject

class DiagnosticPeriodicRate(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticReadDataByPeriodicIDClass import DiagnosticReadDataByPeriodicIDClass
        self._artop_period = None
        self._artop_periodicRateCategory = None
        self._artop_diagnosticReadDataByPeriodicIdClass = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticReadDataByPeriodicIdClass": "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"})

    @property
    def period_(self):
        return self._artop_period

    @property
    def periodicRateCategory_(self):
        return self._artop_periodicRateCategory

    @property
    def ref_diagnosticReadDataByPeriodicIDClass_(self):
        return self._artop_diagnosticReadDataByPeriodicIdClass

    @property
    def diagnosticReadDataByPeriodicIDClass_(self):
        if self._artop_diagnosticReadDataByPeriodicIdClass is not None:
            if hasattr(self._artop_diagnosticReadDataByPeriodicIdClass, "uuid"):
                return self._artop_diagnosticReadDataByPeriodicIdClass.uuid
        return
