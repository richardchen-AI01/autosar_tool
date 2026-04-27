# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ObdMonitorServiceNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        from .ApplicationDataType import ApplicationDataType
        from .DiagnosticEventNeeds import DiagnosticEventNeeds
        self._artop_onBoardMonitorId = None
        self._artop_testId = None
        self._artop_unitAndScalingId = None
        self._artop_updateKind = None
        self._artop_applicationDataTypeRef = None
        self._artop_eventNeedsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_applicationDataTypeRef':"APPLICATION-DATA-TYPE", 
         '_artop_eventNeedsRef':"DIAGNOSTIC-EVENT-NEEDS"})

    @property
    def onBoardMonitorId_(self):
        return self._artop_onBoardMonitorId

    @property
    def testId_(self):
        return self._artop_testId

    @property
    def unitAndScalingId_(self):
        return self._artop_unitAndScalingId

    @property
    def updateKind_(self):
        return self._artop_updateKind

    @property
    def ref_applicationDataType_(self):
        return self._artop_applicationDataTypeRef

    @property
    def applicationDataType_(self):
        if self._artop_applicationDataTypeRef is not None:
            if hasattr(self._artop_applicationDataTypeRef, "uuid"):
                return self._artop_applicationDataTypeRef.uuid
        return

    @property
    def ref_eventNeeds_(self):
        return self._artop_eventNeedsRef

    @property
    def eventNeeds_(self):
        if self._artop_eventNeedsRef is not None:
            if hasattr(self._artop_eventNeedsRef, "uuid"):
                return self._artop_eventNeedsRef.uuid
        return
