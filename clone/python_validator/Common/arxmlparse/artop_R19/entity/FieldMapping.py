# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FieldMapping.py
from .Identifiable import Identifiable

class FieldMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .InterfaceMapping import InterfaceMapping
        from .Field import Field
        from .ClientServerOperation import ClientServerOperation
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_interfaceMapping = None
        self._artop_fieldRef = None
        self._artop_getterOperationRef = None
        self._artop_notifierDataElementRef = None
        self._artop_setterOperationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_interfaceMapping': '"INTERFACE-MAPPING"', 
         '_artop_fieldRef': '"FIELD"', 
         '_artop_getterOperationRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_notifierDataElementRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_setterOperationRef': '"CLIENT-SERVER-OPERATION"'})

    @property
    def ref_interfaceMapping_(self):
        return self._artop_interfaceMapping

    @property
    def interfaceMapping_(self):
        if self._artop_interfaceMapping is not None:
            if hasattr(self._artop_interfaceMapping, "uuid"):
                return self._artop_interfaceMapping.uuid
        return

    @property
    def ref_field_(self):
        return self._artop_fieldRef

    @property
    def field_(self):
        if self._artop_fieldRef is not None:
            if hasattr(self._artop_fieldRef, "uuid"):
                return self._artop_fieldRef.uuid
        return

    @property
    def ref_getterOperation_(self):
        return self._artop_getterOperationRef

    @property
    def getterOperation_(self):
        if self._artop_getterOperationRef is not None:
            if hasattr(self._artop_getterOperationRef, "uuid"):
                return self._artop_getterOperationRef.uuid
        return

    @property
    def ref_notifierDataElement_(self):
        return self._artop_notifierDataElementRef

    @property
    def notifierDataElement_(self):
        if self._artop_notifierDataElementRef is not None:
            if hasattr(self._artop_notifierDataElementRef, "uuid"):
                return self._artop_notifierDataElementRef.uuid
        return

    @property
    def ref_setterOperation_(self):
        return self._artop_setterOperationRef

    @property
    def setterOperation_(self):
        if self._artop_setterOperationRef is not None:
            if hasattr(self._artop_setterOperationRef, "uuid"):
                return self._artop_setterOperationRef.uuid
        return
