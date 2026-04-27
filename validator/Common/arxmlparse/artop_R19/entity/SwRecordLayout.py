# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwRecordLayout.py
from .ARElement import ARElement

class SwRecordLayout(ARElement):

    def __init__(self):
        super().__init__()
        from .SwRecordLayoutGroup import SwRecordLayoutGroup
        self._artop_swRecordLayoutGroup = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swRecordLayoutGroup": "SW-RECORD-LAYOUT-GROUP"})

    @property
    def ref_swRecordLayoutGroup_(self):
        return self._artop_swRecordLayoutGroup

    @property
    def swRecordLayoutGroup_(self):
        if self._artop_swRecordLayoutGroup is not None:
            if hasattr(self._artop_swRecordLayoutGroup, "uuid"):
                return self._artop_swRecordLayoutGroup.uuid
        return
