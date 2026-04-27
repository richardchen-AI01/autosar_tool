# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MethodMapping.py
from .Identifiable import Identifiable

class MethodMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .InterfaceMapping import InterfaceMapping
        from .ClientServerOperation import ClientServerOperation
        self._artop_interfaceMapping = None
        self._artop_clientServerOperationRef = None
        self._artop_methodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_interfaceMapping':"INTERFACE-MAPPING", 
         '_artop_clientServerOperationRef':"CLIENT-SERVER-OPERATION", 
         '_artop_methodRef':"CLIENT-SERVER-OPERATION"})

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
    def ref_clientServerOperation_(self):
        return self._artop_clientServerOperationRef

    @property
    def clientServerOperation_(self):
        if self._artop_clientServerOperationRef is not None:
            if hasattr(self._artop_clientServerOperationRef, "uuid"):
                return self._artop_clientServerOperationRef.uuid
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
