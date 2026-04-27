# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcToSwcOperationArguments.py
from .ARObject import ARObject

class SwcToSwcOperationArguments(ARObject):

    def __init__(self):
        super().__init__()
        from .OperationInSystemInstanceRef import OperationInSystemInstanceRef
        self._artop_direction = None
        self._artop_operationIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_operationIref": "OPERATION-IN-SYSTEM-INSTANCE-REF-IREF"})

    @property
    def direction_(self):
        return self._artop_direction

    @property
    def operations_OperationInSystemInstanceRef(self):
        return self._artop_operationIref
