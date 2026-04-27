# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AclObjectSet.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class AclObjectSet(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .Collection import Collection
        from .AtpBlueprint import AtpBlueprint
        from .AutosarEngineeringObject import AutosarEngineeringObject
        from .AtpDefinition import AtpDefinition
        from .Referrable import Referrable
        self._artop_aclObjectClass = None
        self._artop_aclScope = None
        self._artop_collectionRef = None
        self._artop_derivedFromBlueprintRef = []
        self._artop_engineeringObject = []
        self._artop_objectDefinitionRef = []
        self._artop_objectDefintionRef = []
        self._artop_objectRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_collectionRef': '"COLLECTION"', 
         '_artop_derivedFromBlueprintRef': '"ATP-BLUEPRINT"', 
         '_artop_engineeringObject': '"AUTOSAR-ENGINEERING-OBJECT"', 
         '_artop_objectDefinitionRef': '"ATP-DEFINITION"', 
         '_artop_objectDefintionRef': '"ATP-DEFINITION"', 
         '_artop_objectRef': '"REFERRABLE"'})

    @property
    def aclObjectClass_(self):
        return self._artop_aclObjectClass

    @property
    def aclScope_(self):
        return self._artop_aclScope

    @property
    def ref_collection_(self):
        return self._artop_collectionRef

    @property
    def collection_(self):
        if self._artop_collectionRef is not None:
            if hasattr(self._artop_collectionRef, "uuid"):
                return self._artop_collectionRef.uuid
        return

    @property
    def ref_derivedFromBlueprints_(self):
        return self._artop_derivedFromBlueprintRef

    @property
    def derivedFromBlueprints_(self):
        return self._artop_derivedFromBlueprintRef

    @property
    def engineeringObjects_AutosarEngineeringObject(self):
        return self._artop_engineeringObject

    @property
    def ref_objectDefinitions_(self):
        return self._artop_objectDefinitionRef

    @property
    def objectDefinitions_(self):
        return self._artop_objectDefinitionRef

    @property
    def ref_objectDefintions_(self):
        return self._artop_objectDefintionRef

    @property
    def objectDefintions_(self):
        return self._artop_objectDefintionRef

    @property
    def ref_objects_(self):
        return self._artop_objectRef

    @property
    def objects_(self):
        return self._artop_objectRef
