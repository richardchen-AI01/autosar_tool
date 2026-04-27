# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinScheduleTable.py
from .Identifiable import Identifiable

class LinScheduleTable(Identifiable):

    def __init__(self):
        super().__init__()
        from .LinPhysicalChannel import LinPhysicalChannel
        from .ScheduleTableEntry import ScheduleTableEntry
        from .VariationPoint import VariationPoint
        self._artop_resumePosition = None
        self._artop_runMode = None
        self._artop_linPhysicalChannel = None
        self._artop_tableEntry = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_linPhysicalChannel':"LIN-PHYSICAL-CHANNEL", 
         '_artop_tableEntry':"SCHEDULE-TABLE-ENTRY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def resumePosition_(self):
        return self._artop_resumePosition

    @property
    def runMode_(self):
        return self._artop_runMode

    @property
    def ref_linPhysicalChannel_(self):
        return self._artop_linPhysicalChannel

    @property
    def linPhysicalChannel_(self):
        if self._artop_linPhysicalChannel is not None:
            if hasattr(self._artop_linPhysicalChannel, "uuid"):
                return self._artop_linPhysicalChannel.uuid
        return

    @property
    def tableEntries_ScheduleTableEntry(self):
        return self._artop_tableEntry

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
