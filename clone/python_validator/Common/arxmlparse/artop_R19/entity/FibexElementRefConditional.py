# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FibexElementRefConditional.py
from .ARObject import ARObject

class FibexElementRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .System import System
        from .FibexElement import FibexElement
        from .VariationPoint import VariationPoint
        self._artop_system = None
        self._artop_fibexElementRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_system':"SYSTEM", 
         '_artop_fibexElementRef':"FIBEX-ELEMENT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_system_(self):
        return self._artop_system

    @property
    def system_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_fibexElement_(self):
        return self._artop_fibexElementRef

    @property
    def fibexElement_(self):
        if self._artop_fibexElementRef is not None:
            if hasattr(self._artop_fibexElementRef, "uuid"):
                return self._artop_fibexElementRef.uuid
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
