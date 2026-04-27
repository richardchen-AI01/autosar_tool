# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionManifestRefConditional.py
from .ARObject import ARObject

class BuildActionManifestRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .Implementation import Implementation
        from .BuildActionManifest import BuildActionManifest
        from .VariationPoint import VariationPoint
        self._artop_implementation = None
        self._artop_buildActionManifestRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_implementation':"IMPLEMENTATION", 
         '_artop_buildActionManifestRef':"BUILD-ACTION-MANIFEST", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_implementation_(self):
        return self._artop_implementation

    @property
    def implementation_(self):
        if self._artop_implementation is not None:
            if hasattr(self._artop_implementation, "uuid"):
                return self._artop_implementation.uuid
        return

    @property
    def ref_buildActionManifest_(self):
        return self._artop_buildActionManifestRef

    @property
    def buildActionManifest_(self):
        if self._artop_buildActionManifestRef is not None:
            if hasattr(self._artop_buildActionManifestRef, "uuid"):
                return self._artop_buildActionManifestRef.uuid
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
