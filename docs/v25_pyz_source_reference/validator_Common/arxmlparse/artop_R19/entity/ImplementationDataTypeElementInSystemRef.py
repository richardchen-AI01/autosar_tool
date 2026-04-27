# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ImplementationDataTypeElementInSystemRef.py
from .DataPrototypeInSystemRef import DataPrototypeInSystemRef

class ImplementationDataTypeElementInSystemRef(DataPrototypeInSystemRef):

    def __init__(self):
        super().__init__()
        from .System import System
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        self._artop_baseRef = None
        self._artop_contextSwcPrototypeRef = []
        self._artop_contextPortPrototypeRef = None
        self._artop_rootDataPrototypeRef = None
        self._artop_contextImplementationDataElementRef = []
        self._artop_targetImplementationDataTypeElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_baseRef': '"SYSTEM"', 
         '_artop_contextSwcPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_rootDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_contextImplementationDataElementRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_targetImplementationDataTypeElementRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"'})

    @property
    def ref_base_(self):
        return self._artop_baseRef

    @property
    def base_(self):
        if self._artop_baseRef is not None:
            if hasattr(self._artop_baseRef, "uuid"):
                return self._artop_baseRef.uuid
        return

    @property
    def ref_contextSwcPrototypes_(self):
        return self._artop_contextSwcPrototypeRef

    @property
    def contextSwcPrototypes_(self):
        return self._artop_contextSwcPrototypeRef

    @property
    def ref_contextPortPrototype_(self):
        return self._artop_contextPortPrototypeRef

    @property
    def contextPortPrototype_(self):
        if self._artop_contextPortPrototypeRef is not None:
            if hasattr(self._artop_contextPortPrototypeRef, "uuid"):
                return self._artop_contextPortPrototypeRef.uuid
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
    def ref_contextImplementationDataElements_(self):
        return self._artop_contextImplementationDataElementRef

    @property
    def contextImplementationDataElements_(self):
        return self._artop_contextImplementationDataElementRef

    @property
    def ref_targetImplementationDataTypeElement_(self):
        return self._artop_targetImplementationDataTypeElementRef

    @property
    def targetImplementationDataTypeElement_(self):
        if self._artop_targetImplementationDataTypeElementRef is not None:
            if hasattr(self._artop_targetImplementationDataTypeElementRef, "uuid"):
                return self._artop_targetImplementationDataTypeElementRef.uuid
        return
