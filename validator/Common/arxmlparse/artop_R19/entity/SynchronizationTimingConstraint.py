# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SynchronizationTimingConstraint.py
from .TimingConstraint import TimingConstraint

class SynchronizationTimingConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEvent import TimingDescriptionEvent
        from .TimingDescriptionEventChain import TimingDescriptionEventChain
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_eventOccurrenceKind = None
        self._artop_synchronizationConstraintType = None
        self._artop_scopeEventRef = []
        self._artop_scopeRef = []
        self._artop_tolerance = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_scopeEventRef':"TIMING-DESCRIPTION-EVENT", 
         '_artop_scopeRef':"TIMING-DESCRIPTION-EVENT-CHAIN", 
         '_artop_tolerance':"MULTIDIMENSIONAL-TIME"})

    @property
    def eventOccurrenceKind_(self):
        return self._artop_eventOccurrenceKind

    @property
    def synchronizationConstraintType_(self):
        return self._artop_synchronizationConstraintType

    @property
    def ref_scopeEvents_(self):
        return self._artop_scopeEventRef

    @property
    def scopeEvents_(self):
        return self._artop_scopeEventRef

    @property
    def ref_scopes_(self):
        return self._artop_scopeRef

    @property
    def scopes_(self):
        return self._artop_scopeRef

    @property
    def ref_tolerance_(self):
        return self._artop_tolerance

    @property
    def tolerance_(self):
        if self._artop_tolerance is not None:
            if hasattr(self._artop_tolerance, "uuid"):
                return self._artop_tolerance.uuid
        return
