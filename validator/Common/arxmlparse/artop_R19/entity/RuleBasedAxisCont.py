# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RuleBasedAxisCont.py
from .ARObject import ARObject

class RuleBasedAxisCont(ARObject):

    def __init__(self):
        super().__init__()
        from .ApplicationRuleBasedValueSpecification import ApplicationRuleBasedValueSpecification
        from .Unit import Unit
        from .ValueList import ValueList
        from .RuleBasedValueSpecification import RuleBasedValueSpecification
        self._artop_category = None
        self._artop_swAxisIndex = None
        self._artop_applicationRuleBasedValueSpecification = None
        self._artop_unitRef = None
        self._artop_swArraysize = None
        self._artop_ruleBasedValues = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_applicationRuleBasedValueSpecification': '"APPLICATION-RULE-BASED-VALUE-SPECIFICATION"', 
         '_artop_unitRef': '"UNIT"', 
         '_artop_swArraysize': '"VALUE-LIST"', 
         '_artop_ruleBasedValues': '"RULE-BASED-VALUE-SPECIFICATION"'})

    @property
    def category_(self):
        return self._artop_category

    @property
    def swAxisIndex_(self):
        return self._artop_swAxisIndex

    @property
    def ref_applicationRuleBasedValueSpecification_(self):
        return self._artop_applicationRuleBasedValueSpecification

    @property
    def applicationRuleBasedValueSpecification_(self):
        if self._artop_applicationRuleBasedValueSpecification is not None:
            if hasattr(self._artop_applicationRuleBasedValueSpecification, "uuid"):
                return self._artop_applicationRuleBasedValueSpecification.uuid
        return

    @property
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

    @property
    def ref_swArraysize_(self):
        return self._artop_swArraysize

    @property
    def swArraysize_(self):
        if self._artop_swArraysize is not None:
            if hasattr(self._artop_swArraysize, "uuid"):
                return self._artop_swArraysize.uuid
        return

    @property
    def ref_ruleBasedValues_(self):
        return self._artop_ruleBasedValues

    @property
    def ruleBasedValues_(self):
        if self._artop_ruleBasedValues is not None:
            if hasattr(self._artop_ruleBasedValues, "uuid"):
                return self._artop_ruleBasedValues.uuid
        return
