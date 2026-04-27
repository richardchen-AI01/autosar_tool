# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SporadicEventTriggering.py
from .EventTriggeringConstraint import EventTriggeringConstraint

class SporadicEventTriggering(EventTriggeringConstraint):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_minimumInterArrivalTime = None
        self._artop_maximumInterArrivalTime = None
        self._artop_jitter = None
        self._artop_period = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_minimumInterArrivalTime': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_maximumInterArrivalTime': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_jitter': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_period': '"MULTIDIMENSIONAL-TIME"'})

    @property
    def ref_minimumInterArrivalTime_(self):
        return self._artop_minimumInterArrivalTime

    @property
    def minimumInterArrivalTime_(self):
        if self._artop_minimumInterArrivalTime is not None:
            if hasattr(self._artop_minimumInterArrivalTime, "uuid"):
                return self._artop_minimumInterArrivalTime.uuid
        return

    @property
    def ref_maximumInterArrivalTime_(self):
        return self._artop_maximumInterArrivalTime

    @property
    def maximumInterArrivalTime_(self):
        if self._artop_maximumInterArrivalTime is not None:
            if hasattr(self._artop_maximumInterArrivalTime, "uuid"):
                return self._artop_maximumInterArrivalTime.uuid
        return

    @property
    def ref_jitter_(self):
        return self._artop_jitter

    @property
    def jitter_(self):
        if self._artop_jitter is not None:
            if hasattr(self._artop_jitter, "uuid"):
                return self._artop_jitter.uuid
        return

    @property
    def ref_period_(self):
        return self._artop_period

    @property
    def period_(self):
        if self._artop_period is not None:
            if hasattr(self._artop_period, "uuid"):
                return self._artop_period.uuid
        return
