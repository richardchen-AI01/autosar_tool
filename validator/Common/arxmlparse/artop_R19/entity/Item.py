# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Item.py
from .Paginateable import Paginateable

class Item(Paginateable):

    def __init__(self):
        super().__init__()
        from .List import List
        from .DocumentationBlock import DocumentationBlock
        from .VariationPoint import VariationPoint
        self._artop_list = None
        self._artop_itemContents = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_list':"LIST", 
         '_artop_itemContents':"DOCUMENTATION-BLOCK", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_list_(self):
        return self._artop_list

    @property
    def list_(self):
        if self._artop_list is not None:
            if hasattr(self._artop_list, "uuid"):
                return self._artop_list.uuid
        return

    @property
    def ref_itemContents_(self):
        return self._artop_itemContents

    @property
    def itemContents_(self):
        if self._artop_itemContents is not None:
            if hasattr(self._artop_itemContents, "uuid"):
                return self._artop_itemContents.uuid
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
