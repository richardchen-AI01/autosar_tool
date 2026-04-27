# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticConnection.py
from .ARElement import ARElement

class DiagnosticConnection(ARElement):

    def __init__(self):
        super().__init__()
        from .TpConnectionIdent import TpConnectionIdent
        from .PduTriggering import PduTriggering
        self._artop_functionalRequestRef = []
        self._artop_periodicResponseUudtRef = []
        self._artop_physicalRequestRef = None
        self._artop_responseOnEventRef = None
        self._artop_responseRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_functionalRequestRef': '"TP-CONNECTION-IDENT"', 
         '_artop_periodicResponseUudtRef': '"PDU-TRIGGERING"', 
         '_artop_physicalRequestRef': '"TP-CONNECTION-IDENT"', 
         '_artop_responseOnEventRef': '"TP-CONNECTION-IDENT"', 
         '_artop_responseRef': '"TP-CONNECTION-IDENT"'})

    @property
    def ref_functionalRequests_(self):
        return self._artop_functionalRequestRef

    @property
    def functionalRequests_(self):
        return self._artop_functionalRequestRef

    @property
    def ref_periodicResponseUudts_(self):
        return self._artop_periodicResponseUudtRef

    @property
    def periodicResponseUudts_(self):
        return self._artop_periodicResponseUudtRef

    @property
    def ref_physicalRequest_(self):
        return self._artop_physicalRequestRef

    @property
    def physicalRequest_(self):
        if self._artop_physicalRequestRef is not None:
            if hasattr(self._artop_physicalRequestRef, "uuid"):
                return self._artop_physicalRequestRef.uuid
        return

    @property
    def ref_responseOnEvent_(self):
        return self._artop_responseOnEventRef

    @property
    def responseOnEvent_(self):
        if self._artop_responseOnEventRef is not None:
            if hasattr(self._artop_responseOnEventRef, "uuid"):
                return self._artop_responseOnEventRef.uuid
        return

    @property
    def ref_response_(self):
        return self._artop_responseRef

    @property
    def response_(self):
        if self._artop_responseRef is not None:
            if hasattr(self._artop_responseRef, "uuid"):
                return self._artop_responseRef.uuid
        return
