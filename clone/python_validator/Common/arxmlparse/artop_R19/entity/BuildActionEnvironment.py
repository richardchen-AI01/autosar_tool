# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionEnvironment.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint

class BuildActionEnvironment(AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .BuildActionManifest import BuildActionManifest
        from .Sdg import Sdg
        from .VariationPoint import VariationPoint
        self._artop_buildActionManifest = None
        self._artop_sdg = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_buildActionManifest':"BUILD-ACTION-MANIFEST", 
         '_artop_sdg':"SDG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_buildActionManifest_(self):
        return self._artop_buildActionManifest

    @property
    def buildActionManifest_(self):
        if self._artop_buildActionManifest is not None:
            if hasattr(self._artop_buildActionManifest, "uuid"):
                return self._artop_buildActionManifest.uuid
        return

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
