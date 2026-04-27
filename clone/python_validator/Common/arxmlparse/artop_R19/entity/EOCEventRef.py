# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EOCEventRef.py
from .EOCExecutableEntityRefAbstract import EOCExecutableEntityRefAbstract

class EOCEventRef(EOCExecutableEntityRefAbstract):

    def __init__(self):
        super().__init__()
        from .BswImplementation import BswImplementation
        from .ComponentInCompositionInstanceRef import ComponentInCompositionInstanceRef
        from .AbstractEvent import AbstractEvent
        from .EOCExecutableEntityRefAbstract import EOCExecutableEntityRefAbstract
        self._artop_bswModuleInstanceRef = None
        self._artop_componentIref = None
        self._artop_eventRef = None
        self._artop_successorRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswModuleInstanceRef': '"BSW-IMPLEMENTATION"', 
         '_artop_componentIref': '"COMPONENT-IN-COMPOSITION-INSTANCE-REF-IREF"', 
         '_artop_eventRef': '"ABSTRACT-EVENT"', 
         '_artop_successorRef': '"EOC-EXECUTABLE-ENTITY-REF-ABSTRACT"'})

    @property
    def ref_bswModuleInstance_(self):
        return self._artop_bswModuleInstanceRef

    @property
    def bswModuleInstance_(self):
        if self._artop_bswModuleInstanceRef is not None:
            if hasattr(self._artop_bswModuleInstanceRef, "uuid"):
                return self._artop_bswModuleInstanceRef.uuid
        return

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
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return

    @property
    def ref_successors_(self):
        return self._artop_successorRef

    @property
    def successors_(self):
        return self._artop_successorRef
