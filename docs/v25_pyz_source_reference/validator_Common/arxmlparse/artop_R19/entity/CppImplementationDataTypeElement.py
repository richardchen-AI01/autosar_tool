# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CppImplementationDataTypeElement.py
from .CppImplementationDataTypeContextTarget import CppImplementationDataTypeContextTarget
from .AbstractImplementationDataTypeElement import AbstractImplementationDataTypeElement

class CppImplementationDataTypeElement(AbstractImplementationDataTypeElement, CppImplementationDataTypeContextTarget):

    def __init__(self):
        super().__init__()
        from .CppImplementationDataType import CppImplementationDataType
        from .CppImplementationDataTypeElementQualifier import CppImplementationDataTypeElementQualifier
        self._artop_isOptional = None
        self._artop_cppImplementationDataType = None
        self._artop_typeReference = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_cppImplementationDataType':"CPP-IMPLEMENTATION-DATA-TYPE", 
         '_artop_typeReference':"CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT-QUALIFIER"})

    @property
    def isOptional_(self):
        if self._artop_isOptional:
            if self._artop_isOptional == "true":
                return True
            return False
        else:
            return self._artop_isOptional

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
    def ref_typeReference_(self):
        return self._artop_typeReference

    @property
    def typeReference_(self):
        if self._artop_typeReference is not None:
            if hasattr(self._artop_typeReference, "uuid"):
                return self._artop_typeReference.uuid
        return
