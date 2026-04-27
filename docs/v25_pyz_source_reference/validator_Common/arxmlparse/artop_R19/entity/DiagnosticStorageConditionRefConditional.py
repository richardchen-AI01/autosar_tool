# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticStorageConditionRefConditional.py
from .ARObject import ARObject

class DiagnosticStorageConditionRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticStorageConditionGroup import DiagnosticStorageConditionGroup
        from .DiagnosticStorageCondition import DiagnosticStorageCondition
        from .VariationPoint import VariationPoint
        self._artop_diagnosticStorageConditionGroup = None
        self._artop_diagnosticStorageConditionRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticStorageConditionGroup':"DIAGNOSTIC-STORAGE-CONDITION-GROUP", 
         '_artop_diagnosticStorageConditionRef':"DIAGNOSTIC-STORAGE-CONDITION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticStorageConditionGroup_(self):
        return self._artop_diagnosticStorageConditionGroup

    @property
    def diagnosticStorageConditionGroup_(self):
        if self._artop_diagnosticStorageConditionGroup is not None:
            if hasattr(self._artop_diagnosticStorageConditionGroup, "uuid"):
                return self._artop_diagnosticStorageConditionGroup.uuid
        return

    @property
    def ref_diagnosticStorageCondition_(self):
        return self._artop_diagnosticStorageConditionRef

    @property
    def diagnosticStorageCondition_(self):
        if self._artop_diagnosticStorageConditionRef is not None:
            if hasattr(self._artop_diagnosticStorageConditionRef, "uuid"):
                return self._artop_diagnosticStorageConditionRef.uuid
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
