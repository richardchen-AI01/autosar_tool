# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TpConnection.py
from .ARObject import ARObject

class TpConnection(ARObject):

    def __init__(self):
        super().__init__()
        from .TpConnectionIdent import TpConnectionIdent
        self._artop_ident = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ident": "TP-CONNECTION-IDENT"})

    @property
    def ref_ident_(self):
        return self._artop_ident

    @property
    def ident_(self):
        if self._artop_ident is not None:
            if hasattr(self._artop_ident, "uuid"):
                return self._artop_ident.uuid
        return
