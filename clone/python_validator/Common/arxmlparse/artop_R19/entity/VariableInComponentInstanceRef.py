# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariableInComponentInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class VariableInComponentInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AutosarVariableInstance import AutosarVariableInstance
        from .SwComponentType import SwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_autosarVariableInstance = None
        self._artop_swComponentType = None
        self._artop_contextComponentRef = []
        self._artop_contextPortPrototypeRef = None
        self._artop_rootVariableDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataProtoypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_autosarVariableInstance': '"AUTOSAR-VARIABLE-INSTANCE"', 
         '_artop_swComponentType': '"SW-COMPONENT-TYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_rootVariableDataPrototypeRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataProtoypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_autosarVariableInstance_(self):
        return self._artop_autosarVariableInstance

    @property
    def autosarVariableInstance_(self):
        if self._artop_autosarVariableInstance is not None:
            if hasattr(self._artop_autosarVariableInstance, "uuid"):
                return self._artop_autosarVariableInstance.uuid
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
    def ref_rootVariableDataPrototype_(self):
        return self._artop_rootVariableDataPrototypeRef

    @property
    def rootVariableDataPrototype_(self):
        if self._artop_rootVariableDataPrototypeRef is not None:
            if hasattr(self._artop_rootVariableDataPrototypeRef, "uuid"):
                return self._artop_rootVariableDataPrototypeRef.uuid
        return

    @property
    def ref_contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def ref_targetDataProtoype_(self):
        return self._artop_targetDataProtoypeRef

    @property
    def targetDataProtoype_(self):
        if self._artop_targetDataProtoypeRef is not None:
            if hasattr(self._artop_targetDataProtoypeRef, "uuid"):
                return self._artop_targetDataProtoypeRef.uuid
        return
