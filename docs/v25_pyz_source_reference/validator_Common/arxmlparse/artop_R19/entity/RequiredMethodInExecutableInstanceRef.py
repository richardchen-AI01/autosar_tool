# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RequiredMethodInExecutableInstanceRef.py
from .AbstractMethodInExecutableInstanceRef import AbstractMethodInExecutableInstanceRef

class RequiredMethodInExecutableInstanceRef(AbstractMethodInExecutableInstanceRef):

    def __init__(self):
        super().__init__()
        from .ComMethodGrantDesign import ComMethodGrantDesign
        from .RootSwComponentPrototype import RootSwComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        from .ClientServerOperation import ClientServerOperation
        self._artop_comMethodGrantDesign = None
        self._artop_contextRootSwComponentPrototypeRef = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_contextRPortPrototypeRef = None
        self._artop_targetMethodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_comMethodGrantDesign': '"COM-METHOD-GRANT-DESIGN"', 
         '_artop_contextRootSwComponentPrototypeRef': '"ROOT-SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextRPortPrototypeRef': '"R-PORT-PROTOTYPE"', 
         '_artop_targetMethodRef': '"CLIENT-SERVER-OPERATION"'})

    @property
    def ref_comMethodGrantDesign_(self):
        return self._artop_comMethodGrantDesign

    @property
    def comMethodGrantDesign_(self):
        if self._artop_comMethodGrantDesign is not None:
            if hasattr(self._artop_comMethodGrantDesign, "uuid"):
                return self._artop_comMethodGrantDesign.uuid
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
    def ref_contextRPortPrototype_(self):
        return self._artop_contextRPortPrototypeRef

    @property
    def contextRPortPrototype_(self):
        if self._artop_contextRPortPrototypeRef is not None:
            if hasattr(self._artop_contextRPortPrototypeRef, "uuid"):
                return self._artop_contextRPortPrototypeRef.uuid
        return

    @property
    def ref_targetMethod_(self):
        return self._artop_targetMethodRef

    @property
    def targetMethod_(self):
        if self._artop_targetMethodRef is not None:
            if hasattr(self._artop_targetMethodRef, "uuid"):
                return self._artop_targetMethodRef.uuid
        return
