# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConstraintTailoring.py
from .RestrictionWithSeverity import RestrictionWithSeverity
from .DataFormatElementScope import DataFormatElementScope

class ConstraintTailoring(DataFormatElementScope, RestrictionWithSeverity):

    def __init__(self):
        super().__init__()
        from .TraceableText import TraceableText
        self._artop_constraintRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_constraintRef": "TRACEABLE-TEXT"})

    @property
    def ref_constraint_(self):
        return self._artop_constraintRef

    @property
    def constraint_(self):
        if self._artop_constraintRef is not None:
            if hasattr(self._artop_constraintRef, "uuid"):
                return self._artop_constraintRef.uuid
        return
