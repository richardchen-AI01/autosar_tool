# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConcretePatternEventTriggering.py
from .EventTriggeringConstraint import EventTriggeringConstraint

class ConcretePatternEventTriggering(EventTriggeringConstraint):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_patternJitter = None
        self._artop_patternPeriod = None
        self._artop_timeValue = []
        self._artop_patternLength = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_patternJitter': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_patternPeriod': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_timeValue': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_patternLength': '"MULTIDIMENSIONAL-TIME"'})

    @property
    def ref_patternJitter_(self):
        return self._artop_patternJitter

    @property
    def patternJitter_(self):
        if self._artop_patternJitter is not None:
            if hasattr(self._artop_patternJitter, "uuid"):
                return self._artop_patternJitter.uuid
        return

    @property
    def ref_patternPeriod_(self):
        return self._artop_patternPeriod

    @property
    def patternPeriod_(self):
        if self._artop_patternPeriod is not None:
            if hasattr(self._artop_patternPeriod, "uuid"):
                return self._artop_patternPeriod.uuid
        return

    @property
    def offsets_MultidimensionalTime(self):
        return self._artop_timeValue

    @property
    def ref_patternLength_(self):
        return self._artop_patternLength

    @property
    def patternLength_(self):
        if self._artop_patternLength is not None:
            if hasattr(self._artop_patternLength, "uuid"):
                return self._artop_patternLength.uuid
        return
