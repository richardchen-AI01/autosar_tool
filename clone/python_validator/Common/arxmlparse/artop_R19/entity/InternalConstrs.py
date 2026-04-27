# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InternalConstrs.py
from .ARObject import ARObject

class InternalConstrs(ARObject):

    def __init__(self):
        super().__init__()
        from .DataConstrRule import DataConstrRule
        from .LimitValueVariationPoint import LimitValueVariationPoint
        from .ScaleConstr import ScaleConstr
        self._artop_maxGradient = None
        self._artop_maxDiff = None
        self._artop_monotony = None
        self._artop_dataConstrRule = None
        self._artop_lowerLimit = None
        self._artop_upperLimit = None
        self._artop_scaleConstr = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataConstrRule': '"DATA-CONSTR-RULE"', 
         '_artop_lowerLimit': '"LIMIT"', 
         '_artop_upperLimit': '"LIMIT"', 
         '_artop_scaleConstr': '"SCALE-CONSTR"'})

    @property
    def maxGradient_(self):
        return self._artop_maxGradient

    @property
    def maxDiff_(self):
        return self._artop_maxDiff

    @property
    def monotony_(self):
        return self._artop_monotony

    @property
    def ref_dataConstrRule_(self):
        return self._artop_dataConstrRule

    @property
    def dataConstrRule_(self):
        if self._artop_dataConstrRule is not None:
            if hasattr(self._artop_dataConstrRule, "uuid"):
                return self._artop_dataConstrRule.uuid
        return

    @property
    def ref_lowerLimit_(self):
        return self._artop_lowerLimit

    @property
    def lowerLimit_(self):
        if self._artop_lowerLimit is not None:
            if hasattr(self._artop_lowerLimit, "uuid"):
                return self._artop_lowerLimit.uuid
        return

    @property
    def ref_upperLimit_(self):
        return self._artop_upperLimit

    @property
    def upperLimit_(self):
        if self._artop_upperLimit is not None:
            if hasattr(self._artop_upperLimit, "uuid"):
                return self._artop_upperLimit.uuid
        return

    @property
    def scaleConstrs_ScaleConstr(self):
        return self._artop_scaleConstr
