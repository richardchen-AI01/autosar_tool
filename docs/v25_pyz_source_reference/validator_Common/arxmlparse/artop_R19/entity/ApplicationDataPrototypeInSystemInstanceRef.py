# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationDataPrototypeInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ApplicationDataPrototypeInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DataPrototypeWithApplicationDataTypeInSystemRef import DataPrototypeWithApplicationDataTypeInSystemRef
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_dataPrototypeWithApplicationDataTypeInSystemRef = None
        self._artop_system = None
        self._artop_contextCompositionRef = None
        self._artop_contextComponentRef = []
        self._artop_contextPortRef = None
        self._artop_rootDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataPrototypeWithApplicationDataTypeInSystemRef': '"DATA-PROTOTYPE-WITH-APPLICATION-DATA-TYPE-IN-SYSTEM-REF"', 
         '_artop_system': '"SYSTEM"', 
         '_artop_contextCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortRef': '"PORT-PROTOTYPE"', 
         '_artop_rootDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_dataPrototypeWithApplicationDataTypeInSystemRef_(self):
        return self._artop_dataPrototypeWithApplicationDataTypeInSystemRef

    @property
    def dataPrototypeWithApplicationDataTypeInSystemRef_(self):
        if self._artop_dataPrototypeWithApplicationDataTypeInSystemRef is not None:
            if hasattr(self._artop_dataPrototypeWithApplicationDataTypeInSystemRef, "uuid"):
                return self._artop_dataPrototypeWithApplicationDataTypeInSystemRef.uuid
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
    def ref_contextComposition_(self):
        return self._artop_contextCompositionRef

    @property
    def contextComposition_(self):
        if self._artop_contextCompositionRef is not None:
            if hasattr(self._artop_contextCompositionRef, "uuid"):
                return self._artop_contextCompositionRef.uuid
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
    def ref_rootDataPrototype_(self):
        return self._artop_rootDataPrototypeRef

    @property
    def rootDataPrototype_(self):
        if self._artop_rootDataPrototypeRef is not None:
            if hasattr(self._artop_rootDataPrototypeRef, "uuid"):
                return self._artop_rootDataPrototypeRef.uuid
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
