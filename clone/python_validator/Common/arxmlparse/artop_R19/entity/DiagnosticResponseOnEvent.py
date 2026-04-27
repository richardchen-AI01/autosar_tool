# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticResponseOnEvent.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticResponseOnEvent(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticResponseOnEventTrigger import DiagnosticResponseOnEventTrigger
        from .DiagnosticEventWindow import DiagnosticEventWindow
        from .DiagnosticResponseOnEventClass import DiagnosticResponseOnEventClass
        self._artop_responseOnEventAction = None
        self._artop_storeEventSupport = None
        self._artop_event = []
        self._artop_eventWindow = []
        self._artop_responseOnEventClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_event':"DIAGNOSTIC-RESPONSE-ON-EVENT-TRIGGER", 
         '_artop_eventWindow':"DIAGNOSTIC-EVENT-WINDOW", 
         '_artop_responseOnEventClassRef':"DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"})

    @property
    def responseOnEventAction_(self):
        return self._artop_responseOnEventAction

    @property
    def storeEventSupport_(self):
        return self._artop_storeEventSupport

    @property
    def events_DiagnosticResponseOnEventTrigger(self):
        return self._artop_event

    @property
    def eventWindows_DiagnosticEventWindow(self):
        return self._artop_eventWindow

    @property
    def ref_responseOnEventClass_(self):
        return self._artop_responseOnEventClassRef

    @property
    def responseOnEventClass_(self):
        if self._artop_responseOnEventClassRef is not None:
            if hasattr(self._artop_responseOnEventClassRef, "uuid"):
                return self._artop_responseOnEventClassRef.uuid
        return
