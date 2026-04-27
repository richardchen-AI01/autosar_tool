# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticServiceSwMapping.py
from .DiagnosticSwMapping import DiagnosticSwMapping

class DiagnosticServiceSwMapping(DiagnosticSwMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataElement import DiagnosticDataElement
        from .BswServiceDependencyIdent import BswServiceDependencyIdent
        from .SwcServiceDependency import SwcServiceDependency
        from .SwcServiceDependencyInExecutableInstanceRef import SwcServiceDependencyInExecutableInstanceRef
        from .SwcServiceDependencyInSystemInstanceRef import SwcServiceDependencyInSystemInstanceRef
        from .SwcServiceDependencyInCompositionInstanceRef import SwcServiceDependencyInCompositionInstanceRef
        from .ProcessDesign import ProcessDesign
        from .DiagnosticServiceInstance import DiagnosticServiceInstance
        self._artop_diagnosticDataElementRef = None
        self._artop_mappedBswServiceDependencyRef = None
        self._artop_mappedFlatSwcServiceDependencyRef = None
        self._artop_mappedSwcServiceDependencyInExecutableIref = None
        self._artop_mappedSwcServiceDependencyInSystemIref = None
        self._artop_mappedSwcServiceDependencyIref = None
        self._artop_processRef = None
        self._artop_serviceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticDataElementRef': '"DIAGNOSTIC-DATA-ELEMENT"', 
         '_artop_mappedBswServiceDependencyRef': '"BSW-SERVICE-DEPENDENCY-IDENT"', 
         '_artop_mappedFlatSwcServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"', 
         '_artop_mappedSwcServiceDependencyInExecutableIref': '"SWC-SERVICE-DEPENDENCY-IN-EXECUTABLE-INSTANCE-REF-IREF"', 
         '_artop_mappedSwcServiceDependencyInSystemIref': '"SWC-SERVICE-DEPENDENCY-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_mappedSwcServiceDependencyIref': '"SWC-SERVICE-DEPENDENCY-IN-COMPOSITION-INSTANCE-REF-IREF"', 
         '_artop_processRef': '"PROCESS-DESIGN"', 
         '_artop_serviceInstanceRef': '"DIAGNOSTIC-SERVICE-INSTANCE"'})

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
    def ref_mappedBswServiceDependency_(self):
        return self._artop_mappedBswServiceDependencyRef

    @property
    def mappedBswServiceDependency_(self):
        if self._artop_mappedBswServiceDependencyRef is not None:
            if hasattr(self._artop_mappedBswServiceDependencyRef, "uuid"):
                return self._artop_mappedBswServiceDependencyRef.uuid
        return

    @property
    def ref_mappedFlatSwcServiceDependency_(self):
        return self._artop_mappedFlatSwcServiceDependencyRef

    @property
    def mappedFlatSwcServiceDependency_(self):
        if self._artop_mappedFlatSwcServiceDependencyRef is not None:
            if hasattr(self._artop_mappedFlatSwcServiceDependencyRef, "uuid"):
                return self._artop_mappedFlatSwcServiceDependencyRef.uuid
        return

    @property
    def ref_mappedSwcServiceDependencyInExecutable_(self):
        return self._artop_mappedSwcServiceDependencyInExecutableIref

    @property
    def mappedSwcServiceDependencyInExecutable_(self):
        if self._artop_mappedSwcServiceDependencyInExecutableIref is not None:
            if hasattr(self._artop_mappedSwcServiceDependencyInExecutableIref, "uuid"):
                return self._artop_mappedSwcServiceDependencyInExecutableIref.uuid
        return

    @property
    def ref_mappedSwcServiceDependencyInSystem_(self):
        return self._artop_mappedSwcServiceDependencyInSystemIref

    @property
    def mappedSwcServiceDependencyInSystem_(self):
        if self._artop_mappedSwcServiceDependencyInSystemIref is not None:
            if hasattr(self._artop_mappedSwcServiceDependencyInSystemIref, "uuid"):
                return self._artop_mappedSwcServiceDependencyInSystemIref.uuid
        return

    @property
    def ref_mappedSwcServiceDependency_(self):
        return self._artop_mappedSwcServiceDependencyIref

    @property
    def mappedSwcServiceDependency_(self):
        if self._artop_mappedSwcServiceDependencyIref is not None:
            if hasattr(self._artop_mappedSwcServiceDependencyIref, "uuid"):
                return self._artop_mappedSwcServiceDependencyIref.uuid
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
    def ref_serviceInstance_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstance_(self):
        if self._artop_serviceInstanceRef is not None:
            if hasattr(self._artop_serviceInstanceRef, "uuid"):
                return self._artop_serviceInstanceRef.uuid
        return
