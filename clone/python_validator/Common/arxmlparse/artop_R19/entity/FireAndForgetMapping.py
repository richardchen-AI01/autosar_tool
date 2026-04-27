# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FireAndForgetMapping.py
from .Identifiable import Identifiable

class FireAndForgetMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .InterfaceMapping import InterfaceMapping
        from .VariableDataPrototype import VariableDataPrototype
        from .ClientServerOperation import ClientServerOperation
        from .Trigger import Trigger
        self._artop_interfaceMapping = None
        self._artop_dataElementRef = None
        self._artop_methodRef = None
        self._artop_triggerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_interfaceMapping': '"INTERFACE-MAPPING"', 
         '_artop_dataElementRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_methodRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_triggerRef': '"TRIGGER"'})

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
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return

    @property
    def ref_method_(self):
        return self._artop_methodRef

    @property
    def method_(self):
        if self._artop_methodRef is not None:
            if hasattr(self._artop_methodRef, "uuid"):
                return self._artop_methodRef.uuid
        return

    @property
    def ref_trigger_(self):
        return self._artop_triggerRef

    @property
    def trigger_(self):
        if self._artop_triggerRef is not None:
            if hasattr(self._artop_triggerRef, "uuid"):
                return self._artop_triggerRef.uuid
        return
