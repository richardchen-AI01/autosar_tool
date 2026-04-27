# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnableConditionPortMapping.py
from .DiagnosticSwMapping import DiagnosticSwMapping

class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnableCondition import DiagnosticEnableCondition
        from .ProcessDesign import ProcessDesign
        from .SwcServiceDependency import SwcServiceDependency
        from .SwcServiceDependencyInExecutableInstanceRef import SwcServiceDependencyInExecutableInstanceRef
        from .SwcServiceDependencyInSystemInstanceRef import SwcServiceDependencyInSystemInstanceRef
        from .SwcServiceDependencyInCompositionInstanceRef import SwcServiceDependencyInCompositionInstanceRef
        self._artop_enableConditionRef = None
        self._artop_processRef = None
        self._artop_swcFlatServiceDependencyRef = None
        self._artop_swcServiceDependencyInExecutableIref = None
        self._artop_swcServiceDependencyInSystemIref = None
        self._artop_swcServiceDependencyIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_enableConditionRef': '"DIAGNOSTIC-ENABLE-CONDITION"', 
         '_artop_processRef': '"PROCESS-DESIGN"', 
         '_artop_swcFlatServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"', 
         '_artop_swcServiceDependencyInExecutableIref': '"SWC-SERVICE-DEPENDENCY-IN-EXECUTABLE-INSTANCE-REF-IREF"', 
         '_artop_swcServiceDependencyInSystemIref': '"SWC-SERVICE-DEPENDENCY-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_swcServiceDependencyIref': '"SWC-SERVICE-DEPENDENCY-IN-COMPOSITION-INSTANCE-REF-IREF"'})

    @property
    def ref_enableCondition_(self):
        return self._artop_enableConditionRef

    @property
    def enableCondition_(self):
        if self._artop_enableConditionRef is not None:
            if hasattr(self._artop_enableConditionRef, "uuid"):
                return self._artop_enableConditionRef.uuid
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
    def ref_swcFlatServiceDependency_(self):
        return self._artop_swcFlatServiceDependencyRef

    @property
    def swcFlatServiceDependency_(self):
        if self._artop_swcFlatServiceDependencyRef is not None:
            if hasattr(self._artop_swcFlatServiceDependencyRef, "uuid"):
                return self._artop_swcFlatServiceDependencyRef.uuid
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

    @property
    def ref_swcServiceDependencyInSystem_(self):
        return self._artop_swcServiceDependencyInSystemIref

    @property
    def swcServiceDependencyInSystem_(self):
        if self._artop_swcServiceDependencyInSystemIref is not None:
            if hasattr(self._artop_swcServiceDependencyInSystemIref, "uuid"):
                return self._artop_swcServiceDependencyInSystemIref.uuid
        return

    @property
    def ref_swcServiceDependency_(self):
        return self._artop_swcServiceDependencyIref

    @property
    def swcServiceDependency_(self):
        if self._artop_swcServiceDependencyIref is not None:
            if hasattr(self._artop_swcServiceDependencyIref, "uuid"):
                return self._artop_swcServiceDependencyIref.uuid
        return
