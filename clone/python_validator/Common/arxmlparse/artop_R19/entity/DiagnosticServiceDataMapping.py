# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticServiceDataMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticServiceDataMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataElement import DiagnosticDataElement
        from .DataPrototypeInExecutableInstanceRef import DataPrototypeInExecutableInstanceRef
        from .DataPrototypeInSystemInstanceRef import DataPrototypeInSystemInstanceRef
        from .ProcessDesign import ProcessDesign
        self._artop_diagnosticDataElementRef = None
        self._artop_mappedApDataElementIref = None
        self._artop_mappedDataElementIref = None
        self._artop_processRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticDataElementRef': '"DIAGNOSTIC-DATA-ELEMENT"', 
         '_artop_mappedApDataElementIref': '"DATA-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF-IREF"', 
         '_artop_mappedDataElementIref': '"DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_processRef': '"PROCESS-DESIGN"'})

    @property
    def ref_diagnosticDataElement_(self):
        return self._artop_diagnosticDataElementRef

    @property
    def diagnosticDataElement_(self):
        if self._artop_diagnosticDataElementRef is not None:
            if hasattr(self._artop_diagnosticDataElementRef, "uuid"):
                return self._artop_diagnosticDataElementRef.uuid
        return

    @property
    def ref_mappedApDataElement_(self):
        return self._artop_mappedApDataElementIref

    @property
    def mappedApDataElement_(self):
        if self._artop_mappedApDataElementIref is not None:
            if hasattr(self._artop_mappedApDataElementIref, "uuid"):
                return self._artop_mappedApDataElementIref.uuid
        return

    @property
    def ref_mappedDataElement_(self):
        return self._artop_mappedDataElementIref

    @property
    def mappedDataElement_(self):
        if self._artop_mappedDataElementIref is not None:
            if hasattr(self._artop_mappedDataElementIref, "uuid"):
                return self._artop_mappedDataElementIref.uuid
        return

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return
