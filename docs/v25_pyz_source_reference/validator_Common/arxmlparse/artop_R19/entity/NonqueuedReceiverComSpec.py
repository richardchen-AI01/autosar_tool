# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NonqueuedReceiverComSpec.py
from .ReceiverComSpec import ReceiverComSpec

class NonqueuedReceiverComSpec(ReceiverComSpec):

    def __init__(self):
        super().__init__()
        from .DataFilter import DataFilter
        from .ValueSpecification import ValueSpecification
        self._artop_aliveTimeout = None
        self._artop_enableUpdate = None
        self._artop_handleDataStatus = None
        self._artop_handleNeverReceived = None
        self._artop_handleTimeoutType = None
        self._artop_filter = None
        self._artop_initValue = None
        self._artop_timeoutSubstitutionValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_filter':"DATA-FILTER", 
         '_artop_initValue':"VALUE-SPECIFICATION", 
         '_artop_timeoutSubstitutionValue':"VALUE-SPECIFICATION"})

    @property
    def aliveTimeout_(self):
        return self._artop_aliveTimeout

    @property
    def enableUpdate_(self):
        if self._artop_enableUpdate:
            if self._artop_enableUpdate == "true":
                return True
            return False
        else:
            return self._artop_enableUpdate

    @property
    def handleDataStatus_(self):
        if self._artop_handleDataStatus:
            if self._artop_handleDataStatus == "true":
                return True
            return False
        else:
            return self._artop_handleDataStatus

    @property
    def handleNeverReceived_(self):
        if self._artop_handleNeverReceived:
            if self._artop_handleNeverReceived == "true":
                return True
            return False
        else:
            return self._artop_handleNeverReceived

    @property
    def handleTimeoutType_(self):
        return self._artop_handleTimeoutType

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
    def ref_initValue_(self):
        return self._artop_initValue

    @property
    def initValue_(self):
        if self._artop_initValue is not None:
            if hasattr(self._artop_initValue, "uuid"):
                return self._artop_initValue.uuid
        return

    @property
    def ref_timeoutSubstitutionValue_(self):
        return self._artop_timeoutSubstitutionValue

    @property
    def timeoutSubstitutionValue_(self):
        if self._artop_timeoutSubstitutionValue is not None:
            if hasattr(self._artop_timeoutSubstitutionValue, "uuid"):
                return self._artop_timeoutSubstitutionValue.uuid
        return
