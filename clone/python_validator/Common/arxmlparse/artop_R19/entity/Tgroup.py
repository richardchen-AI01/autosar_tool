# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Tgroup.py
from .ARObject import ARObject

class Tgroup(ARObject):

    def __init__(self):
        super().__init__()
        from .Table import Table
        from .Colspec import Colspec
        from .Tbody import Tbody
        self._artop_align = None
        self._artop_cols = None
        self._artop_colsep = None
        self._artop_rowsep = None
        self._artop_table = None
        self._artop_colspec = []
        self._artop_thead = None
        self._artop_tfoot = None
        self._artop_tbody = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_table': '"TABLE"', 
         '_artop_colspec': '"COLSPEC"', 
         '_artop_thead': '"TBODY"', 
         '_artop_tfoot': '"TBODY"', 
         '_artop_tbody': '"TBODY"'})

    @property
    def align_(self):
        return self._artop_align

    @property
    def cols_(self):
        if self._artop_cols:
            return int(self._artop_cols)
        return self._artop_cols

    @property
    def colsep_(self):
        return self._artop_colsep

    @property
    def rowsep_(self):
        return self._artop_rowsep

    @property
    def ref_table_(self):
        return self._artop_table

    @property
    def table_(self):
        if self._artop_table is not None:
            if hasattr(self._artop_table, "uuid"):
                return self._artop_table.uuid
        return

    @property
    def colspecs_Colspec(self):
        return self._artop_colspec

    @property
    def ref_thead_(self):
        return self._artop_thead

    @property
    def thead_(self):
        if self._artop_thead is not None:
            if hasattr(self._artop_thead, "uuid"):
                return self._artop_thead.uuid
        return

    @property
    def ref_tfoot_(self):
        return self._artop_tfoot

    @property
    def tfoot_(self):
        if self._artop_tfoot is not None:
            if hasattr(self._artop_tfoot, "uuid"):
                return self._artop_tfoot.uuid
        return

    @property
    def ref_tbody_(self):
        return self._artop_tbody

    @property
    def tbody_(self):
        if self._artop_tbody is not None:
            if hasattr(self._artop_tbody, "uuid"):
                return self._artop_tbody.uuid
        return
