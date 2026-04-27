# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McGroup.py
from .ARElement import ARElement

class McGroup(ARElement):

    def __init__(self):
        super().__init__()
        from .McGroupDataRefSet import McGroupDataRefSet
        from .McFunction import McFunction
        self._artop_subGroupRef = []
        self._artop_refCalprmSet = None
        self._artop_refMeasurementSet = None
        self._artop_mcFunctionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_subGroupRef': '"MC-GROUP"', 
         '_artop_refCalprmSet': '"MC-GROUP-DATA-REF-SET"', 
         '_artop_refMeasurementSet': '"MC-GROUP-DATA-REF-SET"', 
         '_artop_mcFunctionRef': '"MC-FUNCTION"'})

    @property
    def ref_subGroups_(self):
        return self._artop_subGroupRef

    @property
    def subGroups_(self):
        return self._artop_subGroupRef

    @property
    def ref_refCalprmSet_(self):
        return self._artop_refCalprmSet

    @property
    def refCalprmSet_(self):
        if self._artop_refCalprmSet is not None:
            if hasattr(self._artop_refCalprmSet, "uuid"):
                return self._artop_refCalprmSet.uuid
        return

    @property
    def ref_refMeasurementSet_(self):
        return self._artop_refMeasurementSet

    @property
    def refMeasurementSet_(self):
        if self._artop_refMeasurementSet is not None:
            if hasattr(self._artop_refMeasurementSet, "uuid"):
                return self._artop_refMeasurementSet.uuid
        return

    @property
    def ref_mcFunctions_(self):
        return self._artop_mcFunctionRef

    @property
    def mcFunctions_(self):
        return self._artop_mcFunctionRef
