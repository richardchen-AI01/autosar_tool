# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ArbitraryEventTriggering.py
from .EventTriggeringConstraint import EventTriggeringConstraint

class ArbitraryEventTriggering(EventTriggeringConstraint):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        from .ConfidenceInterval import ConfidenceInterval
        self._artop_timeValue = []
        self._artop_timeValue = []
        self._artop_confidenceInterval = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_timeValue':"MULTIDIMENSIONAL-TIME", 
         '_artop_timeValue':"MULTIDIMENSIONAL-TIME", 
         '_artop_confidenceInterval':"CONFIDENCE-INTERVAL"})

    @property
    def minimumDistances_MultidimensionalTime(self):
        return self._artop_timeValue

    @property
    def maximumDistances_MultidimensionalTime(self):
        return self._artop_timeValue

    @property
    def confidenceIntervals_ConfidenceInterval(self):
        return self._artop_confidenceInterval
