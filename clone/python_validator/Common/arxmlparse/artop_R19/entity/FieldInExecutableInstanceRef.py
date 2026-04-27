# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FieldInExecutableInstanceRef.py
from .AutosarDataPrototypeInExecutableInstanceRef import AutosarDataPrototypeInExecutableInstanceRef

class FieldInExecutableInstanceRef(AutosarDataPrototypeInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .ComFieldGrantDesign import ComFieldGrantDesign
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        from .Field import Field
        self._artop_comFieldGrantDesign = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_contextRPortPrototypeRef = None
        self._artop_targetFieldRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_comFieldGrantDesign': '"COM-FIELD-GRANT-DESIGN"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextRPortPrototypeRef': '"R-PORT-PROTOTYPE"', 
         '_artop_targetFieldRef': '"FIELD"'})

    @property
    def ref_comFieldGrantDesign_(self):
        return self._artop_comFieldGrantDesign

    @property
    def comFieldGrantDesign_(self):
        if self._artop_comFieldGrantDesign is not None:
            if hasattr(self._artop_comFieldGrantDesign, "uuid"):
                return self._artop_comFieldGrantDesign.uuid
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
    def ref_targetField_(self):
        return self._artop_targetFieldRef

    @property
    def targetField_(self):
        if self._artop_targetFieldRef is not None:
            if hasattr(self._artop_targetFieldRef, "uuid"):
                return self._artop_targetFieldRef.uuid
        return
