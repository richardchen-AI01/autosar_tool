# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RTEEvent.py
from .AtpStructureElement import AtpStructureElement
from .AbstractEvent import AbstractEvent

class RTEEvent(AbstractEvent, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .SwcInternalBehavior import SwcInternalBehavior
        from .RModeInAtomicSwcInstanceRef import RModeInAtomicSwcInstanceRef
        from .RunnableEntity import RunnableEntity
        from .VariationPoint import VariationPoint
        self._artop_swcInternalBehavior = None
        self._artop_disabledModeIref = []
        self._artop_startOnEventRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcInternalBehavior': '"SWC-INTERNAL-BEHAVIOR"', 
         '_artop_disabledModeIref': '"R-MODE-IN-ATOMIC-SWC-INSTANCE-REF-IREF"', 
         '_artop_startOnEventRef': '"RUNNABLE-ENTITY"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_swcInternalBehavior_(self):
        return self._artop_swcInternalBehavior

    @property
    def swcInternalBehavior_(self):
        if self._artop_swcInternalBehavior is not None:
            if hasattr(self._artop_swcInternalBehavior, "uuid"):
                return self._artop_swcInternalBehavior.uuid
        return

    @property
    def disabledModes_RModeInAtomicSwcInstanceRef(self):
        return self._artop_disabledModeIref

    @property
    def ref_startOnEvent_(self):
        return self._artop_startOnEventRef

    @property
    def startOnEvent_(self):
        if self._artop_startOnEventRef is not None:
            if hasattr(self._artop_startOnEventRef, "uuid"):
                return self._artop_startOnEventRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
