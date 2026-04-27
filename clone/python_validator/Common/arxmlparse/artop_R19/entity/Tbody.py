# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Tbody.py
from .ARObject import ARObject

class Tbody(ARObject):

    def __init__(self):
        super().__init__()
        from .Row import Row
        self._artop_valign = None
        self._artop_row = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_row": "ROW"})

    @property
    def valign_(self):
        return self._artop_valign

    @property
    def rows_Row(self):
        return self._artop_row
