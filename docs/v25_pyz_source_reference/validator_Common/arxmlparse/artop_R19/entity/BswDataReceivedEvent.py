# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswDataReceivedEvent.py
from .BswScheduleEvent import BswScheduleEvent

class BswDataReceivedEvent(BswScheduleEvent):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_dataRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataRef": "VARIABLE-DATA-PROTOTYPE"})

    @property
    def ref_data_(self):
        return self._artop_dataRef

    @property
    def data_(self):
        if self._artop_dataRef is not None:
            if hasattr(self._artop_dataRef, "uuid"):
                return self._artop_dataRef.uuid
        return
