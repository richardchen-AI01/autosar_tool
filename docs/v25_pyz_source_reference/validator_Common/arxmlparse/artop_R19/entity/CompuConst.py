# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuConst.py
from .ARObject import ARObject

class CompuConst(ARObject):

    def __init__(self):
        super().__init__()
        from .CompuConstContent import CompuConstContent
        self._artop_compuConstContentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compuConstContentType": "COMPU-CONST-CONTENT"})

    @property
    def ref_compuConstContentType_(self):
        return self._artop_compuConstContentType

    @property
    def compuConstContentType_(self):
        if self._artop_compuConstContentType is not None:
            if hasattr(self._artop_compuConstContentType, "uuid"):
                return self._artop_compuConstContentType.uuid
        return
