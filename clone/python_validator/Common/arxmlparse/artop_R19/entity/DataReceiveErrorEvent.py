# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataReceiveErrorEvent.py
from .RTEEvent import RTEEvent

class DataReceiveErrorEvent(RTEEvent):

    def __init__(self):
        super().__init__()
        from .RVariableInAtomicSwcInstanceRef import RVariableInAtomicSwcInstanceRef
        self._artop_dataIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataIref": "R-VARIABLE-IN-ATOMIC-SWC-INSTANCE-REF"})

    @property
    def ref_data_(self):
        return self._artop_dataIref

    @property
    def data_(self):
        if self._artop_dataIref is not None:
            if hasattr(self._artop_dataIref, "uuid"):
                return self._artop_dataIref.uuid
        return
