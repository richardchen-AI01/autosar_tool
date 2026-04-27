# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventOperation.py
from .TDEventVfbPort import TDEventVfbPort

class TDEventOperation(TDEventVfbPort):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        self._artop_tdEventOperationType = None
        self._artop_operationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_operationRef": "CLIENT-SERVER-OPERATION"})

    @property
    def tdEventOperationType_(self):
        return self._artop_tdEventOperationType

    @property
    def ref_operation_(self):
        return self._artop_operationRef

    @property
    def operation_(self):
        if self._artop_operationRef is not None:
            if hasattr(self._artop_operationRef, "uuid"):
                return self._artop_operationRef.uuid
        return
