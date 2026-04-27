# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswEvent.py
from .AbstractEvent import AbstractEvent

class BswEvent(AbstractEvent):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .BswDistinguishedPartition import BswDistinguishedPartition
        from .ModeInBswModuleDescriptionInstanceRef import ModeInBswModuleDescriptionInstanceRef
        from .BswModuleEntity import BswModuleEntity
        from .VariationPoint import VariationPoint
        self._artop_bswInternalBehavior = None
        self._artop_contextLimitationRef = []
        self._artop_disabledInModeIref = []
        self._artop_startsOnEventRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswInternalBehavior': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_contextLimitationRef': '"BSW-DISTINGUISHED-PARTITION"', 
         '_artop_disabledInModeIref': '"MODE-IN-BSW-MODULE-DESCRIPTION-INSTANCE-REF-IREF"', 
         '_artop_startsOnEventRef': '"BSW-MODULE-ENTITY"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_bswInternalBehavior_(self):
        return self._artop_bswInternalBehavior

    @property
    def bswInternalBehavior_(self):
        if self._artop_bswInternalBehavior is not None:
            if hasattr(self._artop_bswInternalBehavior, "uuid"):
                return self._artop_bswInternalBehavior.uuid
        return

    @property
    def ref_contextLimitations_(self):
        return self._artop_contextLimitationRef

    @property
    def contextLimitations_(self):
        return self._artop_contextLimitationRef

    @property
    def disabledInModes_ModeInBswModuleDescriptionInstanceRef(self):
        return self._artop_disabledInModeIref

    @property
    def ref_startsOnEvent_(self):
        return self._artop_startsOnEventRef

    @property
    def startsOnEvent_(self):
        if self._artop_startsOnEventRef is not None:
            if hasattr(self._artop_startsOnEventRef, "uuid"):
                return self._artop_startsOnEventRef.uuid
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
