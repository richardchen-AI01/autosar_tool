# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClassContentConditional.py
from .Identifiable import Identifiable

class ClassContentConditional(Identifiable):

    def __init__(self):
        super().__init__()
        from .ClassTailoring import ClassTailoring
        from .AbstractCondition import AbstractCondition
        from .AttributeTailoring import AttributeTailoring
        from .ConstraintTailoring import ConstraintTailoring
        from .SdgTailoring import SdgTailoring
        self._artop_classTailoring = None
        self._artop_condition = None
        self._artop_attributeTailoring = []
        self._artop_constraintTailoring = []
        self._artop_sdgTailoring = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_classTailoring': '"CLASS-TAILORING"', 
         '_artop_condition': '"ABSTRACT-CONDITION"', 
         '_artop_attributeTailoring': '"ATTRIBUTE-TAILORING"', 
         '_artop_constraintTailoring': '"CONSTRAINT-TAILORING"', 
         '_artop_sdgTailoring': '"SDG-TAILORING"'})

    @property
    def ref_classTailoring_(self):
        return self._artop_classTailoring

    @property
    def classTailoring_(self):
        if self._artop_classTailoring is not None:
            if hasattr(self._artop_classTailoring, "uuid"):
                return self._artop_classTailoring.uuid
        return

    @property
    def ref_condition_(self):
        return self._artop_condition

    @property
    def condition_(self):
        if self._artop_condition is not None:
            if hasattr(self._artop_condition, "uuid"):
                return self._artop_condition.uuid
        return

    @property
    def attributeTailorings_AttributeTailoring(self):
        return self._artop_attributeTailoring

    @property
    def constraintTailorings_ConstraintTailoring(self):
        return self._artop_constraintTailoring

    @property
    def sdgTailorings_SdgTailoring(self):
        return self._artop_sdgTailoring
