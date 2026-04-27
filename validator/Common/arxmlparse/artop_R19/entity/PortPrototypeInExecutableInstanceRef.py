# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototypeInExecutableInstanceRef.py
from .AbstractPortPrototypeInExecutableInstanceRef import AbstractPortPrototypeInExecutableInstanceRef

class PortPrototypeInExecutableInstanceRef(AbstractPortPrototypeInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .Executable import Executable
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        self._artop_executable = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_targetPortPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_executable': '"EXECUTABLE"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetPortPrototypeRef': '"PORT-PROTOTYPE"'})

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
    def ref_targetPortPrototype_(self):
        return self._artop_targetPortPrototypeRef

    @property
    def targetPortPrototype_(self):
        if self._artop_targetPortPrototypeRef is not None:
            if hasattr(self._artop_targetPortPrototypeRef, "uuid"):
                return self._artop_targetPortPrototypeRef.uuid
        return
