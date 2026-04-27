# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InterpolationRoutine.py
from .ARObject import ARObject

class InterpolationRoutine(ARObject):

    def __init__(self):
        super().__init__()
        from .InterpolationRoutineMapping import InterpolationRoutineMapping
        from .BswModuleEntry import BswModuleEntry
        self._artop_shortLabel = None
        self._artop_isDefault = None
        self._artop_interpolationRoutineMapping = None
        self._artop_interpolationRoutineRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_interpolationRoutineMapping':"INTERPOLATION-ROUTINE-MAPPING", 
         '_artop_interpolationRoutineRef':"BSW-MODULE-ENTRY"})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def isDefault_(self):
        if self._artop_isDefault:
            if self._artop_isDefault == "true":
                return True
            return False
        else:
            return self._artop_isDefault

    @property
    def ref_interpolationRoutineMapping_(self):
        return self._artop_interpolationRoutineMapping

    @property
    def interpolationRoutineMapping_(self):
        if self._artop_interpolationRoutineMapping is not None:
            if hasattr(self._artop_interpolationRoutineMapping, "uuid"):
                return self._artop_interpolationRoutineMapping.uuid
        return

    @property
    def ref_interpolationRoutine_(self):
        return self._artop_interpolationRoutineRef

    @property
    def interpolationRoutine_(self):
        if self._artop_interpolationRoutineRef is not None:
            if hasattr(self._artop_interpolationRoutineRef, "uuid"):
                return self._artop_interpolationRoutineRef.uuid
        return
