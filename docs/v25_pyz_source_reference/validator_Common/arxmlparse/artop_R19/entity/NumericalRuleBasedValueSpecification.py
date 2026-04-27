# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NumericalRuleBasedValueSpecification.py
from .AbstractRuleBasedValueSpecification import AbstractRuleBasedValueSpecification

class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):

    def __init__(self):
        super().__init__()
        from .RuleBasedValueSpecification import RuleBasedValueSpecification
        self._artop_ruleBasedValues = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ruleBasedValues": "RULE-BASED-VALUE-SPECIFICATION"})

    @property
    def ref_ruleBasedValues_(self):
        return self._artop_ruleBasedValues

    @property
    def ruleBasedValues_(self):
        if self._artop_ruleBasedValues is not None:
            if hasattr(self._artop_ruleBasedValues, "uuid"):
                return self._artop_ruleBasedValues.uuid
        return
