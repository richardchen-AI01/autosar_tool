# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventSwcInternalBehaviorReference.py
from .TDEventSwc import TDEventSwc

class TDEventSwcInternalBehaviorReference(TDEventSwc):

    def __init__(self):
        super().__init__()
        from .TDEventSwc import TDEventSwc
        self._artop_referencedTdEventSwcRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_referencedTdEventSwcRef": "TD-EVENT-SWC"})

    @property
    def ref_referencedTDEventSwc_(self):
        return self._artop_referencedTdEventSwcRef

    @property
    def referencedTDEventSwc_(self):
        if self._artop_referencedTdEventSwcRef is not None:
            if hasattr(self._artop_referencedTdEventSwcRef, "uuid"):
                return self._artop_referencedTdEventSwcRef.uuid
        return
