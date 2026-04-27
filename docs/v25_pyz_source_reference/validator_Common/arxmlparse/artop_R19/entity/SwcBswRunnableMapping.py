# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcBswRunnableMapping.py
from .ARObject import ARObject

class SwcBswRunnableMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcBswMapping import SwcBswMapping
        from .BswModuleEntity import BswModuleEntity
        from .RunnableEntity import RunnableEntity
        from .VariationPoint import VariationPoint
        self._artop_swcBswMapping = None
        self._artop_bswEntityRef = None
        self._artop_swcRunnableRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcBswMapping': '"SWC-BSW-MAPPING"', 
         '_artop_bswEntityRef': '"BSW-MODULE-ENTITY"', 
         '_artop_swcRunnableRef': '"RUNNABLE-ENTITY"', 
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
    def ref_bswEntity_(self):
        return self._artop_bswEntityRef

    @property
    def bswEntity_(self):
        if self._artop_bswEntityRef is not None:
            if hasattr(self._artop_bswEntityRef, "uuid"):
                return self._artop_bswEntityRef.uuid
        return

    @property
    def ref_swcRunnable_(self):
        return self._artop_swcRunnableRef

    @property
    def swcRunnable_(self):
        if self._artop_swcRunnableRef is not None:
            if hasattr(self._artop_swcRunnableRef, "uuid"):
                return self._artop_swcRunnableRef.uuid
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
