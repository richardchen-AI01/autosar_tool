# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CppTemplateArgument.py
from .ARObject import ARObject

class CppTemplateArgument(ARObject):

    def __init__(self):
        super().__init__()
        from .CppImplementationDataType import CppImplementationDataType
        from .Allocator import Allocator
        self._artop_category = None
        self._artop_inplace = None
        self._artop_cppImplementationDataType = None
        self._artop_allocatorRef = None
        self._artop_templateTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_cppImplementationDataType':"CPP-IMPLEMENTATION-DATA-TYPE", 
         '_artop_allocatorRef':"ALLOCATOR", 
         '_artop_templateTypeRef':"CPP-IMPLEMENTATION-DATA-TYPE"})

    @property
    def category_(self):
        return self._artop_category

    @property
    def inplace_(self):
        if self._artop_inplace:
            if self._artop_inplace == "true":
                return True
            return False
        else:
            return self._artop_inplace

    @property
    def ref_cppImplementationDataType_(self):
        return self._artop_cppImplementationDataType

    @property
    def cppImplementationDataType_(self):
        if self._artop_cppImplementationDataType is not None:
            if hasattr(self._artop_cppImplementationDataType, "uuid"):
                return self._artop_cppImplementationDataType.uuid
        return

    @property
    def ref_allocator_(self):
        return self._artop_allocatorRef

    @property
    def allocator_(self):
        if self._artop_allocatorRef is not None:
            if hasattr(self._artop_allocatorRef, "uuid"):
                return self._artop_allocatorRef.uuid
        return

    @property
    def ref_templateType_(self):
        return self._artop_templateTypeRef

    @property
    def templateType_(self):
        if self._artop_templateTypeRef is not None:
            if hasattr(self._artop_templateTypeRef, "uuid"):
                return self._artop_templateTypeRef.uuid
        return
