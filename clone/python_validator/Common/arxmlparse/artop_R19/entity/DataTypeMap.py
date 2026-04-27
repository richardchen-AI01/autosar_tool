# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataTypeMap.py
from .ARObject import ARObject

class DataTypeMap(ARObject):

    def __init__(self):
        super().__init__()
        from .DataTypeMappingSet import DataTypeMappingSet
        from .ApplicationDataType import ApplicationDataType
        from .AbstractImplementationDataType import AbstractImplementationDataType
        self._artop_dataTypeMappingSet = None
        self._artop_applicationDataTypeRef = None
        self._artop_implementationDataTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTypeMappingSet':"DATA-TYPE-MAPPING-SET", 
         '_artop_applicationDataTypeRef':"APPLICATION-DATA-TYPE", 
         '_artop_implementationDataTypeRef':"ABSTRACT-IMPLEMENTATION-DATA-TYPE"})

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
    def ref_applicationDataType_(self):
        return self._artop_applicationDataTypeRef

    @property
    def applicationDataType_(self):
        if self._artop_applicationDataTypeRef is not None:
            if hasattr(self._artop_applicationDataTypeRef, "uuid"):
                return self._artop_applicationDataTypeRef.uuid
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
