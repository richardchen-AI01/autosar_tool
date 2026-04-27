# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticReadDataByPeriodicID.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticAbstractDataIdentifier import DiagnosticAbstractDataIdentifier
        from .DiagnosticReadDataByPeriodicIDClass import DiagnosticReadDataByPeriodicIDClass
        self._artop_dataIdentifierRef = None
        self._artop_readDataClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataIdentifierRef':"DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER", 
         '_artop_readDataClassRef':"DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"})

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
    def ref_readDataClass_(self):
        return self._artop_readDataClassRef

    @property
    def readDataClass_(self):
        if self._artop_readDataClassRef is not None:
            if hasattr(self._artop_readDataClassRef, "uuid"):
                return self._artop_readDataClassRef.uuid
        return
