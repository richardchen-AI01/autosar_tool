# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CppImplementationDataTypeElementQualifier.py
from .ARObject import ARObject

class CppImplementationDataTypeElementQualifier(ARObject):

    def __init__(self):
        super().__init__()
        from .CppImplementationDataTypeElement import CppImplementationDataTypeElement
        from .CppImplementationDataType import CppImplementationDataType
        self._artop_inplace = None
        self._artop_cppImplementationDataTypeElement = None
        self._artop_typeReferenceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_cppImplementationDataTypeElement':"CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT", 
         '_artop_typeReferenceRef':"CPP-IMPLEMENTATION-DATA-TYPE"})

    @property
    def inplace_(self):
        if self._artop_inplace:
            if self._artop_inplace == "true":
                return True
            return False
        else:
            return self._artop_inplace

    @property
    def ref_cppImplementationDataTypeElement_(self):
        return self._artop_cppImplementationDataTypeElement

    @property
    def cppImplementationDataTypeElement_(self):
        if self._artop_cppImplementationDataTypeElement is not None:
            if hasattr(self._artop_cppImplementationDataTypeElement, "uuid"):
                return self._artop_cppImplementationDataTypeElement.uuid
        return

    @property
    def ref_typeReference_(self):
        return self._artop_typeReferenceRef

    @property
    def typeReference_(self):
        if self._artop_typeReferenceRef is not None:
            if hasattr(self._artop_typeReferenceRef, "uuid"):
                return self._artop_typeReferenceRef.uuid
        return
