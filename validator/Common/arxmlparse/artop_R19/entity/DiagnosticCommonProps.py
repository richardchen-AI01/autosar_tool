# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticCommonProps.py
from .ARObject import ARObject

class DiagnosticCommonProps(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticContributionSet import DiagnosticContributionSet
        from .DiagnosticCommonPropsConditional import DiagnosticCommonPropsConditional
        self._artop_diagnosticContributionSet = None
        self._artop_diagnosticCommonPropsVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticContributionSet':"DIAGNOSTIC-CONTRIBUTION-SET", 
         '_artop_diagnosticCommonPropsVariant':"DIAGNOSTIC-COMMON-PROPS-CONDITIONAL"})

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
    def DiagnosticCommonPropsVariants_DiagnosticCommonPropsConditional(self):
        return self._artop_diagnosticCommonPropsVariant
