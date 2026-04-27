# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConfidenceInterval.py
from .ARObject import ARObject

class ConfidenceInterval(ARObject):

    def __init__(self):
        super().__init__()
        from .ArbitraryEventTriggering import ArbitraryEventTriggering
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_propability = None
        self._artop_arbitraryEventTriggering = None
        self._artop_lowerBound = None
        self._artop_upperBound = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_arbitraryEventTriggering':"ARBITRARY-EVENT-TRIGGERING", 
         '_artop_lowerBound':"MULTIDIMENSIONAL-TIME", 
         '_artop_upperBound':"MULTIDIMENSIONAL-TIME"})

    @property
    def propability_(self):
        if self._artop_propability:
            return float(self._artop_propability)
        return self._artop_propability

    @property
    def ref_arbitraryEventTriggering_(self):
        return self._artop_arbitraryEventTriggering

    @property
    def arbitraryEventTriggering_(self):
        if self._artop_arbitraryEventTriggering is not None:
            if hasattr(self._artop_arbitraryEventTriggering, "uuid"):
                return self._artop_arbitraryEventTriggering.uuid
        return

    @property
    def ref_lowerBound_(self):
        return self._artop_lowerBound

    @property
    def lowerBound_(self):
        if self._artop_lowerBound is not None:
            if hasattr(self._artop_lowerBound, "uuid"):
                return self._artop_lowerBound.uuid
        return

    @property
    def ref_upperBound_(self):
        return self._artop_upperBound

    @property
    def upperBound_(self):
        if self._artop_upperBound is not None:
            if hasattr(self._artop_upperBound, "uuid"):
                return self._artop_upperBound.uuid
        return
