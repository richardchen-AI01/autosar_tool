# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleDescriptionRefConditional.py
from .ARObject import ARObject

class BswModuleDescriptionRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .BswModuleDependency import BswModuleDependency
        from .BswModuleDescription import BswModuleDescription
        from .VariationPoint import VariationPoint
        self._artop_bswModuleDependency = None
        self._artop_bswModuleDescriptionRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bswModuleDependency':"BSW-MODULE-DEPENDENCY", 
         '_artop_bswModuleDescriptionRef':"BSW-MODULE-DESCRIPTION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_bswModuleDependency_(self):
        return self._artop_bswModuleDependency

    @property
    def bswModuleDependency_(self):
        if self._artop_bswModuleDependency is not None:
            if hasattr(self._artop_bswModuleDependency, "uuid"):
                return self._artop_bswModuleDependency.uuid
        return

    @property
    def ref_bswModuleDescription_(self):
        return self._artop_bswModuleDescriptionRef

    @property
    def bswModuleDescription_(self):
        if self._artop_bswModuleDescriptionRef is not None:
            if hasattr(self._artop_bswModuleDescriptionRef, "uuid"):
                return self._artop_bswModuleDescriptionRef.uuid
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
