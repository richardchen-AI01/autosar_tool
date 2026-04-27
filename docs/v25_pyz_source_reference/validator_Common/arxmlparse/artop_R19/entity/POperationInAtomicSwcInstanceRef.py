# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\POperationInAtomicSwcInstanceRef.py
from .OperationInAtomicSwcInstanceRef import OperationInAtomicSwcInstanceRef

class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):

    def __init__(self):
        super().__init__()
        from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype
        from .ClientServerOperation import ClientServerOperation
        from .AtomicSwComponentType import AtomicSwComponentType
        self._artop_contextPPortRef = None
        self._artop_targetProvidedOperationRef = None
        self._artop_atomicSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_contextPPortRef':"ABSTRACT-PROVIDED-PORT-PROTOTYPE", 
         '_artop_targetProvidedOperationRef':"CLIENT-SERVER-OPERATION", 
         '_artop_atomicSwComponentType':"ATOMIC-SW-COMPONENT-TYPE"})

    @property
    def ref_contextPPort_(self):
        return self._artop_contextPPortRef

    @property
    def contextPPort_(self):
        if self._artop_contextPPortRef is not None:
            if hasattr(self._artop_contextPPortRef, "uuid"):
                return self._artop_contextPPortRef.uuid
        return

    @property
    def ref_targetProvidedOperation_(self):
        return self._artop_targetProvidedOperationRef

    @property
    def targetProvidedOperation_(self):
        if self._artop_targetProvidedOperationRef is not None:
            if hasattr(self._artop_targetProvidedOperationRef, "uuid"):
                return self._artop_targetProvidedOperationRef.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_atomicSwComponentType

    @property
    def base_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return
