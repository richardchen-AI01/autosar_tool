# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CppImplementationDataType.py
from .CppImplementationDataTypeContextTarget import CppImplementationDataTypeContextTarget
from .AbstractImplementationDataType import AbstractImplementationDataType

class CppImplementationDataType(AbstractImplementationDataType, CppImplementationDataTypeContextTarget):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .SymbolProps import SymbolProps
        from .CppImplementationDataTypeElement import CppImplementationDataTypeElement
        from .CppTemplateArgument import CppTemplateArgument
        self._artop_typeEmitter = None
        self._artop_arraySize = None
        self._artop_namespace = []
        self._artop_subElement = []
        self._artop_templateArgument = []
        self._artop_typeReferenceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_arraySize': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_namespace': '"SYMBOL-PROPS"', 
         '_artop_subElement': '"CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_templateArgument': '"CPP-TEMPLATE-ARGUMENT"', 
         '_artop_typeReferenceRef': '"CPP-IMPLEMENTATION-DATA-TYPE"'})

    @property
    def typeEmitter_(self):
        return self._artop_typeEmitter

    @property
    def ref_arraySize_(self):
        return self._artop_arraySize

    @property
    def arraySize_(self):
        if self._artop_arraySize is not None:
            if hasattr(self._artop_arraySize, "uuid"):
                return self._artop_arraySize.uuid
        return

    @property
    def namespaces_SymbolProps(self):
        return self._artop_namespace

    @property
    def subElements_CppImplementationDataTypeElement(self):
        return self._artop_subElement

    @property
    def templateArguments_CppTemplateArgument(self):
        return self._artop_templateArgument

    @property
    def ref_typeReference_(self):
        return self._artop_typeReferenceRef

    @property
    def typeReference_(self):
        if self._artop_typeReferenceRef is not None:
            if hasattr(self._artop_typeReferenceRef, "uuid"):
                return self._artop_typeReferenceRef.uuid
        return
