# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PPortPrototypeInExecutableInstanceRef.py
from .AbstractPortPrototypeInExecutableInstanceRef import AbstractPortPrototypeInExecutableInstanceRef

class PPortPrototypeInExecutableInstanceRef(AbstractPortPrototypeInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .PPortPrototype import PPortPrototype
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_targetPPortPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_contextRootSwComponentPrototypeRef':"ROOT-SW-COMPONENT-PROTOTYPE", 
         '_artop_contextComponentPrototypeRef':"SW-COMPONENT-PROTOTYPE", 
         '_artop_targetPPortPrototypeRef':"P-PORT-PROTOTYPE"})

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
    def ref_targetPPortPrototype_(self):
        return self._artop_targetPPortPrototypeRef

    @property
    def targetPPortPrototype_(self):
        if self._artop_targetPPortPrototypeRef is not None:
            if hasattr(self._artop_targetPPortPrototypeRef, "uuid"):
                return self._artop_targetPPortPrototypeRef.uuid
        return
