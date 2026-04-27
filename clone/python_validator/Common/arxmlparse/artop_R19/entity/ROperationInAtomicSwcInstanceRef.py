# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ROperationInAtomicSwcInstanceRef.py
from .OperationInAtomicSwcInstanceRef import OperationInAtomicSwcInstanceRef

class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):

    def __init__(self):
        super().__init__()
        from .ServerCallPoint import ServerCallPoint
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        from .ClientServerOperation import ClientServerOperation
        from .AtomicSwComponentType import AtomicSwComponentType
        self._artop_serverCallPoint = None
        self._artop_contextRPortRef = None
        self._artop_targetRequiredOperationRef = None
        self._artop_atomicSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_serverCallPoint': '"SERVER-CALL-POINT"', 
         '_artop_contextRPortRef': '"ABSTRACT-REQUIRED-PORT-PROTOTYPE"', 
         '_artop_targetRequiredOperationRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"'})

    @property
    def ref_serverCallPoint_(self):
        return self._artop_serverCallPoint

    @property
    def serverCallPoint_(self):
        if self._artop_serverCallPoint is not None:
            if hasattr(self._artop_serverCallPoint, "uuid"):
                return self._artop_serverCallPoint.uuid
        return

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
    def ref_targetRequiredOperation_(self):
        return self._artop_targetRequiredOperationRef

    @property
    def targetRequiredOperation_(self):
        if self._artop_targetRequiredOperationRef is not None:
            if hasattr(self._artop_targetRequiredOperationRef, "uuid"):
                return self._artop_targetRequiredOperationRef.uuid
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
