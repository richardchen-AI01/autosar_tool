# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Entry.py
from .ARObject import ARObject

class Entry(ARObject):

    def __init__(self):
        super().__init__()
        from .Row import Row
        from .DocumentationBlock import DocumentationBlock
        self._artop_bgcolor = None
        self._artop_align = None
        self._artop_bgcolor = None
        self._artop_colname = None
        self._artop_colsep = None
        self._artop_morerows = None
        self._artop_nameend = None
        self._artop_namest = None
        self._artop_rotate = None
        self._artop_rowsep = None
        self._artop_spanname = None
        self._artop_valign = None
        self._artop_row = None
        self._artop_entryContents = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_row':"ROW", 
         '_artop_entryContents':"DOCUMENTATION-BLOCK"})

    @property
    def bgcolor_(self):
        return self._artop_bgcolor

    @property
    def align_(self):
        return self._artop_align

    @property
    def bgcolor_(self):
        return self._artop_bgcolor

    @property
    def colname_(self):
        return self._artop_colname

    @property
    def colsep_(self):
        return self._artop_colsep

    @property
    def morerows_(self):
        return self._artop_morerows

    @property
    def nameend_(self):
        return self._artop_nameend

    @property
    def namest_(self):
        return self._artop_namest

    @property
    def rotate_(self):
        return self._artop_rotate

    @property
    def rowsep_(self):
        return self._artop_rowsep

    @property
    def spanname_(self):
        return self._artop_spanname

    @property
    def valign_(self):
        return self._artop_valign

    @property
    def ref_row_(self):
        return self._artop_row

    @property
    def row_(self):
        if self._artop_row is not None:
            if hasattr(self._artop_row, "uuid"):
                return self._artop_row.uuid
        return

    @property
    def ref_entryContents_(self):
        return self._artop_entryContents

    @property
    def entryContents_(self):
        if self._artop_entryContents is not None:
            if hasattr(self._artop_entryContents, "uuid"):
                return self._artop_entryContents.uuid
        return
