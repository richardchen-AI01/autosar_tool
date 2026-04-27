# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnableConditionRefConditional.py
from .ARObject import ARObject

class DiagnosticEnableConditionRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnableConditionGroup import DiagnosticEnableConditionGroup
        from .DiagnosticEnableCondition import DiagnosticEnableCondition
        from .VariationPoint import VariationPoint
        self._artop_diagnosticEnableConditionGroup = None
        self._artop_diagnosticEnableConditionRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticEnableConditionGroup':"DIAGNOSTIC-ENABLE-CONDITION-GROUP", 
         '_artop_diagnosticEnableConditionRef':"DIAGNOSTIC-ENABLE-CONDITION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticEnableConditionGroup_(self):
        return self._artop_diagnosticEnableConditionGroup

    @property
    def diagnosticEnableConditionGroup_(self):
        if self._artop_diagnosticEnableConditionGroup is not None:
            if hasattr(self._artop_diagnosticEnableConditionGroup, "uuid"):
                return self._artop_diagnosticEnableConditionGroup.uuid
        return

    @property
    def ref_diagnosticEnableCondition_(self):
        return self._artop_diagnosticEnableConditionRef

    @property
    def diagnosticEnableCondition_(self):
        if self._artop_diagnosticEnableConditionRef is not None:
            if hasattr(self._artop_diagnosticEnableConditionRef, "uuid"):
                return self._artop_diagnosticEnableConditionRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
