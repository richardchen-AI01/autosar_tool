# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationArrayElement.py
from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype

class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):

    def __init__(self):
        super().__init__()
        from .ApplicationArrayDataType import ApplicationArrayDataType
        from .ApplicationPrimitiveDataType import ApplicationPrimitiveDataType
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_arraySizeHandling = None
        self._artop_arraySizeSemantics = None
        self._artop_applicationArrayDataType = None
        self._artop_indexDataTypeRef = None
        self._artop_maxNumberOfElements = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_applicationArrayDataType':"APPLICATION-ARRAY-DATA-TYPE", 
         '_artop_indexDataTypeRef':"APPLICATION-PRIMITIVE-DATA-TYPE", 
         '_artop_maxNumberOfElements':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def arraySizeHandling_(self):
        return self._artop_arraySizeHandling

    @property
    def arraySizeSemantics_(self):
        return self._artop_arraySizeSemantics

    @property
    def ref_applicationArrayDataType_(self):
        return self._artop_applicationArrayDataType

    @property
    def applicationArrayDataType_(self):
        if self._artop_applicationArrayDataType is not None:
            if hasattr(self._artop_applicationArrayDataType, "uuid"):
                return self._artop_applicationArrayDataType.uuid
        return

    @property
    def ref_indexDataType_(self):
        return self._artop_indexDataTypeRef

    @property
    def indexDataType_(self):
        if self._artop_indexDataTypeRef is not None:
            if hasattr(self._artop_indexDataTypeRef, "uuid"):
                return self._artop_indexDataTypeRef.uuid
        return

    @property
    def ref_maxNumberOfElements_(self):
        return self._artop_maxNumberOfElements

    @property
    def maxNumberOfElements_(self):
        if self._artop_maxNumberOfElements is not None:
            if hasattr(self._artop_maxNumberOfElements, "uuid"):
                return self._artop_maxNumberOfElements.uuid
        return
