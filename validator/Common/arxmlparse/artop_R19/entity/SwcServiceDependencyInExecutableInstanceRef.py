# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcServiceDependencyInExecutableInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class SwcServiceDependencyInExecutableInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .Executable import Executable
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .SwcServiceDependency import SwcServiceDependency
        self._artop_executable = None
        self._artop_contextRootComponentRef = None
        self._artop_contextComponentRef = []
        self._artop_targetSwcServiceDependencyRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_executable': '"EXECUTABLE"', 
         '_artop_contextRootComponentRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetSwcServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"'})

    @property
    def ref_base_(self):
        return self._artop_executable

    @property
    def base_(self):
        if self._artop_executable is not None:
            if hasattr(self._artop_executable, "uuid"):
                return self._artop_executable.uuid
        return

    @property
    def ref_contextRootComponent_(self):
        return self._artop_contextRootComponentRef

    @property
    def contextRootComponent_(self):
        if self._artop_contextRootComponentRef is not None:
            if hasattr(self._artop_contextRootComponentRef, "uuid"):
                return self._artop_contextRootComponentRef.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def ref_targetSwcServiceDependency_(self):
        return self._artop_targetSwcServiceDependencyRef

    @property
    def targetSwcServiceDependency_(self):
        if self._artop_targetSwcServiceDependencyRef is not None:
            if hasattr(self._artop_targetSwcServiceDependencyRef, "uuid"):
                return self._artop_targetSwcServiceDependencyRef.uuid
        return
