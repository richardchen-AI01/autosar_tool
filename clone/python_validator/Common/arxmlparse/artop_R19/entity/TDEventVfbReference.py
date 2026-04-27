# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventVfbReference.py
from .TDEventVfb import TDEventVfb

class TDEventVfbReference(TDEventVfb):

    def __init__(self):
        super().__init__()
        from .TDEventVfb import TDEventVfb
        self._artop_referencedTdEventVfbRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_referencedTdEventVfbRef": "TD-EVENT-VFB"})

    @property
    def ref_referencedTDEventVfb_(self):
        return self._artop_referencedTdEventVfbRef

    @property
    def referencedTDEventVfb_(self):
        if self._artop_referencedTdEventVfbRef is not None:
            if hasattr(self._artop_referencedTdEventVfbRef, "uuid"):
                return self._artop_referencedTdEventVfbRef.uuid
        return
