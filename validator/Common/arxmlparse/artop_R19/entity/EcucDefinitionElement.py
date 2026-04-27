# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucDefinitionElement.py
from .AtpDefinition import AtpDefinition
from .Identifiable import Identifiable

class EcucDefinitionElement(Identifiable, AtpDefinition):

    def __init__(self):
        super().__init__()
        from .Traceable import Traceable
        from .EcucValidationCondition import EcucValidationCondition
        from .EcucConditionSpecification import EcucConditionSpecification
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        self._artop_scope = None
        self._artop_relatedTraceItemRef = None
        self._artop_ecucValidationCond = []
        self._artop_ecucCond = None
        self._artop_lowerMultiplicity = None
        self._artop_upperMultiplicity = None
        self._artop_upperMultiplicityInfinite = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_relatedTraceItemRef': '"TRACEABLE"', 
         '_artop_ecucValidationCond': '"ECUC-VALIDATION-CONDITION"', 
         '_artop_ecucCond': '"ECUC-CONDITION-SPECIFICATION"', 
         '_artop_lowerMultiplicity': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_upperMultiplicity': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_upperMultiplicityInfinite': '"BOOLEAN-VALUE-VARIATION-POINT"'})

    @property
    def scope_(self):
        return self._artop_scope

    @property
    def ref_relatedTraceItem_(self):
        return self._artop_relatedTraceItemRef

    @property
    def relatedTraceItem_(self):
        if self._artop_relatedTraceItemRef is not None:
            if hasattr(self._artop_relatedTraceItemRef, "uuid"):
                return self._artop_relatedTraceItemRef.uuid
        return

    @property
    def ecucValidationConds_EcucValidationCondition(self):
        return self._artop_ecucValidationCond

    @property
    def ref_ecucCond_(self):
        return self._artop_ecucCond

    @property
    def ecucCond_(self):
        if self._artop_ecucCond is not None:
            if hasattr(self._artop_ecucCond, "uuid"):
                return self._artop_ecucCond.uuid
        return

    @property
    def ref_lowerMultiplicity_(self):
        return self._artop_lowerMultiplicity

    @property
    def lowerMultiplicity_(self):
        if self._artop_lowerMultiplicity is not None:
            if hasattr(self._artop_lowerMultiplicity, "uuid"):
                return self._artop_lowerMultiplicity.uuid
        return

    @property
    def ref_upperMultiplicity_(self):
        return self._artop_upperMultiplicity

    @property
    def upperMultiplicity_(self):
        if self._artop_upperMultiplicity is not None:
            if hasattr(self._artop_upperMultiplicity, "uuid"):
                return self._artop_upperMultiplicity.uuid
        return

    @property
    def ref_upperMultiplicityInfinite_(self):
        return self._artop_upperMultiplicityInfinite

    @property
    def upperMultiplicityInfinite_(self):
        if self._artop_upperMultiplicityInfinite is not None:
            if hasattr(self._artop_upperMultiplicityInfinite, "uuid"):
                return self._artop_upperMultiplicityInfinite.uuid
        return
