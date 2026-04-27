# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class DataPrototypeInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DiagnosticServiceDataMapping import DiagnosticServiceDataMapping
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_diagnosticServiceDataMapping = None
        self._artop_system = None
        self._artop_contextRootCompositionRef = None
        self._artop_contextComponentRef = []
        self._artop_contextPortRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticServiceDataMapping': '"DIAGNOSTIC-SERVICE-DATA-MAPPING"', 
         '_artop_system': '"SYSTEM"', 
         '_artop_contextRootCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
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
        return self._artop_system

    @property
    def base_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_contextRootComposition_(self):
        return self._artop_contextRootCompositionRef

    @property
    def contextRootComposition_(self):
        if self._artop_contextRootCompositionRef is not None:
            if hasattr(self._artop_contextRootCompositionRef, "uuid"):
                return self._artop_contextRootCompositionRef.uuid
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
