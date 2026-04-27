# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\OperationInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class OperationInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .ClientServerOperation import ClientServerOperation
        self._artop_system = None
        self._artop_contextCompositionRef = None
        self._artop_contextComponentRef = []
        self._artop_contextPortRef = None
        self._artop_targetOperationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_system': '"SYSTEM"', 
         '_artop_contextCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortRef': '"PORT-PROTOTYPE"', 
         '_artop_targetOperationRef': '"CLIENT-SERVER-OPERATION"'})

    @property
    def ref_base_(self):
        return self._artop_system

    @property
    def base_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_contextComposition_(self):
        return self._artop_contextCompositionRef

    @property
    def contextComposition_(self):
        if self._artop_contextCompositionRef is not None:
            if hasattr(self._artop_contextCompositionRef, "uuid"):
                return self._artop_contextCompositionRef.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def ref_contextPort_(self):
        return self._artop_contextPortRef

    @property
    def contextPort_(self):
        if self._artop_contextPortRef is not None:
            if hasattr(self._artop_contextPortRef, "uuid"):
                return self._artop_contextPortRef.uuid
        return

    @property
    def ref_targetOperation_(self):
        return self._artop_targetOperationRef

    @property
    def targetOperation_(self):
        if self._artop_targetOperationRef is not None:
            if hasattr(self._artop_targetOperationRef, "uuid"):
                return self._artop_targetOperationRef.uuid
        return
