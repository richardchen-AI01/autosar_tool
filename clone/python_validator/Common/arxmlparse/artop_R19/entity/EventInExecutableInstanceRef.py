# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EventInExecutableInstanceRef.py
from .AutosarDataPrototypeInExecutableInstanceRef import AutosarDataPrototypeInExecutableInstanceRef

class EventInExecutableInstanceRef(AutosarDataPrototypeInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .ComEventGrantDesign import ComEventGrantDesign
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_comEventGrantDesign = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_contextRPortPrototypeRef = None
        self._artop_targetEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_comEventGrantDesign': '"COM-EVENT-GRANT-DESIGN"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextRPortPrototypeRef': '"R-PORT-PROTOTYPE"', 
         '_artop_targetEventRef': '"VARIABLE-DATA-PROTOTYPE"'})

    @property
    def ref_comEventGrantDesign_(self):
        return self._artop_comEventGrantDesign

    @property
    def comEventGrantDesign_(self):
        if self._artop_comEventGrantDesign is not None:
            if hasattr(self._artop_comEventGrantDesign, "uuid"):
                return self._artop_comEventGrantDesign.uuid
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
    def ref_contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def ref_contextRPortPrototype_(self):
        return self._artop_contextRPortPrototypeRef

    @property
    def contextRPortPrototype_(self):
        if self._artop_contextRPortPrototypeRef is not None:
            if hasattr(self._artop_contextRPortPrototypeRef, "uuid"):
                return self._artop_contextRPortPrototypeRef.uuid
        return

    @property
    def ref_targetEvent_(self):
        return self._artop_targetEventRef

    @property
    def targetEvent_(self):
        if self._artop_targetEventRef is not None:
            if hasattr(self._artop_targetEventRef, "uuid"):
                return self._artop_targetEventRef.uuid
        return
