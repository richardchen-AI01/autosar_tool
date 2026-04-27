# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeJ1939.py
from .DiagnosticTroubleCode import DiagnosticTroubleCode

class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeProps import DiagnosticTroubleCodeProps
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .DiagnosticJ1939Node import DiagnosticJ1939Node
        from .DiagnosticJ1939Spn import DiagnosticJ1939Spn
        self._artop_fmi = None
        self._artop_kind = None
        self._artop_dtcPropsRef = None
        self._artop_j1939DtcValue = None
        self._artop_nodeRef = None
        self._artop_spnRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dtcPropsRef': '"DIAGNOSTIC-TROUBLE-CODE-PROPS"', 
         '_artop_j1939DtcValue': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_nodeRef': '"DIAGNOSTIC-J-1939-NODE"', 
         '_artop_spnRef': '"DIAGNOSTIC-J-1939-SPN"'})

    @property
    def fmi_(self):
        return self._artop_fmi

    @property
    def kind_(self):
        return self._artop_kind

    @property
    def ref_dtcProps_(self):
        return self._artop_dtcPropsRef

    @property
    def dtcProps_(self):
        if self._artop_dtcPropsRef is not None:
            if hasattr(self._artop_dtcPropsRef, "uuid"):
                return self._artop_dtcPropsRef.uuid
        return

    @property
    def ref_j1939DtcValue_(self):
        return self._artop_j1939DtcValue

    @property
    def j1939DtcValue_(self):
        if self._artop_j1939DtcValue is not None:
            if hasattr(self._artop_j1939DtcValue, "uuid"):
                return self._artop_j1939DtcValue.uuid
        return

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
    def ref_spn_(self):
        return self._artop_spnRef

    @property
    def spn_(self):
        if self._artop_spnRef is not None:
            if hasattr(self._artop_spnRef, "uuid"):
                return self._artop_spnRef.uuid
        return
