# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ImplementationDataType.py
from .AbstractImplementationDataType import AbstractImplementationDataType

class ImplementationDataType(AbstractImplementationDataType):

    def __init__(self):
        super().__init__()
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        from .SymbolProps import SymbolProps
        self._artop_dynamicArraySizeProfile = None
        self._artop_isStructWithOptionalElement = None
        self._artop_typeEmitter = None
        self._artop_subElement = []
        self._artop_symbolProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_subElement':"IMPLEMENTATION-DATA-TYPE-ELEMENT", 
         '_artop_symbolProps':"SYMBOL-PROPS"})

    @property
    def dynamicArraySizeProfile_(self):
        return self._artop_dynamicArraySizeProfile

    @property
    def isStructWithOptionalElement_(self):
        if self._artop_isStructWithOptionalElement:
            if self._artop_isStructWithOptionalElement == "true":
                return True
            return False
        else:
            return self._artop_isStructWithOptionalElement

    @property
    def typeEmitter_(self):
        return self._artop_typeEmitter

    @property
    def subElements_ImplementationDataTypeElement(self):
        return self._artop_subElement

    @property
    def ref_symbolProps_(self):
        return self._artop_symbolProps

    @property
    def symbolProps_(self):
        if self._artop_symbolProps is not None:
            if hasattr(self._artop_symbolProps, "uuid"):
                return self._artop_symbolProps.uuid
        return
