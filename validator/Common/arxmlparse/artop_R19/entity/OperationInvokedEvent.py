# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\OperationInvokedEvent.py
from .RTEEvent import RTEEvent

class OperationInvokedEvent(RTEEvent):

    def __init__(self):
        super().__init__()
        from .POperationInAtomicSwcInstanceRef import POperationInAtomicSwcInstanceRef
        self._artop_operationIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_operationIref": "P-OPERATION-IN-ATOMIC-SWC-INSTANCE-REF"})

    @property
    def ref_operation_(self):
        return self._artop_operationIref

    @property
    def operation_(self):
        if self._artop_operationIref is not None:
            if hasattr(self._artop_operationIref, "uuid"):
                return self._artop_operationIref.uuid
        return
