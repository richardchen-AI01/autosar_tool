# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcBswMapping.py
from .AtpStructureElement import AtpStructureElement
from .ARElement import ARElement

class SwcBswMapping(ARElement, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .SwcBswRunnableMapping import SwcBswRunnableMapping
        from .SwcInternalBehavior import SwcInternalBehavior
        from .SwcBswSynchronizedModeGroupPrototype import SwcBswSynchronizedModeGroupPrototype
        from .SwcBswSynchronizedTrigger import SwcBswSynchronizedTrigger
        self._artop_bswBehaviorRef = None
        self._artop_runnableMapping = []
        self._artop_swcBehaviorRef = None
        self._artop_synchronizedModeGroup = []
        self._artop_synchronizedTrigger = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswBehaviorRef': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_runnableMapping': '"SWC-BSW-RUNNABLE-MAPPING"', 
         '_artop_swcBehaviorRef': '"SWC-INTERNAL-BEHAVIOR"', 
         '_artop_synchronizedModeGroup': '"SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE"', 
         '_artop_synchronizedTrigger': '"SWC-BSW-SYNCHRONIZED-TRIGGER"'})

    @property
    def ref_bswBehavior_(self):
        return self._artop_bswBehaviorRef

    @property
    def bswBehavior_(self):
        if self._artop_bswBehaviorRef is not None:
            if hasattr(self._artop_bswBehaviorRef, "uuid"):
                return self._artop_bswBehaviorRef.uuid
        return

    @property
    def runnableMappings_SwcBswRunnableMapping(self):
        return self._artop_runnableMapping

    @property
    def ref_swcBehavior_(self):
        return self._artop_swcBehaviorRef

    @property
    def swcBehavior_(self):
        if self._artop_swcBehaviorRef is not None:
            if hasattr(self._artop_swcBehaviorRef, "uuid"):
                return self._artop_swcBehaviorRef.uuid
        return

    @property
    def synchronizedModeGroups_SwcBswSynchronizedModeGroupPrototype(self):
        return self._artop_synchronizedModeGroup

    @property
    def synchronizedTriggers_SwcBswSynchronizedTrigger(self):
        return self._artop_synchronizedTrigger
