# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanClusterBusOffRecovery.py
from .ARObject import ARObject

class CanClusterBusOffRecovery(ARObject):

    def __init__(self):
        super().__init__()
        from .AbstractCanClusterContent import AbstractCanClusterContent
        self._artop_borCounterL1ToL2 = None
        self._artop_borTimeL1 = None
        self._artop_borTimeL2 = None
        self._artop_borTimeTxEnsured = None
        self._artop_mainFunctionPeriod = None
        self._artop_abstractCanClusterContent = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_abstractCanClusterContent": "ABSTRACT-CAN-CLUSTER-CONTENT"})

    @property
    def borCounterL1ToL2_(self):
        return self._artop_borCounterL1ToL2

    @property
    def borTimeL1_(self):
        return self._artop_borTimeL1

    @property
    def borTimeL2_(self):
        return self._artop_borTimeL2

    @property
    def borTimeTxEnsured_(self):
        return self._artop_borTimeTxEnsured

    @property
    def mainFunctionPeriod_(self):
        return self._artop_mainFunctionPeriod

    @property
    def ref_abstractCanClusterContent_(self):
        return self._artop_abstractCanClusterContent

    @property
    def abstractCanClusterContent_(self):
        if self._artop_abstractCanClusterContent is not None:
            if hasattr(self._artop_abstractCanClusterContent, "uuid"):
                return self._artop_abstractCanClusterContent.uuid
        return
