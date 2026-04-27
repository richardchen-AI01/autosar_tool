# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InterpolationRoutineMapping.py
from .ARObject import ARObject

class InterpolationRoutineMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .InterpolationRoutineMappingSet import InterpolationRoutineMappingSet
        from .InterpolationRoutine import InterpolationRoutine
        from .SwRecordLayout import SwRecordLayout
        self._artop_interpolationRoutineMappingSet = None
        self._artop_interpolationRoutine = []
        self._artop_swRecordLayoutRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_interpolationRoutineMappingSet':"INTERPOLATION-ROUTINE-MAPPING-SET", 
         '_artop_interpolationRoutine':"INTERPOLATION-ROUTINE", 
         '_artop_swRecordLayoutRef':"SW-RECORD-LAYOUT"})

    @property
    def ref_interpolationRoutineMappingSet_(self):
        return self._artop_interpolationRoutineMappingSet

    @property
    def interpolationRoutineMappingSet_(self):
        if self._artop_interpolationRoutineMappingSet is not None:
            if hasattr(self._artop_interpolationRoutineMappingSet, "uuid"):
                return self._artop_interpolationRoutineMappingSet.uuid
        return

    @property
    def interpolationRoutines_InterpolationRoutine(self):
        return self._artop_interpolationRoutine

    @property
    def ref_swRecordLayout_(self):
        return self._artop_swRecordLayoutRef

    @property
    def swRecordLayout_(self):
        if self._artop_swRecordLayoutRef is not None:
            if hasattr(self._artop_swRecordLayoutRef, "uuid"):
                return self._artop_swRecordLayoutRef.uuid
        return
