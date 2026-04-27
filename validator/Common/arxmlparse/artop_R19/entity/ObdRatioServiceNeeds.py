# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ObdRatioServiceNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class ObdRatioServiceNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticEventNeeds import DiagnosticEventNeeds
        from .FunctionInhibitionNeeds import FunctionInhibitionNeeds
        self._artop_connectionType = None
        self._artop_denominatorGroup = None
        self._artop_iumprGroup = None
        self._artop_rateBasedMonitoredEventRef = None
        self._artop_usedFidRef = None
        self._artop_usedSecondaryFidRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_rateBasedMonitoredEventRef':"DIAGNOSTIC-EVENT-NEEDS", 
         '_artop_usedFidRef':"FUNCTION-INHIBITION-NEEDS", 
         '_artop_usedSecondaryFidRef':"FUNCTION-INHIBITION-NEEDS"})

    @property
    def connectionType_(self):
        return self._artop_connectionType

    @property
    def denominatorGroup_(self):
        return self._artop_denominatorGroup

    @property
    def iumprGroup_(self):
        return self._artop_iumprGroup

    @property
    def ref_rateBasedMonitoredEvent_(self):
        return self._artop_rateBasedMonitoredEventRef

    @property
    def rateBasedMonitoredEvent_(self):
        if self._artop_rateBasedMonitoredEventRef is not None:
            if hasattr(self._artop_rateBasedMonitoredEventRef, "uuid"):
                return self._artop_rateBasedMonitoredEventRef.uuid
        return

    @property
    def ref_usedFid_(self):
        return self._artop_usedFidRef

    @property
    def usedFid_(self):
        if self._artop_usedFidRef is not None:
            if hasattr(self._artop_usedFidRef, "uuid"):
                return self._artop_usedFidRef.uuid
        return

    @property
    def ref_usedSecondaryFids_(self):
        return self._artop_usedSecondaryFidRef

    @property
    def usedSecondaryFids_(self):
        return self._artop_usedSecondaryFidRef
