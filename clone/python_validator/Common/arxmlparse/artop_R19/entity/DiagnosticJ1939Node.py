# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticJ1939Node.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticJ1939Node(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .J1939NmNode import J1939NmNode
        self._artop_nmNodeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_nmNodeRef": "J-1939-NM-NODE"})

    @property
    def ref_nmNode_(self):
        return self._artop_nmNodeRef

    @property
    def nmNode_(self):
        if self._artop_nmNodeRef is not None:
            if hasattr(self._artop_nmNodeRef, "uuid"):
                return self._artop_nmNodeRef.uuid
        return
