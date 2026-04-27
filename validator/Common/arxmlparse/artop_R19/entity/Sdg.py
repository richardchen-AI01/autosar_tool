# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Sdg.py
from .ARObject import ARObject

class Sdg(ARObject):

    def __init__(self):
        super().__init__()
        from .SdgCaption import SdgCaption
        from .SdgContents import SdgContents
        from .VariationPoint import VariationPoint
        self._artop_gid = None
        self._artop_sdgCaption = None
        self._artop_sdgCaptionRef = None
        self._artop_sdgContentsType = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_sdgCaption': '"SDG-CAPTION"', 
         '_artop_sdgCaptionRef': '"SDG-CAPTION"', 
         '_artop_sdgContentsType': '"SDG-CONTENTS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def gid_(self):
        return self._artop_gid

    @property
    def ref_sdgCaption_(self):
        return self._artop_sdgCaption

    @property
    def sdgCaption_(self):
        if self._artop_sdgCaption is not None:
            if hasattr(self._artop_sdgCaption, "uuid"):
                return self._artop_sdgCaption.uuid
        return

    @property
    def ref_sdgCaptionRef_(self):
        return self._artop_sdgCaptionRef

    @property
    def sdgCaptionRef_(self):
        if self._artop_sdgCaptionRef is not None:
            if hasattr(self._artop_sdgCaptionRef, "uuid"):
                return self._artop_sdgCaptionRef.uuid
        return

    @property
    def ref_sdgContentsType_(self):
        return self._artop_sdgContentsType

    @property
    def sdgContentsType_(self):
        if self._artop_sdgContentsType is not None:
            if hasattr(self._artop_sdgContentsType, "uuid"):
                return self._artop_sdgContentsType.uuid
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
