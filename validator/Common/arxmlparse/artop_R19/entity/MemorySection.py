# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MemorySection.py
from .Identifiable import Identifiable

class MemorySection(Identifiable):

    def __init__(self):
        super().__init__()
        from .ResourceConsumption import ResourceConsumption
        from .ExecutableEntity import ExecutableEntity
        from .SectionNamePrefix import SectionNamePrefix
        from .SwAddrMethod import SwAddrMethod
        from .VariationPoint import VariationPoint
        self._artop_alignment = None
        self._artop_memClassSymbol = None
        self._artop_option = None
        self._artop_size = None
        self._artop_symbol = None
        self._artop_resourceConsumption = None
        self._artop_executableEntityRef = []
        self._artop_prefixRef = None
        self._artop_swAddrmethodRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_resourceConsumption': '"RESOURCE-CONSUMPTION"', 
         '_artop_executableEntityRef': '"EXECUTABLE-ENTITY"', 
         '_artop_prefixRef': '"SECTION-NAME-PREFIX"', 
         '_artop_swAddrmethodRef': '"SW-ADDR-METHOD"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def alignment_(self):
        return self._artop_alignment

    @property
    def memClassSymbol_(self):
        return self._artop_memClassSymbol

    @property
    def option_(self):
        return self._artop_option

    @property
    def size_(self):
        return self._artop_size

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return

    @property
    def ref_executableEntities_(self):
        return self._artop_executableEntityRef

    @property
    def executableEntities_(self):
        return self._artop_executableEntityRef

    @property
    def ref_prefix_(self):
        return self._artop_prefixRef

    @property
    def prefix_(self):
        if self._artop_prefixRef is not None:
            if hasattr(self._artop_prefixRef, "uuid"):
                return self._artop_prefixRef.uuid
        return

    @property
    def ref_swAddrmethod_(self):
        return self._artop_swAddrmethodRef

    @property
    def swAddrmethod_(self):
        if self._artop_swAddrmethodRef is not None:
            if hasattr(self._artop_swAddrmethodRef, "uuid"):
                return self._artop_swAddrmethodRef.uuid
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
