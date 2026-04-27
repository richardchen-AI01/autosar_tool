# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDebounceAlgorithmProps.py
from .Referrable import Referrable

class DiagnosticDebounceAlgorithmProps(Referrable):

    def __init__(self):
        super().__init__()
        from .DiagnosticCommonPropsContent import DiagnosticCommonPropsContent
        from .DiagEventDebounceAlgorithm import DiagEventDebounceAlgorithm
        from .DiagnosticDebounceBehaviorEnumValueVariationPoint import DiagnosticDebounceBehaviorEnumValueVariationPoint
        self._artop_debounceCounterStorage = None
        self._artop_diagnosticCommonPropsContent = None
        self._artop_debounceAlgorithm = None
        self._artop_debounceBehavior = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticCommonPropsContent':"DIAGNOSTIC-COMMON-PROPS-CONTENT", 
         '_artop_debounceAlgorithm':"DIAG-EVENT-DEBOUNCE-ALGORITHM", 
         '_artop_debounceBehavior':"DIAGNOSTIC-DEBOUNCE-BEHAVIOR-ENUM-VALUE-VARIATION-POINT"})

    @property
    def debounceCounterStorage_(self):
        if self._artop_debounceCounterStorage:
            if self._artop_debounceCounterStorage == "true":
                return True
            return False
        else:
            return self._artop_debounceCounterStorage

    @property
    def ref_diagnosticCommonPropsContent_(self):
        return self._artop_diagnosticCommonPropsContent

    @property
    def diagnosticCommonPropsContent_(self):
        if self._artop_diagnosticCommonPropsContent is not None:
            if hasattr(self._artop_diagnosticCommonPropsContent, "uuid"):
                return self._artop_diagnosticCommonPropsContent.uuid
        return

    @property
    def ref_debounceAlgorithm_(self):
        return self._artop_debounceAlgorithm

    @property
    def debounceAlgorithm_(self):
        if self._artop_debounceAlgorithm is not None:
            if hasattr(self._artop_debounceAlgorithm, "uuid"):
                return self._artop_debounceAlgorithm.uuid
        return

    @property
    def ref_debounceBehavior_(self):
        return self._artop_debounceBehavior

    @property
    def debounceBehavior_(self):
        if self._artop_debounceBehavior is not None:
            if hasattr(self._artop_debounceBehavior, "uuid"):
                return self._artop_debounceBehavior.uuid
        return
