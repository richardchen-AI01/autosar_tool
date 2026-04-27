# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MlFigure.py
from .Paginateable import Paginateable

class MlFigure(Paginateable):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .Caption import Caption
        from .LGraphic import LGraphic
        from .MultiLanguageVerbatim import MultiLanguageVerbatim
        from .VariationPoint import VariationPoint
        self._artop_frame = None
        self._artop_helpEntry = None
        self._artop_pgwide = None
        self._artop_documentationBlock = None
        self._artop_figureCaption = None
        self._artop_lGraphic = []
        self._artop_verbatim = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_documentationBlock': '"DOCUMENTATION-BLOCK"', 
         '_artop_figureCaption': '"CAPTION"', 
         '_artop_lGraphic': '"L-GRAPHIC"', 
         '_artop_verbatim': '"MULTI-LANGUAGE-VERBATIM"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def frame_(self):
        return self._artop_frame

    @property
    def helpEntry_(self):
        return self._artop_helpEntry

    @property
    def pgwide_(self):
        return self._artop_pgwide

    @property
    def ref_documentationBlock_(self):
        return self._artop_documentationBlock

    @property
    def documentationBlock_(self):
        if self._artop_documentationBlock is not None:
            if hasattr(self._artop_documentationBlock, "uuid"):
                return self._artop_documentationBlock.uuid
        return

    @property
    def ref_figureCaption_(self):
        return self._artop_figureCaption

    @property
    def figureCaption_(self):
        if self._artop_figureCaption is not None:
            if hasattr(self._artop_figureCaption, "uuid"):
                return self._artop_figureCaption.uuid
        return

    @property
    def lGraphics_LGraphic(self):
        return self._artop_lGraphic

    @property
    def ref_verbatim_(self):
        return self._artop_verbatim

    @property
    def verbatim_(self):
        if self._artop_verbatim is not None:
            if hasattr(self._artop_verbatim, "uuid"):
                return self._artop_verbatim.uuid
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
