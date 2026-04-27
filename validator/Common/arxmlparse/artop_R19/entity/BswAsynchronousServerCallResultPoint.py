# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswAsynchronousServerCallResultPoint.py
from .BswModuleCallPoint import BswModuleCallPoint

class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):

    def __init__(self):
        super().__init__()
        from .BswAsynchronousServerCallPoint import BswAsynchronousServerCallPoint
        self._artop_asynchronousServerCallPointRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_asynchronousServerCallPointRef": "BSW-ASYNCHRONOUS-SERVER-CALL-POINT"})

    @property
    def ref_asynchronousServerCallPoint_(self):
        return self._artop_asynchronousServerCallPointRef

    @property
    def asynchronousServerCallPoint_(self):
        if self._artop_asynchronousServerCallPointRef is not None:
            if hasattr(self._artop_asynchronousServerCallPointRef, "uuid"):
                return self._artop_asynchronousServerCallPointRef.uuid
        return
