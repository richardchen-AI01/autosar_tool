# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuContent.py
from .ARObject import ARObject

class CompuContent(ARObject):

    def __init__(self):
        super().__init__()
        from .Compu import Compu
        self._artop_compu = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compu": "COMPU"})

    @property
    def ref_compu_(self):
        return self._artop_compu

    @property
    def compu_(self):
        if self._artop_compu is not None:
            if hasattr(self._artop_compu, "uuid"):
                return self._artop_compu.uuid
        return
