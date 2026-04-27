# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LatencyTimingConstraint.py
from .TimingConstraint import TimingConstraint

class LatencyTimingConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEventChain import TimingDescriptionEventChain
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_latencyConstraintType = None
        self._artop_scopeRef = None
        self._artop_minimum = None
        self._artop_maximum = None
        self._artop_nominal = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_scopeRef': '"TIMING-DESCRIPTION-EVENT-CHAIN"', 
         '_artop_minimum': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_maximum': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_nominal': '"MULTIDIMENSIONAL-TIME"'})

    @property
    def latencyConstraintType_(self):
        return self._artop_latencyConstraintType

    @property
    def ref_scope_(self):
        return self._artop_scopeRef

    @property
    def scope_(self):
        if self._artop_scopeRef is not None:
            if hasattr(self._artop_scopeRef, "uuid"):
                return self._artop_scopeRef.uuid
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

    @property
    def ref_nominal_(self):
        return self._artop_nominal

    @property
    def nominal_(self):
        if self._artop_nominal is not None:
            if hasattr(self._artop_nominal, "uuid"):
                return self._artop_nominal.uuid
        return
