# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDynamicallyDefineDataIdentifier.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticDynamicDataIdentifier import DiagnosticDynamicDataIdentifier
        from .DiagnosticDynamicallyDefineDataIdentifierClass import DiagnosticDynamicallyDefineDataIdentifierClass
        self._artop_maxSourceElement = None
        self._artop_dataIdentifierRef = None
        self._artop_dynamicallyDefineDataIdentifierClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataIdentifierRef':"DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER", 
         '_artop_dynamicallyDefineDataIdentifierClassRef':"DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"})

    @property
    def maxSourceElement_(self):
        return self._artop_maxSourceElement

    @property
    def ref_dataIdentifier_(self):
        return self._artop_dataIdentifierRef

    @property
    def dataIdentifier_(self):
        if self._artop_dataIdentifierRef is not None:
            if hasattr(self._artop_dataIdentifierRef, "uuid"):
                return self._artop_dataIdentifierRef.uuid
        return

    @property
    def ref_dynamicallyDefineDataIdentifierClass_(self):
        return self._artop_dynamicallyDefineDataIdentifierClassRef

    @property
    def dynamicallyDefineDataIdentifierClass_(self):
        if self._artop_dynamicallyDefineDataIdentifierClassRef is not None:
            if hasattr(self._artop_dynamicallyDefineDataIdentifierClassRef, "uuid"):
                return self._artop_dynamicallyDefineDataIdentifierClassRef.uuid
        return
