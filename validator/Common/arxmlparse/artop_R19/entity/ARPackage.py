# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ARPackage.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .CollectableElement import CollectableElement

class ARPackage(CollectableElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .ReferenceBase import ReferenceBase
        from .PackageableElement import PackageableElement
        from .VariationPoint import VariationPoint
        self._artop_referenceBase = []
        self._artop_element = []
        self._artop_arPackage = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_referenceBase': '"REFERENCE-BASE"', 
         '_artop_element': '"PACKAGEABLE-ELEMENT"', 
         '_artop_arPackage': '"AR-PACKAGE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def referenceBases_ReferenceBase(self):
        return self._artop_referenceBase

    @property
    def elements_PackageableElement(self):
        return self._artop_element

    @property
    def arPackages_ARPackage(self):
        return self._artop_arPackage

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
