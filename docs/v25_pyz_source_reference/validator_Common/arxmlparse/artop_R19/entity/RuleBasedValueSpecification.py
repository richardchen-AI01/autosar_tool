# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RuleBasedValueSpecification.py
from .ARObject import ARObject

class RuleBasedValueSpecification(ARObject):

    def __init__(self):
        super().__init__()
        from .RuleArguments import RuleArguments
        self._artop_rule = None
        self._artop_maxSizeToFill = None
        self._artop_arguments = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_arguments": "RULE-ARGUMENTS"})

    @property
    def rule_(self):
        return self._artop_rule

    @property
    def maxSizeToFill_(self):
        if self._artop_maxSizeToFill:
            return int(self._artop_maxSizeToFill)
        return self._artop_maxSizeToFill

    @property
    def arguments_RuleArguments(self):
        return self._artop_arguments
