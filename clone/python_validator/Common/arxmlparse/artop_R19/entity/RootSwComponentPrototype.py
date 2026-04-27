# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RootSwComponentPrototype.py
from .AtpPrototype import AtpPrototype

class RootSwComponentPrototype(AtpPrototype):

    def __init__(self):
        super().__init__()
        from .Executable import Executable
        from .SwComponentType import SwComponentType
        self._artop_executable = None
        self._artop_applicationTypeTref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_executable':"EXECUTABLE", 
         '_artop_applicationTypeTref':"SW-COMPONENT-TYPE"})

    @property
    def ref_executable_(self):
        return self._artop_executable

    @property
    def executable_(self):
        if self._artop_executable is not None:
            if hasattr(self._artop_executable, "uuid"):
                return self._artop_executable.uuid
        return

    @property
    def ref_applicationType_(self):
        return self._artop_applicationTypeTref

    @property
    def applicationType_(self):
        if self._artop_applicationTypeTref is not None:
            if hasattr(self._artop_applicationTypeTref, "uuid"):
                return self._artop_applicationTypeTref.uuid
        return
