# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticCommonElementRefConditional.py
from .ARObject import ARObject

class DiagnosticCommonElementRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticContributionSet import DiagnosticContributionSet
        from .DiagnosticCommonElement import DiagnosticCommonElement
        from .VariationPoint import VariationPoint
        self._artop_diagnosticContributionSet = None
        self._artop_diagnosticCommonElementRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticContributionSet':"DIAGNOSTIC-CONTRIBUTION-SET", 
         '_artop_diagnosticCommonElementRef':"DIAGNOSTIC-COMMON-ELEMENT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticContributionSet_(self):
        return self._artop_diagnosticContributionSet

    @property
    def diagnosticContributionSet_(self):
        if self._artop_diagnosticContributionSet is not None:
            if hasattr(self._artop_diagnosticContributionSet, "uuid"):
                return self._artop_diagnosticContributionSet.uuid
        return

    @property
    def ref_diagnosticCommonElement_(self):
        return self._artop_diagnosticCommonElementRef

    @property
    def diagnosticCommonElement_(self):
        if self._artop_diagnosticCommonElementRef is not None:
            if hasattr(self._artop_diagnosticCommonElementRef, "uuid"):
                return self._artop_diagnosticCommonElementRef.uuid
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
