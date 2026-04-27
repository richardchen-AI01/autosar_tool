# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureDecomposition.py
from .ARObject import ARObject

class FMFeatureDecomposition(ARObject):

    def __init__(self):
        super().__init__()
        from .FMFeature import FMFeature
        self._artop_category = None
        self._artop_max = None
        self._artop_min = None
        self._artop_fmFeature = None
        self._artop_featureRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_fmFeature':"FM-FEATURE", 
         '_artop_featureRef':"FM-FEATURE"})

    @property
    def category_(self):
        return self._artop_category

    @property
    def max_(self):
        return self._artop_max

    @property
    def min_(self):
        return self._artop_min

    @property
    def ref_fMFeature_(self):
        return self._artop_fmFeature

    @property
    def fMFeature_(self):
        if self._artop_fmFeature is not None:
            if hasattr(self._artop_fmFeature, "uuid"):
                return self._artop_fmFeature.uuid
        return

    @property
    def ref_features_(self):
        return self._artop_featureRef

    @property
    def features_(self):
        return self._artop_featureRef
