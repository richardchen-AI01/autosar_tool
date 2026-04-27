# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AnyInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class AnyInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AtpClassifier import AtpClassifier
        from .AtpFeature import AtpFeature
        from .VariationPoint import VariationPoint
        self._artop_atpClassifier = None
        self._artop_contextElementRef = []
        self._artop_targetRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_atpClassifier': '"ATP-CLASSIFIER"', 
         '_artop_contextElementRef': '"ATP-FEATURE"', 
         '_artop_targetRef': '"ATP-FEATURE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_base_(self):
        return self._artop_atpClassifier

    @property
    def base_(self):
        if self._artop_atpClassifier is not None:
            if hasattr(self._artop_atpClassifier, "uuid"):
                return self._artop_atpClassifier.uuid
        return

    @property
    def ref_contextElements_(self):
        return self._artop_contextElementRef

    @property
    def contextElements_(self):
        return self._artop_contextElementRef

    @property
    def ref_target_(self):
        return self._artop_targetRef

    @property
    def target_(self):
        if self._artop_targetRef is not None:
            if hasattr(self._artop_targetRef, "uuid"):
                return self._artop_targetRef.uuid
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
