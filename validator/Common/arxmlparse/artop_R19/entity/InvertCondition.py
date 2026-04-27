# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InvertCondition.py
from .AbstractCondition import AbstractCondition

class InvertCondition(AbstractCondition):

    def __init__(self):
        super().__init__()
        from .AbstractCondition import AbstractCondition
        self._artop_condition = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_condition": "ABSTRACT-CONDITION"})

    @property
    def ref_condition_(self):
        return self._artop_condition

    @property
    def condition_(self):
        if self._artop_condition is not None:
            if hasattr(self._artop_condition, "uuid"):
                return self._artop_condition.uuid
        return
