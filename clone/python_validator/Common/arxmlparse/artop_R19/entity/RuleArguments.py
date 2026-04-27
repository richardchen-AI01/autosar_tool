# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RuleArguments.py
from .ARObject import ARObject

class RuleArguments(ARObject):

    def __init__(self):
        super().__init__()
        from .RuleBasedValueSpecification import RuleBasedValueSpecification
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        from .NumericalOrText import NumericalOrText
        from .VariationPoint import VariationPoint
        self._artop_v = None
        self._artop_vt = None
        self._artop_mixed = None
        self._artop_ruleBasedValueSpecification = None
        self._artop_vf = []
        self._artop_vtf = []
        self._artop_variationPoint = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ruleBasedValueSpecification': '"RULE-BASED-VALUE-SPECIFICATION"', 
         '_artop_vf': '"NUMERICAL-VALUE-VARIATION-POINT"', 
         '_artop_vtf': '"NUMERICAL-OR-TEXT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def v_(self):
        return self._artop_v

    @property
    def vt_(self):
        return self._artop_vt

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_ruleBasedValueSpecification_(self):
        return self._artop_ruleBasedValueSpecification

    @property
    def ruleBasedValueSpecification_(self):
        if self._artop_ruleBasedValueSpecification is not None:
            if hasattr(self._artop_ruleBasedValueSpecification, "uuid"):
                return self._artop_ruleBasedValueSpecification.uuid
        return

    @property
    def vfs_NumericalValueVariationPoint(self):
        return self._artop_vf

    @property
    def vtfs_NumericalOrText(self):
        return self._artop_vtf

    @property
    def variationPoints_VariationPoint(self):
        return self._artop_variationPoint
