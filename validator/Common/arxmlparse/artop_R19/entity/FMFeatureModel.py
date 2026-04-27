# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeatureModel.py
from .ARElement import ARElement

class FMFeatureModel(ARElement):

    def __init__(self):
        super().__init__()
        from .FMFeature import FMFeature
        self._artop_featureRef = []
        self._artop_rootRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_featureRef':"FM-FEATURE", 
         '_artop_rootRef':"FM-FEATURE"})

    @property
    def ref_features_(self):
        return self._artop_featureRef

    @property
    def features_(self):
        return self._artop_featureRef

    @property
    def ref_root_(self):
        return self._artop_rootRef

    @property
    def root_(self):
        if self._artop_rootRef is not None:
            if hasattr(self._artop_rootRef, "uuid"):
                return self._artop_rootRef.uuid
        return
