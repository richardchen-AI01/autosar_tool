# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwRecordLayoutGroupContent.py
from .ARObject import ARObject

class SwRecordLayoutGroupContent(ARObject):

    def __init__(self):
        super().__init__()
        from .SwRecordLayoutGroup import SwRecordLayoutGroup
        from .SwRecordLayout import SwRecordLayout
        from .SwRecordLayoutV import SwRecordLayoutV
        self._artop_mixed = None
        self._artop_swRecordLayoutGroup = None
        self._artop_swRecordLayoutRef = []
        self._artop_swRecordLayoutV = []
        self._artop_swRecordLayoutGroup = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swRecordLayoutGroup': '"SW-RECORD-LAYOUT-GROUP"', 
         '_artop_swRecordLayoutRef': '"SW-RECORD-LAYOUT"', 
         '_artop_swRecordLayoutV': '"SW-RECORD-LAYOUT-V"', 
         '_artop_swRecordLayoutGroup': '"SW-RECORD-LAYOUT-GROUP"'})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_swRecordLayoutGroup_(self):
        return self._artop_swRecordLayoutGroup

    @property
    def swRecordLayoutGroup_(self):
        if self._artop_swRecordLayoutGroup is not None:
            if hasattr(self._artop_swRecordLayoutGroup, "uuid"):
                return self._artop_swRecordLayoutGroup.uuid
        return

    @property
    def ref_swRecordLayouts_(self):
        return self._artop_swRecordLayoutRef

    @property
    def swRecordLayouts_(self):
        return self._artop_swRecordLayoutRef

    @property
    def swRecordLayoutVs_SwRecordLayoutV(self):
        return self._artop_swRecordLayoutV

    @property
    def swRecordLayoutGroups_SwRecordLayoutGroup(self):
        return self._artop_swRecordLayoutGroup
