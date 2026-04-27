# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcBswSynchronizedModeGroupPrototype.py
from .ARObject import ARObject

class SwcBswSynchronizedModeGroupPrototype(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcBswMapping import SwcBswMapping
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .PModeGroupInAtomicSwcInstanceRef import PModeGroupInAtomicSwcInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_swcBswMapping = None
        self._artop_bswModeGroupRef = None
        self._artop_swcModeGroupIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcBswMapping': '"SWC-BSW-MAPPING"', 
         '_artop_bswModeGroupRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_swcModeGroupIref': '"P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF"', 
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
    def ref_bswModeGroup_(self):
        return self._artop_bswModeGroupRef

    @property
    def bswModeGroup_(self):
        if self._artop_bswModeGroupRef is not None:
            if hasattr(self._artop_bswModeGroupRef, "uuid"):
                return self._artop_bswModeGroupRef.uuid
        return

    @property
    def ref_swcModeGroup_(self):
        return self._artop_swcModeGroupIref

    @property
    def swcModeGroup_(self):
        if self._artop_swcModeGroupIref is not None:
            if hasattr(self._artop_swcModeGroupIref, "uuid"):
                return self._artop_swcModeGroupIref.uuid
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
