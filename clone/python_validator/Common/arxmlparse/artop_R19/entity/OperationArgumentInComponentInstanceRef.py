# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\OperationArgumentInComponentInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class OperationArgumentInComponentInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AutosarOperationArgumentInstance import AutosarOperationArgumentInstance
        from .SwComponentType import SwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .ClientServerOperation import ClientServerOperation
        from .ArgumentDataPrototype import ArgumentDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_autosarOperationArgumentInstance = None
        self._artop_swComponentType = None
        self._artop_contextComponentRef = []
        self._artop_contextPortPrototypeRef = None
        self._artop_contextOperationRef = None
        self._artop_rootArgumentDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_autosarOperationArgumentInstance': '"AUTOSAR-OPERATION-ARGUMENT-INSTANCE"', 
         '_artop_swComponentType': '"SW-COMPONENT-TYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_contextOperationRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_rootArgumentDataPrototypeRef': '"ARGUMENT-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_autosarOperationArgumentInstance_(self):
        return self._artop_autosarOperationArgumentInstance

    @property
    def autosarOperationArgumentInstance_(self):
        if self._artop_autosarOperationArgumentInstance is not None:
            if hasattr(self._artop_autosarOperationArgumentInstance, "uuid"):
                return self._artop_autosarOperationArgumentInstance.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_swComponentType

    @property
    def base_(self):
        if self._artop_swComponentType is not None:
            if hasattr(self._artop_swComponentType, "uuid"):
                return self._artop_swComponentType.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

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
    def ref_contextOperation_(self):
        return self._artop_contextOperationRef

    @property
    def contextOperation_(self):
        if self._artop_contextOperationRef is not None:
            if hasattr(self._artop_contextOperationRef, "uuid"):
                return self._artop_contextOperationRef.uuid
        return

    @property
    def ref_rootArgumentDataPrototype_(self):
        return self._artop_rootArgumentDataPrototypeRef

    @property
    def rootArgumentDataPrototype_(self):
        if self._artop_rootArgumentDataPrototypeRef is not None:
            if hasattr(self._artop_rootArgumentDataPrototypeRef, "uuid"):
                return self._artop_rootArgumentDataPrototypeRef.uuid
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
