# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InterpolationRoutineMappingSet.py
from .ARElement import ARElement

class InterpolationRoutineMappingSet(ARElement):

    def __init__(self):
        super().__init__()
        from .InterpolationRoutineMapping import InterpolationRoutineMapping
        self._artop_interpolationRoutineMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_interpolationRoutineMapping": "INTERPOLATION-ROUTINE-MAPPING"})

    @property
    def interpolationRoutineMappings_InterpolationRoutineMapping(self):
        return self._artop_interpolationRoutineMapping
