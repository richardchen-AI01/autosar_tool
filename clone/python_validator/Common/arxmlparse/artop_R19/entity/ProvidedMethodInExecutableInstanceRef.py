# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProvidedMethodInExecutableInstanceRef.py
from .AbstractMethodInExecutableInstanceRef import AbstractMethodInExecutableInstanceRef

class ProvidedMethodInExecutableInstanceRef(AbstractMethodInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .RecoveryViaApplicationActionToClientServerOperationMapping import RecoveryViaApplicationActionToClientServerOperationMapping
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PPortPrototype import PPortPrototype
        from .ClientServerOperation import ClientServerOperation
        self._artop_recoveryViaApplicationActionToClientServerOperationMapping = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_contextPPortPrototypeRef = None
        self._artop_targetMethodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_recoveryViaApplicationActionToClientServerOperationMapping': '"RECOVERY-VIA-APPLICATION-ACTION-TO-CLIENT-SERVER-OPERATION-MAPPING"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPPortPrototypeRef': '"P-PORT-PROTOTYPE"', 
         '_artop_targetMethodRef': '"CLIENT-SERVER-OPERATION"'})

    @property
    def ref_recoveryViaApplicationActionToClientServerOperationMapping_(self):
        return self._artop_recoveryViaApplicationActionToClientServerOperationMapping

    @property
    def recoveryViaApplicationActionToClientServerOperationMapping_(self):
        if self._artop_recoveryViaApplicationActionToClientServerOperationMapping is not None:
            if hasattr(self._artop_recoveryViaApplicationActionToClientServerOperationMapping, "uuid"):
                return self._artop_recoveryViaApplicationActionToClientServerOperationMapping.uuid
        return

    @property
    def ref_contextRootSwComponentPrototype_(self):
        return self._artop_contextRootSwComponentPrototypeRef

    @property
    def contextRootSwComponentPrototype_(self):
        if self._artop_contextRootSwComponentPrototypeRef is not None:
            if hasattr(self._artop_contextRootSwComponentPrototypeRef, "uuid"):
                return self._artop_contextRootSwComponentPrototypeRef.uuid
        return

    @property
    def ref_contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def ref_contextPPortPrototype_(self):
        return self._artop_contextPPortPrototypeRef

    @property
    def contextPPortPrototype_(self):
        if self._artop_contextPPortPrototypeRef is not None:
            if hasattr(self._artop_contextPPortPrototypeRef, "uuid"):
                return self._artop_contextPPortPrototypeRef.uuid
        return

    @property
    def ref_targetMethod_(self):
        return self._artop_targetMethodRef

    @property
    def targetMethod_(self):
        if self._artop_targetMethodRef is not None:
            if hasattr(self._artop_targetMethodRef, "uuid"):
                return self._artop_targetMethodRef.uuid
        return
