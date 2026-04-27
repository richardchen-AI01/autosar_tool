# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcBswSynchronizedTrigger.py
from .ARObject import ARObject

class SwcBswSynchronizedTrigger(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcBswMapping import SwcBswMapping
        from .Trigger import Trigger
        from .PTriggerInAtomicSwcTypeInstanceRef import PTriggerInAtomicSwcTypeInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_swcBswMapping = None
        self._artop_bswTriggerRef = None
        self._artop_swcTriggerIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcBswMapping': '"SWC-BSW-MAPPING"', 
         '_artop_bswTriggerRef': '"TRIGGER"', 
         '_artop_swcTriggerIref': '"P-TRIGGER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_swcBswMapping_(self):
        return self._artop_swcBswMapping

    @property
    def swcBswMapping_(self):
        if self._artop_swcBswMapping is not None:
            if hasattr(self._artop_swcBswMapping, "uuid"):
                return self._artop_swcBswMapping.uuid
        return

    @property
    def ref_bswTrigger_(self):
        return self._artop_bswTriggerRef

    @property
    def bswTrigger_(self):
        if self._artop_bswTriggerRef is not None:
            if hasattr(self._artop_bswTriggerRef, "uuid"):
                return self._artop_bswTriggerRef.uuid
        return

    @property
    def ref_swcTrigger_(self):
        return self._artop_swcTriggerIref

    @property
    def swcTrigger_(self):
        if self._artop_swcTriggerIref is not None:
            if hasattr(self._artop_swcTriggerIref, "uuid"):
                return self._artop_swcTriggerIref.uuid
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
