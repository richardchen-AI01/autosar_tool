# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureRelation.py
from .Identifiable import Identifiable

class FMFeatureRelation(Identifiable):

    def __init__(self):
        super().__init__()
        from .FMFeature import FMFeature
        from .FMConditionByFeaturesAndAttributes import FMConditionByFeaturesAndAttributes
        self._artop_fmFeature = None
        self._artop_featureRef = []
        self._artop_restriction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_fmFeature':"FM-FEATURE", 
         '_artop_featureRef':"FM-FEATURE", 
         '_artop_restriction':"FM-CONDITION-BY-FEATURES-AND-ATTRIBUTES"})

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

    @property
    def ref_restriction_(self):
        return self._artop_restriction

    @property
    def restriction_(self):
        if self._artop_restriction is not None:
            if hasattr(self._artop_restriction, "uuid"):
                return self._artop_restriction.uuid
        return
