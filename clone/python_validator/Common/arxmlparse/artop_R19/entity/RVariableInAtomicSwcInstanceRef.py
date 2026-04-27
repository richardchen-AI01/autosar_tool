# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RVariableInAtomicSwcInstanceRef.py
from .VariableInAtomicSwcInstanceRef import VariableInAtomicSwcInstanceRef

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):

    def __init__(self):
        super().__init__()
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .AtomicSwComponentType import AtomicSwComponentType
        self._artop_contextRPortRef = None
        self._artop_targetDataElementRef = None
        self._artop_atomicSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_contextRPortRef':"ABSTRACT-REQUIRED-PORT-PROTOTYPE", 
         '_artop_targetDataElementRef':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_atomicSwComponentType':"ATOMIC-SW-COMPONENT-TYPE"})

    @property
    def ref_contextRPort_(self):
        return self._artop_contextRPortRef

    @property
    def contextRPort_(self):
        if self._artop_contextRPortRef is not None:
            if hasattr(self._artop_contextRPortRef, "uuid"):
                return self._artop_contextRPortRef.uuid
        return

    @property
    def ref_targetDataElement_(self):
        return self._artop_targetDataElementRef

    @property
    def targetDataElement_(self):
        if self._artop_targetDataElementRef is not None:
            if hasattr(self._artop_targetDataElementRef, "uuid"):
                return self._artop_targetDataElementRef.uuid
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
