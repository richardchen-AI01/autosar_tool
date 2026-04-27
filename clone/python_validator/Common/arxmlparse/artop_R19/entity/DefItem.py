# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DefItem.py
from .Paginateable import Paginateable
from .MultilanguageReferrable import MultilanguageReferrable

class DefItem(MultilanguageReferrable, Paginateable):

    def __init__(self):
        super().__init__()
        from .DefList import DefList
        from .DocumentationBlock import DocumentationBlock
        from .VariationPoint import VariationPoint
        self._artop_helpEntry = None
        self._artop_defList = None
        self._artop_def_ = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_defList':"DEF-LIST", 
         '_artop_def_':"DOCUMENTATION-BLOCK", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def helpEntry_(self):
        return self._artop_helpEntry

    @property
    def ref_defList_(self):
        return self._artop_defList

    @property
    def defList_(self):
        if self._artop_defList is not None:
            if hasattr(self._artop_defList, "uuid"):
                return self._artop_defList.uuid
        return

    @property
    def ref_def_(self):
        return self._artop_def_

    @property
    def def_(self):
        if self._artop_def_ is not None:
            if hasattr(self._artop_def_, "uuid"):
                return self._artop_def_.uuid
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
