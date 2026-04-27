# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFeature.py
from .ARElement import ARElement

class FMFeature(ARElement):

    def __init__(self):
        super().__init__()
        from .FMAttributeDef import FMAttributeDef
        from .FMFeatureDecomposition import FMFeatureDecomposition
        from .FMFeatureRelation import FMFeatureRelation
        from .FMFeatureRestriction import FMFeatureRestriction
        self._artop_maximumIntendedBindingTime = None
        self._artop_minimumIntendedBindingTime = None
        self._artop_attributeDef = []
        self._artop_decomposition = []
        self._artop_relation = []
        self._artop_restriction = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_attributeDef': '"FM-ATTRIBUTE-DEF"', 
         '_artop_decomposition': '"FM-FEATURE-DECOMPOSITION"', 
         '_artop_relation': '"FM-FEATURE-RELATION"', 
         '_artop_restriction': '"FM-FEATURE-RESTRICTION"'})

    @property
    def maximumIntendedBindingTime_(self):
        return self._artop_maximumIntendedBindingTime

    @property
    def minimumIntendedBindingTime_(self):
        return self._artop_minimumIntendedBindingTime

    @property
    def attributeDefs_FMAttributeDef(self):
        return self._artop_attributeDef

    @property
    def decompositions_FMFeatureDecomposition(self):
        return self._artop_decomposition

    @property
    def relations_FMFeatureRelation(self):
        return self._artop_relation

    @property
    def restrictions_FMFeatureRestriction(self):
        return self._artop_restriction
