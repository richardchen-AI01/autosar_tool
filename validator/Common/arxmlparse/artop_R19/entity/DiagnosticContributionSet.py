# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticContributionSet.py
from .ARElement import ARElement

class DiagnosticContributionSet(ARElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticCommonProps import DiagnosticCommonProps
        from .EcuInstance import EcuInstance
        from .DiagnosticCommonElementRefConditional import DiagnosticCommonElementRefConditional
        from .DiagnosticServiceTableRefConditional import DiagnosticServiceTableRefConditional
        self._artop_commonProperties = None
        self._artop_ecuInstanceRef = []
        self._artop_element = []
        self._artop_serviceTable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_commonProperties': '"DIAGNOSTIC-COMMON-PROPS"', 
         '_artop_ecuInstanceRef': '"ECU-INSTANCE"', 
         '_artop_element': '"DIAGNOSTIC-COMMON-ELEMENT-REF-CONDITIONAL"', 
         '_artop_serviceTable': '"DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL"'})

    @property
    def ref_commonProperties_(self):
        return self._artop_commonProperties

    @property
    def commonProperties_(self):
        if self._artop_commonProperties is not None:
            if hasattr(self._artop_commonProperties, "uuid"):
                return self._artop_commonProperties.uuid
        return

    @property
    def ref_ecuInstances_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstances_(self):
        return self._artop_ecuInstanceRef

    @property
    def elements_DiagnosticCommonElementRefConditional(self):
        return self._artop_element

    @property
    def serviceTables_DiagnosticServiceTableRefConditional(self):
        return self._artop_serviceTable
