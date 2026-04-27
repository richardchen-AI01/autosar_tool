# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionIoElement.py
from .ARObject import ARObject

class BuildActionIoElement(ARObject):

    def __init__(self):
        super().__init__()
        from .Sdg import Sdg
        from .EcucDefinitionElement import EcucDefinitionElement
        from .BuildEngineeringObject import BuildEngineeringObject
        from .ForeignModelReference import ForeignModelReference
        from .GenericModelReference import GenericModelReference
        self._artop_category = None
        self._artop_role = None
        self._artop_sdg = []
        self._artop_ecucDefinitionRef = None
        self._artop_engineeringObject = None
        self._artop_foreignModelReference = None
        self._artop_modelObjectReference = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_sdg': '"SDG"', 
         '_artop_ecucDefinitionRef': '"ECUC-DEFINITION-ELEMENT"', 
         '_artop_engineeringObject': '"BUILD-ENGINEERING-OBJECT"', 
         '_artop_foreignModelReference': '"FOREIGN-MODEL-REFERENCE"', 
         '_artop_modelObjectReference': '"GENERIC-MODEL-REFERENCE"'})

    @property
    def category_(self):
        return self._artop_category

    @property
    def role_(self):
        return self._artop_role

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg

    @property
    def ref_ecucDefinition_(self):
        return self._artop_ecucDefinitionRef

    @property
    def ecucDefinition_(self):
        if self._artop_ecucDefinitionRef is not None:
            if hasattr(self._artop_ecucDefinitionRef, "uuid"):
                return self._artop_ecucDefinitionRef.uuid
        return

    @property
    def ref_engineeringObject_(self):
        return self._artop_engineeringObject

    @property
    def engineeringObject_(self):
        if self._artop_engineeringObject is not None:
            if hasattr(self._artop_engineeringObject, "uuid"):
                return self._artop_engineeringObject.uuid
        return

    @property
    def ref_foreignModelReference_(self):
        return self._artop_foreignModelReference

    @property
    def foreignModelReference_(self):
        if self._artop_foreignModelReference is not None:
            if hasattr(self._artop_foreignModelReference, "uuid"):
                return self._artop_foreignModelReference.uuid
        return

    @property
    def ref_modelObjectReference_(self):
        return self._artop_modelObjectReference

    @property
    def modelObjectReference_(self):
        if self._artop_modelObjectReference is not None:
            if hasattr(self._artop_modelObjectReference, "uuid"):
                return self._artop_modelObjectReference.uuid
        return
