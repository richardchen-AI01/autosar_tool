# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Row.py
from .Paginateable import Paginateable

class Row(Paginateable):

    def __init__(self):
        super().__init__()
        from .Tbody import Tbody
        from .Entry import Entry
        from .VariationPoint import VariationPoint
        self._artop_rowsep = None
        self._artop_valign = None
        self._artop_tbody = None
        self._artop_entry = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tbody':"TBODY", 
         '_artop_entry':"ENTRY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def rowsep_(self):
        return self._artop_rowsep

    @property
    def valign_(self):
        return self._artop_valign

    @property
    def ref_tbody_(self):
        return self._artop_tbody

    @property
    def tbody_(self):
        if self._artop_tbody is not None:
            if hasattr(self._artop_tbody, "uuid"):
                return self._artop_tbody.uuid
        return

    @property
    def entries_Entry(self):
        return self._artop_entry

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
