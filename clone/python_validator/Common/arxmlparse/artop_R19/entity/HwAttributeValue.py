# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwAttributeValue.py
from .ARObject import ARObject

class HwAttributeValue(ARObject):

    def __init__(self):
        super().__init__()
        from .HwDescriptionEntity import HwDescriptionEntity
        from .Annotation import Annotation
        from .HwAttributeDef import HwAttributeDef
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        from .VariationPoint import VariationPoint
        self._artop_vt = None
        self._artop_hwDescriptionEntity = None
        self._artop_annotation = None
        self._artop_hwAttributeDefRef = None
        self._artop_v = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_hwDescriptionEntity': '"HW-DESCRIPTION-ENTITY"', 
         '_artop_annotation': '"ANNOTATION"', 
         '_artop_hwAttributeDefRef': '"HW-ATTRIBUTE-DEF"', 
         '_artop_v': '"NUMERICAL-VALUE-VARIATION-POINT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def vt_(self):
        return self._artop_vt

    @property
    def ref_hwDescriptionEntity_(self):
        return self._artop_hwDescriptionEntity

    @property
    def hwDescriptionEntity_(self):
        if self._artop_hwDescriptionEntity is not None:
            if hasattr(self._artop_hwDescriptionEntity, "uuid"):
                return self._artop_hwDescriptionEntity.uuid
        return

    @property
    def ref_annotation_(self):
        return self._artop_annotation

    @property
    def annotation_(self):
        if self._artop_annotation is not None:
            if hasattr(self._artop_annotation, "uuid"):
                return self._artop_annotation.uuid
        return

    @property
    def ref_hwAttributeDef_(self):
        return self._artop_hwAttributeDefRef

    @property
    def hwAttributeDef_(self):
        if self._artop_hwAttributeDefRef is not None:
            if hasattr(self._artop_hwAttributeDefRef, "uuid"):
                return self._artop_hwAttributeDefRef.uuid
        return

    @property
    def ref_v_(self):
        return self._artop_v

    @property
    def v_(self):
        if self._artop_v is not None:
            if hasattr(self._artop_v, "uuid"):
                return self._artop_v.uuid
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
