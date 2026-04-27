# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RPortPrototypeInExecutableInstanceRef.py
from .AbstractPortPrototypeInExecutableInstanceRef import AbstractPortPrototypeInExecutableInstanceRef

class RPortPrototypeInExecutableInstanceRef(AbstractPortPrototypeInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_targetRPortPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_contextRootSwComponentPrototypeRef':"ROOT-SW-COMPONENT-PROTOTYPE", 
         '_artop_contextComponentPrototypeRef':"SW-COMPONENT-PROTOTYPE", 
         '_artop_targetRPortPrototypeRef':"R-PORT-PROTOTYPE"})

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
    def ref_targetRPortPrototype_(self):
        return self._artop_targetRPortPrototypeRef

    @property
    def targetRPortPrototype_(self):
        if self._artop_targetRPortPrototypeRef is not None:
            if hasattr(self._artop_targetRPortPrototypeRef, "uuid"):
                return self._artop_targetRPortPrototypeRef.uuid
        return
