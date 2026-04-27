# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcServiceDependencyInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class SwcServiceDependencyInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .SwcServiceDependency import SwcServiceDependency
        self._artop_system = None
        self._artop_contextRootSwCompositionRef = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_targetSwcServiceDependencyRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_system': '"SYSTEM"', 
         '_artop_contextRootSwCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetSwcServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"'})

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
    def ref_contextRootSwComposition_(self):
        return self._artop_contextRootSwCompositionRef

    @property
    def contextRootSwComposition_(self):
        if self._artop_contextRootSwCompositionRef is not None:
            if hasattr(self._artop_contextRootSwCompositionRef, "uuid"):
                return self._artop_contextRootSwCompositionRef.uuid
        return

    @property
    def ref_contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def ref_targetSwcServiceDependency_(self):
        return self._artop_targetSwcServiceDependencyRef

    @property
    def targetSwcServiceDependency_(self):
        if self._artop_targetSwcServiceDependencyRef is not None:
            if hasattr(self._artop_targetSwcServiceDependencyRef, "uuid"):
                return self._artop_targetSwcServiceDependencyRef.uuid
        return
