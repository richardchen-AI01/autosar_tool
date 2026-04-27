# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EOCExecutableEntityRefGroup.py
from .EOCExecutableEntityRefAbstract import EOCExecutableEntityRefAbstract

class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEventChain import TimingDescriptionEventChain
        from .EOCExecutableEntityRefAbstract import EOCExecutableEntityRefAbstract
        from .TimingDescriptionEvent import TimingDescriptionEvent
        self._artop_maxCycles = None
        self._artop_maxSlots = None
        self._artop_letIntervalRef = []
        self._artop_nestedElementRef = []
        self._artop_successorRef = []
        self._artop_triggeringEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_letIntervalRef': '"TIMING-DESCRIPTION-EVENT-CHAIN"', 
         '_artop_nestedElementRef': '"EOC-EXECUTABLE-ENTITY-REF-ABSTRACT"', 
         '_artop_successorRef': '"EOC-EXECUTABLE-ENTITY-REF-ABSTRACT"', 
         '_artop_triggeringEventRef': '"TIMING-DESCRIPTION-EVENT"'})

    @property
    def maxCycles_(self):
        if self._artop_maxCycles:
            return int(self._artop_maxCycles)
        return self._artop_maxCycles

    @property
    def maxSlots_(self):
        if self._artop_maxSlots:
            return int(self._artop_maxSlots)
        return self._artop_maxSlots

    @property
    def ref_letIntervals_(self):
        return self._artop_letIntervalRef

    @property
    def letIntervals_(self):
        return self._artop_letIntervalRef

    @property
    def ref_nestedElements_(self):
        return self._artop_nestedElementRef

    @property
    def nestedElements_(self):
        return self._artop_nestedElementRef

    @property
    def ref_successors_(self):
        return self._artop_successorRef

    @property
    def successors_(self):
        return self._artop_successorRef

    @property
    def ref_triggeringEvent_(self):
        return self._artop_triggeringEventRef

    @property
    def triggeringEvent_(self):
        if self._artop_triggeringEventRef is not None:
            if hasattr(self._artop_triggeringEventRef, "uuid"):
                return self._artop_triggeringEventRef.uuid
        return
