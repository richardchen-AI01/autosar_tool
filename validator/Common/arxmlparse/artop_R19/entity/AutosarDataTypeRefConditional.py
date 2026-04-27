# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AutosarDataTypeRefConditional.py
from .ARObject import ARObject

class AutosarDataTypeRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ArgumentDataPrototype import ArgumentDataPrototype
        from .AutosarDataType import AutosarDataType
        from .VariationPoint import VariationPoint
        self._artop_argumentDataPrototype = None
        self._artop_autosarDataTypeRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_argumentDataPrototype':"ARGUMENT-DATA-PROTOTYPE", 
         '_artop_autosarDataTypeRef':"AUTOSAR-DATA-TYPE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_argumentDataPrototype_(self):
        return self._artop_argumentDataPrototype

    @property
    def argumentDataPrototype_(self):
        if self._artop_argumentDataPrototype is not None:
            if hasattr(self._artop_argumentDataPrototype, "uuid"):
                return self._artop_argumentDataPrototype.uuid
        return

    @property
    def ref_autosarDataType_(self):
        return self._artop_autosarDataTypeRef

    @property
    def autosarDataType_(self):
        if self._artop_autosarDataTypeRef is not None:
            if hasattr(self._artop_autosarDataTypeRef, "uuid"):
                return self._artop_autosarDataTypeRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
