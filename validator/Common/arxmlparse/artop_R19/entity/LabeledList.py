# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LabeledList.py
from .Paginateable import Paginateable

class LabeledList(Paginateable):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .IndentSample import IndentSample
        from .LabeledItem import LabeledItem
        from .VariationPoint import VariationPoint
        self._artop_documentationBlock = None
        self._artop_indentSample = None
        self._artop_labeledItem = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_documentationBlock': '"DOCUMENTATION-BLOCK"', 
         '_artop_indentSample': '"INDENT-SAMPLE"', 
         '_artop_labeledItem': '"LABELED-ITEM"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def ref_indentSample_(self):
        return self._artop_indentSample

    @property
    def indentSample_(self):
        if self._artop_indentSample is not None:
            if hasattr(self._artop_indentSample, "uuid"):
                return self._artop_indentSample.uuid
        return

    @property
    def labeledItems_LabeledItem(self):
        return self._artop_labeledItem

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
