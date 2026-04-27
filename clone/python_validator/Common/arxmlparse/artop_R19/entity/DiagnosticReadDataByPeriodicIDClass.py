# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticReadDataByPeriodicIDClass.py
from .DiagnosticServiceClass import DiagnosticServiceClass

class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):

    def __init__(self):
        super().__init__()
        from .DiagnosticPeriodicRate import DiagnosticPeriodicRate
        self._artop_maxPeriodicDidToRead = None
        self._artop_schedulerMaxNumber = None
        self._artop_periodicRate = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_periodicRate": "DIAGNOSTIC-PERIODIC-RATE"})

    @property
    def maxPeriodicDidToRead_(self):
        return self._artop_maxPeriodicDidToRead

    @property
    def schedulerMaxNumber_(self):
        return self._artop_schedulerMaxNumber

    @property
    def periodicRates_DiagnosticPeriodicRate(self):
        return self._artop_periodicRate
