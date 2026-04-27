# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompositeValueSpecification.py
from .ValueSpecification import ValueSpecification

class CompositeValueSpecification(ValueSpecification):

    def __init__(self):
        super().__init__()
        from .CompositeRuleBasedValueSpecification import CompositeRuleBasedValueSpecification
        self._artop_compositeRuleBasedValueSpecification = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compositeRuleBasedValueSpecification": "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION"})

    @property
    def ref_compositeRuleBasedValueSpecification_(self):
        return self._artop_compositeRuleBasedValueSpecification

    @property
    def compositeRuleBasedValueSpecification_(self):
        if self._artop_compositeRuleBasedValueSpecification is not None:
            if hasattr(self._artop_compositeRuleBasedValueSpecification, "uuid"):
                return self._artop_compositeRuleBasedValueSpecification.uuid
        return
