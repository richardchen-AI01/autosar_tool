# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataTransformation.py
from .Identifiable import Identifiable

class DataTransformation(Identifiable):

    def __init__(self):
        super().__init__()
        from .DataTransformationSet import DataTransformationSet
        from .TransformationTechnology import TransformationTechnology
        from .VariationPoint import VariationPoint
        self._artop_dataTransformationKind = None
        self._artop_executeDespiteDataUnavailability = None
        self._artop_dataTransformationSet = None
        self._artop_transformerChainRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTransformationSet':"DATA-TRANSFORMATION-SET", 
         '_artop_transformerChainRef':"TRANSFORMATION-TECHNOLOGY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def dataTransformationKind_(self):
        return self._artop_dataTransformationKind

    @property
    def executeDespiteDataUnavailability_(self):
        if self._artop_executeDespiteDataUnavailability:
            if self._artop_executeDespiteDataUnavailability == "true":
                return True
            return False
        else:
            return self._artop_executeDespiteDataUnavailability

    @property
    def ref_dataTransformationSet_(self):
        return self._artop_dataTransformationSet

    @property
    def dataTransformationSet_(self):
        if self._artop_dataTransformationSet is not None:
            if hasattr(self._artop_dataTransformationSet, "uuid"):
                return self._artop_dataTransformationSet.uuid
        return

    @property
    def ref_transformerChains_(self):
        return self._artop_transformerChainRef

    @property
    def transformerChains_(self):
        return self._artop_transformerChainRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
