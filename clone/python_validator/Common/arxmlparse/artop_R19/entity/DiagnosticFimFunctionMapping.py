# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFimFunctionMapping.py
from .DiagnosticSwMapping import DiagnosticSwMapping

class DiagnosticFimFunctionMapping(DiagnosticSwMapping):

    def __init__(self):
        super().__init__()
        from .BswServiceDependencyIdent import BswServiceDependencyIdent
        from .SwcServiceDependency import SwcServiceDependency
        from .DiagnosticFunctionIdentifier import DiagnosticFunctionIdentifier
        from .SwcServiceDependencyInSystemInstanceRef import SwcServiceDependencyInSystemInstanceRef
        self._artop_mappedBswServiceDependencyRef = None
        self._artop_mappedFlatSwcServiceDependencyRef = None
        self._artop_mappedFunctionRef = None
        self._artop_mappedSwcServiceDependencyIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_mappedBswServiceDependencyRef': '"BSW-SERVICE-DEPENDENCY-IDENT"', 
         '_artop_mappedFlatSwcServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"', 
         '_artop_mappedFunctionRef': '"DIAGNOSTIC-FUNCTION-IDENTIFIER"', 
         '_artop_mappedSwcServiceDependencyIref': '"SWC-SERVICE-DEPENDENCY-IN-SYSTEM-INSTANCE-REF-IREF"'})

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
    def ref_mappedFunction_(self):
        return self._artop_mappedFunctionRef

    @property
    def mappedFunction_(self):
        if self._artop_mappedFunctionRef is not None:
            if hasattr(self._artop_mappedFunctionRef, "uuid"):
                return self._artop_mappedFunctionRef.uuid
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
