# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DefList.py
from .Paginateable import Paginateable

class DefList(Paginateable):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .DefItem import DefItem
        from .VariationPoint import VariationPoint
        self._artop_documentationBlock = None
        self._artop_defItem = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_documentationBlock':"DOCUMENTATION-BLOCK", 
         '_artop_defItem':"DEF-ITEM", 
         '_artop_variationPoint':"VARIATION-POINT"})

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
    def defItems_DefItem(self):
        return self._artop_defItem

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
