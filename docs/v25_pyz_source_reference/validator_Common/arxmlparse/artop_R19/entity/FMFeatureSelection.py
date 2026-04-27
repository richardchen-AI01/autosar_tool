# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureSelection.py
from .Identifiable import Identifiable

class FMFeatureSelection(Identifiable):

    def __init__(self):
        super().__init__()
        from .FMFeatureSelectionSet import FMFeatureSelectionSet
        from .FMFeature import FMFeature
        from .FMAttributeValue import FMAttributeValue
        self._artop_state = None
        self._artop_minimumSelectedBindingTime = None
        self._artop_maximumSelectedBindingTime = None
        self._artop_fmFeatureSelectionSet = None
        self._artop_featureRef = None
        self._artop_attributeValue = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_fmFeatureSelectionSet':"FM-FEATURE-SELECTION-SET", 
         '_artop_featureRef':"FM-FEATURE", 
         '_artop_attributeValue':"FM-ATTRIBUTE-VALUE"})

    @property
    def state_(self):
        return self._artop_state

    @property
    def minimumSelectedBindingTime_(self):
        return self._artop_minimumSelectedBindingTime

    @property
    def maximumSelectedBindingTime_(self):
        return self._artop_maximumSelectedBindingTime

    @property
    def ref_fMFeatureSelectionSet_(self):
        return self._artop_fmFeatureSelectionSet

    @property
    def fMFeatureSelectionSet_(self):
        if self._artop_fmFeatureSelectionSet is not None:
            if hasattr(self._artop_fmFeatureSelectionSet, "uuid"):
                return self._artop_fmFeatureSelectionSet.uuid
        return

    @property
    def ref_feature_(self):
        return self._artop_featureRef

    @property
    def feature_(self):
        if self._artop_featureRef is not None:
            if hasattr(self._artop_featureRef, "uuid"):
                return self._artop_featureRef.uuid
        return

    @property
    def attributeValues_FMAttributeValue(self):
        return self._artop_attributeValue
