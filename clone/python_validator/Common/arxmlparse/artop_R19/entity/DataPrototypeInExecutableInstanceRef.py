# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInExecutableInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class DataPrototypeInExecutableInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DiagnosticServiceDataMapping import DiagnosticServiceDataMapping
        from .Executable import Executable
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_diagnosticServiceDataMapping = None
        self._artop_executable = None
        self._artop_contextRootComponentRef = None
        self._artop_contextComponentRef = []
        self._artop_contextPortRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticServiceDataMapping': '"DIAGNOSTIC-SERVICE-DATA-MAPPING"', 
         '_artop_executable': '"EXECUTABLE"', 
         '_artop_contextRootComponentRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortRef': '"PORT-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_diagnosticServiceDataMapping_(self):
        return self._artop_diagnosticServiceDataMapping

    @property
    def diagnosticServiceDataMapping_(self):
        if self._artop_diagnosticServiceDataMapping is not None:
            if hasattr(self._artop_diagnosticServiceDataMapping, "uuid"):
                return self._artop_diagnosticServiceDataMapping.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_executable

    @property
    def base_(self):
        if self._artop_executable is not None:
            if hasattr(self._artop_executable, "uuid"):
                return self._artop_executable.uuid
        return

    @property
    def ref_contextRootComponent_(self):
        return self._artop_contextRootComponentRef

    @property
    def contextRootComponent_(self):
        if self._artop_contextRootComponentRef is not None:
            if hasattr(self._artop_contextRootComponentRef, "uuid"):
                return self._artop_contextRootComponentRef.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def ref_contextPort_(self):
        return self._artop_contextPortRef

    @property
    def contextPort_(self):
        if self._artop_contextPortRef is not None:
            if hasattr(self._artop_contextPortRef, "uuid"):
                return self._artop_contextPortRef.uuid
        return

    @property
    def ref_contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def ref_targetDataPrototype_(self):
        return self._artop_targetDataPrototypeRef

    @property
    def targetDataPrototype_(self):
        if self._artop_targetDataPrototypeRef is not None:
            if hasattr(self._artop_targetDataPrototypeRef, "uuid"):
                return self._artop_targetDataPrototypeRef.uuid
        return
