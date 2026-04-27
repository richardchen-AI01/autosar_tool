# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Colspec.py
from .ARObject import ARObject

class Colspec(ARObject):

    def __init__(self):
        super().__init__()
        from .Tgroup import Tgroup
        self._artop_align = None
        self._artop_colname = None
        self._artop_colnum = None
        self._artop_colsep = None
        self._artop_colwidth = None
        self._artop_rowsep = None
        self._artop_tgroup = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tgroup": "TGROUP"})

    @property
    def align_(self):
        return self._artop_align

    @property
    def colname_(self):
        return self._artop_colname

    @property
    def colnum_(self):
        return self._artop_colnum

    @property
    def colsep_(self):
        return self._artop_colsep

    @property
    def colwidth_(self):
        return self._artop_colwidth

    @property
    def rowsep_(self):
        return self._artop_rowsep

    @property
    def ref_tgroup_(self):
        return self._artop_tgroup

    @property
    def tgroup_(self):
        if self._artop_tgroup is not None:
            if hasattr(self._artop_tgroup, "uuid"):
                return self._artop_tgroup.uuid
        return
