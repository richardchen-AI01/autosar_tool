# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McFunction.py
from .ARElement import ARElement

class McFunction(ARElement):

    def __init__(self):
        super().__init__()
        from .McFunctionDataRefSet import McFunctionDataRefSet
        self._artop_defCalprmSet = None
        self._artop_refCalprmSet = None
        self._artop_inMeasurementSet = None
        self._artop_outMeasurmentSet = None
        self._artop_locMeasurementSet = None
        self._artop_outMeasurementSet = None
        self._artop_subFunctionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_defCalprmSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_refCalprmSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_inMeasurementSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_outMeasurmentSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_locMeasurementSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_outMeasurementSet': '"MC-FUNCTION-DATA-REF-SET"', 
         '_artop_subFunctionRef': '"MC-FUNCTION"'})

    @property
    def ref_defCalprmSet_(self):
        return self._artop_defCalprmSet

    @property
    def defCalprmSet_(self):
        if self._artop_defCalprmSet is not None:
            if hasattr(self._artop_defCalprmSet, "uuid"):
                return self._artop_defCalprmSet.uuid
        return

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
    def ref_inMeasurementSet_(self):
        return self._artop_inMeasurementSet

    @property
    def inMeasurementSet_(self):
        if self._artop_inMeasurementSet is not None:
            if hasattr(self._artop_inMeasurementSet, "uuid"):
                return self._artop_inMeasurementSet.uuid
        return

    @property
    def ref_outMeasurmentSet_(self):
        return self._artop_outMeasurmentSet

    @property
    def outMeasurmentSet_(self):
        if self._artop_outMeasurmentSet is not None:
            if hasattr(self._artop_outMeasurmentSet, "uuid"):
                return self._artop_outMeasurmentSet.uuid
        return

    @property
    def ref_locMeasurementSet_(self):
        return self._artop_locMeasurementSet

    @property
    def locMeasurementSet_(self):
        if self._artop_locMeasurementSet is not None:
            if hasattr(self._artop_locMeasurementSet, "uuid"):
                return self._artop_locMeasurementSet.uuid
        return

    @property
    def ref_outMeasurementSet_(self):
        return self._artop_outMeasurementSet

    @property
    def outMeasurementSet_(self):
        if self._artop_outMeasurementSet is not None:
            if hasattr(self._artop_outMeasurementSet, "uuid"):
                return self._artop_outMeasurementSet.uuid
        return

    @property
    def ref_subFunctions_(self):
        return self._artop_subFunctionRef

    @property
    def subFunctions_(self):
        return self._artop_subFunctionRef
