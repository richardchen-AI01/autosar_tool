# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FMFormulaByFeaturesAndAttributes.py
from .FormulaExpression import FormulaExpression

class FMFormulaByFeaturesAndAttributes(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .FMAttributeDef import FMAttributeDef
        from .FMFeature import FMFeature
        self._artop_attributeRef = []
        self._artop_featureRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_attributeRef':"FM-ATTRIBUTE-DEF", 
         '_artop_featureRef':"FM-FEATURE"})

    @property
    def ref_attributes_(self):
        return self._artop_attributeRef

    @property
    def attributes_(self):
        return self._artop_attributeRef

    @property
    def ref_features_(self):
        return self._artop_featureRef

    @property
    def features_(self):
        return self._artop_featureRef
