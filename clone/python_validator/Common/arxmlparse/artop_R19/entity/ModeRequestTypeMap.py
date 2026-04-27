# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeRequestTypeMap.py
from .ARObject import ARObject

class ModeRequestTypeMap(ARObject):

    def __init__(self):
        super().__init__()
        from .DataTypeMappingSet import DataTypeMappingSet
        from .AbstractImplementationDataType import AbstractImplementationDataType
        from .ModeDeclarationGroup import ModeDeclarationGroup
        self._artop_dataTypeMappingSet = None
        self._artop_implementationDataTypeRef = None
        self._artop_modeGroupRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTypeMappingSet':"DATA-TYPE-MAPPING-SET", 
         '_artop_implementationDataTypeRef':"ABSTRACT-IMPLEMENTATION-DATA-TYPE", 
         '_artop_modeGroupRef':"MODE-DECLARATION-GROUP"})

    @property
    def ref_dataTypeMappingSet_(self):
        return self._artop_dataTypeMappingSet

    @property
    def dataTypeMappingSet_(self):
        if self._artop_dataTypeMappingSet is not None:
            if hasattr(self._artop_dataTypeMappingSet, "uuid"):
                return self._artop_dataTypeMappingSet.uuid
        return

    @property
    def ref_implementationDataType_(self):
        return self._artop_implementationDataTypeRef

    @property
    def implementationDataType_(self):
        if self._artop_implementationDataTypeRef is not None:
            if hasattr(self._artop_implementationDataTypeRef, "uuid"):
                return self._artop_implementationDataTypeRef.uuid
        return

    @property
    def ref_modeGroup_(self):
        return self._artop_modeGroupRef

    @property
    def modeGroup_(self):
        if self._artop_modeGroupRef is not None:
            if hasattr(self._artop_modeGroupRef, "uuid"):
                return self._artop_modeGroupRef.uuid
        return
