# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McDataAccessDetails.py
from .ARObject import ARObject

class McDataAccessDetails(ARObject):

    def __init__(self):
        super().__init__()
        from .McDataInstance import McDataInstance
        from .RteEventInEcuInstanceRef import RteEventInEcuInstanceRef
        from .VariableAccessInEcuInstanceRef import VariableAccessInEcuInstanceRef
        self._artop_mcDataInstance = None
        self._artop_rteEventIref = []
        self._artop_variableAccessIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_mcDataInstance':"MC-DATA-INSTANCE", 
         '_artop_rteEventIref':"RTE-EVENT-IN-ECU-INSTANCE-REF-IREF", 
         '_artop_variableAccessIref':"VARIABLE-ACCESS-IN-ECU-INSTANCE-REF-IREF"})

    @property
    def ref_mcDataInstance_(self):
        return self._artop_mcDataInstance

    @property
    def mcDataInstance_(self):
        if self._artop_mcDataInstance is not None:
            if hasattr(self._artop_mcDataInstance, "uuid"):
                return self._artop_mcDataInstance.uuid
        return

    @property
    def rteEvents_RteEventInEcuInstanceRef(self):
        return self._artop_rteEventIref

    @property
    def variableAccess_VariableAccessInEcuInstanceRef(self):
        return self._artop_variableAccessIref
