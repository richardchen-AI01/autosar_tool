# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ScheduleTableEntry.py
from .ARObject import ARObject

class ScheduleTableEntry(ARObject):

    def __init__(self):
        super().__init__()
        from .LinScheduleTable import LinScheduleTable
        from .DocumentationBlock import DocumentationBlock
        self._artop_delay = None
        self._artop_positionInTable = None
        self._artop_linScheduleTable = None
        self._artop_introduction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_linScheduleTable':"LIN-SCHEDULE-TABLE", 
         '_artop_introduction':"DOCUMENTATION-BLOCK"})

    @property
    def delay_(self):
        return self._artop_delay

    @property
    def positionInTable_(self):
        if self._artop_positionInTable:
            return int(self._artop_positionInTable)
        return self._artop_positionInTable

    @property
    def ref_linScheduleTable_(self):
        return self._artop_linScheduleTable

    @property
    def linScheduleTable_(self):
        if self._artop_linScheduleTable is not None:
            if hasattr(self._artop_linScheduleTable, "uuid"):
                return self._artop_linScheduleTable.uuid
        return

    @property
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return
