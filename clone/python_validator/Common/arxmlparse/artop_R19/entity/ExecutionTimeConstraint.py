# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExecutionTimeConstraint.py
from .TimingConstraint import TimingConstraint

class ExecutionTimeConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .ComponentInCompositionInstanceRef import ComponentInCompositionInstanceRef
        from .ExecutableEntity import ExecutableEntity
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_executionTimeType = None
        self._artop_componentIref = None
        self._artop_executableRef = None
        self._artop_maximum = None
        self._artop_minimum = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_componentIref': '"COMPONENT-IN-COMPOSITION-INSTANCE-REF-IREF"', 
         '_artop_executableRef': '"EXECUTABLE-ENTITY"', 
         '_artop_maximum': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_minimum': '"MULTIDIMENSIONAL-TIME"'})

    @property
    def executionTimeType_(self):
        return self._artop_executionTimeType

    @property
    def ref_component_(self):
        return self._artop_componentIref

    @property
    def component_(self):
        if self._artop_componentIref is not None:
            if hasattr(self._artop_componentIref, "uuid"):
                return self._artop_componentIref.uuid
        return

    @property
    def ref_executable_(self):
        return self._artop_executableRef

    @property
    def executable_(self):
        if self._artop_executableRef is not None:
            if hasattr(self._artop_executableRef, "uuid"):
                return self._artop_executableRef.uuid
        return

    @property
    def ref_maximum_(self):
        return self._artop_maximum

    @property
    def maximum_(self):
        if self._artop_maximum is not None:
            if hasattr(self._artop_maximum, "uuid"):
                return self._artop_maximum.uuid
        return

    @property
    def ref_minimum_(self):
        return self._artop_minimum

    @property
    def minimum_(self):
        if self._artop_minimum is not None:
            if hasattr(self._artop_minimum, "uuid"):
                return self._artop_minimum.uuid
        return
