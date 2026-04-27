# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PerInstanceMemorySize.py
from .ARObject import ARObject

class PerInstanceMemorySize(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcImplementation import SwcImplementation
        from .PerInstanceMemory import PerInstanceMemory
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .VariationPoint import VariationPoint
        self._artop_alignment = None
        self._artop_swcImplementation = None
        self._artop_perInstanceMemoryRef = None
        self._artop_size = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcImplementation': '"SWC-IMPLEMENTATION"', 
         '_artop_perInstanceMemoryRef': '"PER-INSTANCE-MEMORY"', 
         '_artop_size': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def alignment_(self):
        return self._artop_alignment

    @property
    def ref_swcImplementation_(self):
        return self._artop_swcImplementation

    @property
    def swcImplementation_(self):
        if self._artop_swcImplementation is not None:
            if hasattr(self._artop_swcImplementation, "uuid"):
                return self._artop_swcImplementation.uuid
        return

    @property
    def ref_perInstanceMemory_(self):
        return self._artop_perInstanceMemoryRef

    @property
    def perInstanceMemory_(self):
        if self._artop_perInstanceMemoryRef is not None:
            if hasattr(self._artop_perInstanceMemoryRef, "uuid"):
                return self._artop_perInstanceMemoryRef.uuid
        return

    @property
    def ref_size_(self):
        return self._artop_size

    @property
    def size_(self):
        if self._artop_size is not None:
            if hasattr(self._artop_size, "uuid"):
                return self._artop_size.uuid
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
