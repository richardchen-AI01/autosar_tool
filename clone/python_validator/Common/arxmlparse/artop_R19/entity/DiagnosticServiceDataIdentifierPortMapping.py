# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticServiceDataIdentifierPortMapping.py
from .DiagnosticSwMapping import DiagnosticSwMapping

class DiagnosticServiceDataIdentifierPortMapping(DiagnosticSwMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataIdentifier import DiagnosticDataIdentifier
        from .ProcessDesign import ProcessDesign
        from .SwcServiceDependencyInExecutableInstanceRef import SwcServiceDependencyInExecutableInstanceRef
        self._artop_diagnosticDataIdentifierRef = None
        self._artop_processRef = None
        self._artop_swcServiceDependencyInExecutableIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticDataIdentifierRef':"DIAGNOSTIC-DATA-IDENTIFIER", 
         '_artop_processRef':"PROCESS-DESIGN", 
         '_artop_swcServiceDependencyInExecutableIref':"SWC-SERVICE-DEPENDENCY-IN-EXECUTABLE-INSTANCE-REF-IREF"})

    @property
    def ref_diagnosticDataIdentifier_(self):
        return self._artop_diagnosticDataIdentifierRef

    @property
    def diagnosticDataIdentifier_(self):
        if self._artop_diagnosticDataIdentifierRef is not None:
            if hasattr(self._artop_diagnosticDataIdentifierRef, "uuid"):
                return self._artop_diagnosticDataIdentifierRef.uuid
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

    @property
    def ref_swcServiceDependencyInExecutable_(self):
        return self._artop_swcServiceDependencyInExecutableIref

    @property
    def swcServiceDependencyInExecutable_(self):
        if self._artop_swcServiceDependencyInExecutableIref is not None:
            if hasattr(self._artop_swcServiceDependencyInExecutableIref, "uuid"):
                return self._artop_swcServiceDependencyInExecutableIref.uuid
        return
