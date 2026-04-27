# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureSelectionSet.py
from .ARElement import ARElement

class FMFeatureSelectionSet(ARElement):

    def __init__(self):
        super().__init__()
        from .FMFeatureModel import FMFeatureModel
        from .FMFeatureSelection import FMFeatureSelection
        self._artop_featureModelRef = []
        self._artop_includeRef = []
        self._artop_selection = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_featureModelRef':"FM-FEATURE-MODEL", 
         '_artop_includeRef':"FM-FEATURE-SELECTION-SET", 
         '_artop_selection':"FM-FEATURE-SELECTION"})

    @property
    def ref_featureModels_(self):
        return self._artop_featureModelRef

    @property
    def featureModels_(self):
        return self._artop_featureModelRef

    @property
    def ref_includes_(self):
        return self._artop_includeRef

    @property
    def includes_(self):
        return self._artop_includeRef

    @property
    def selections_FMFeatureSelection(self):
        return self._artop_selection
