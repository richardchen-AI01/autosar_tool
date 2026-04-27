# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\OffsetTimingConstraint.py
from .TimingConstraint import TimingConstraint

class OffsetTimingConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEvent import TimingDescriptionEvent
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_sourceRef = None
        self._artop_targetRef = None
        self._artop_minimum = None
        self._artop_maximum = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_sourceRef': '"TIMING-DESCRIPTION-EVENT"', 
         '_artop_targetRef': '"TIMING-DESCRIPTION-EVENT"', 
         '_artop_minimum': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_maximum': '"MULTIDIMENSIONAL-TIME"'})

    @property
    def ref_source_(self):
        return self._artop_sourceRef

    @property
    def source_(self):
        if self._artop_sourceRef is not None:
            if hasattr(self._artop_sourceRef, "uuid"):
                return self._artop_sourceRef.uuid
        return

    @property
    def ref_target_(self):
        return self._artop_targetRef

    @property
    def target_(self):
        if self._artop_targetRef is not None:
            if hasattr(self._artop_targetRef, "uuid"):
                return self._artop_targetRef.uuid
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

    @property
    def ref_maximum_(self):
        return self._artop_maximum

    @property
    def maximum_(self):
        if self._artop_maximum is not None:
            if hasattr(self._artop_maximum, "uuid"):
                return self._artop_maximum.uuid
        return
