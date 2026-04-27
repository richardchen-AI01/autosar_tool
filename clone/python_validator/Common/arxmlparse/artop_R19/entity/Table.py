# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Table.py
from .Paginateable import Paginateable

class Table(Paginateable):

    def __init__(self):
        super().__init__()
        from .Caption import Caption
        from .Tgroup import Tgroup
        from .VariationPoint import VariationPoint
        self._artop_colsep = None
        self._artop_float = None
        self._artop_frame = None
        self._artop_helpEntry = None
        self._artop_orient = None
        self._artop_pgwide = None
        self._artop_rowsep = None
        self._artop_tabstyle = None
        self._artop_tableCaption = None
        self._artop_tgroup = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tableCaption':"CAPTION", 
         '_artop_tgroup':"TGROUP", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def colsep_(self):
        return self._artop_colsep

    @property
    def float_(self):
        return self._artop_float

    @property
    def frame_(self):
        return self._artop_frame

    @property
    def helpEntry_(self):
        return self._artop_helpEntry

    @property
    def orient_(self):
        return self._artop_orient

    @property
    def pgwide_(self):
        return self._artop_pgwide

    @property
    def rowsep_(self):
        return self._artop_rowsep

    @property
    def tabstyle_(self):
        return self._artop_tabstyle

    @property
    def ref_tableCaption_(self):
        return self._artop_tableCaption

    @property
    def tableCaption_(self):
        if self._artop_tableCaption is not None:
            if hasattr(self._artop_tableCaption, "uuid"):
                return self._artop_tableCaption.uuid
        return

    @property
    def tgroups_Tgroup(self):
        return self._artop_tgroup

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
