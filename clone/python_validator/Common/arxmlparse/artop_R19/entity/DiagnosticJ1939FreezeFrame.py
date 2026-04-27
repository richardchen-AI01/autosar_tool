# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticJ1939FreezeFrame.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticJ1939FreezeFrame(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticJ1939Node import DiagnosticJ1939Node
        from .DiagnosticJ1939Spn import DiagnosticJ1939Spn
        self._artop_nodeRef = None
        self._artop_spnRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nodeRef':"DIAGNOSTIC-J-1939-NODE", 
         '_artop_spnRef':"DIAGNOSTIC-J-1939-SPN"})

    @property
    def ref_node_(self):
        return self._artop_nodeRef

    @property
    def node_(self):
        if self._artop_nodeRef is not None:
            if hasattr(self._artop_nodeRef, "uuid"):
                return self._artop_nodeRef.uuid
        return

    @property
    def ref_spns_(self):
        return self._artop_spnRef

    @property
    def spns_(self):
        return self._artop_spnRef
