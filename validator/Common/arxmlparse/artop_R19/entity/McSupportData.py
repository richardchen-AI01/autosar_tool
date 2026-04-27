# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McSupportData.py
from .ARObject import ARObject

class McSupportData(ARObject):

    def __init__(self):
        super().__init__()
        from .Implementation import Implementation
        from .McSwEmulationMethodSupport import McSwEmulationMethodSupport
        from .McDataInstance import McDataInstance
        from .SwSystemconstantValueSet import SwSystemconstantValueSet
        from .RptSupportData import RptSupportData
        self._artop_implementation = None
        self._artop_emulationSupport = []
        self._artop_mcParameterInstance = []
        self._artop_mcVariableInstance = []
        self._artop_measurableSystemConstantValuesRef = []
        self._artop_rptSupportData = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_implementation': '"IMPLEMENTATION"', 
         '_artop_emulationSupport': '"MC-SW-EMULATION-METHOD-SUPPORT"', 
         '_artop_mcParameterInstance': '"MC-DATA-INSTANCE"', 
         '_artop_mcVariableInstance': '"MC-DATA-INSTANCE"', 
         '_artop_measurableSystemConstantValuesRef': '"SW-SYSTEMCONSTANT-VALUE-SET"', 
         '_artop_rptSupportData': '"RPT-SUPPORT-DATA"'})

    @property
    def ref_implementation_(self):
        return self._artop_implementation

    @property
    def implementation_(self):
        if self._artop_implementation is not None:
            if hasattr(self._artop_implementation, "uuid"):
                return self._artop_implementation.uuid
        return

    @property
    def emulationSupports_McSwEmulationMethodSupport(self):
        return self._artop_emulationSupport

    @property
    def mcParameterInstances_McDataInstance(self):
        return self._artop_mcParameterInstance

    @property
    def mcVariableInstances_McDataInstance(self):
        return self._artop_mcVariableInstance

    @property
    def ref_measurableSystemConstantValues_(self):
        return self._artop_measurableSystemConstantValuesRef

    @property
    def measurableSystemConstantValues_(self):
        return self._artop_measurableSystemConstantValuesRef

    @property
    def ref_rptSupportData_(self):
        return self._artop_rptSupportData

    @property
    def rptSupportData_(self):
        if self._artop_rptSupportData is not None:
            if hasattr(self._artop_rptSupportData, "uuid"):
                return self._artop_rptSupportData.uuid
        return
