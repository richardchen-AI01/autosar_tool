# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComponentInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ComponentInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        self._artop_system = None
        self._artop_contextCompositionRef = None
        self._artop_contextComponentRef = []
        self._artop_targetComponentRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_system': '"SYSTEM"', 
         '_artop_contextCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetComponentRef': '"SW-COMPONENT-PROTOTYPE"'})

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
    def ref_targetComponent_(self):
        return self._artop_targetComponentRef

    @property
    def targetComponent_(self):
        if self._artop_targetComponentRef is not None:
            if hasattr(self._artop_targetComponentRef, "uuid"):
                return self._artop_targetComponentRef.uuid
        return
