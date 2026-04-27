# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeAccessPointIdent.py
from .IdentCaption import IdentCaption
from .AbstractAccessPoint import AbstractAccessPoint

class ModeAccessPointIdent(AbstractAccessPoint, IdentCaption):

    def __init__(self):
        super().__init__()
        from .ModeAccessPoint import ModeAccessPoint
        self._artop_modeAccessPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeAccessPoint": "MODE-ACCESS-POINT"})

    @property
    def ref_modeAccessPoint_(self):
        return self._artop_modeAccessPoint

    @property
    def modeAccessPoint_(self):
        if self._artop_modeAccessPoint is not None:
            if hasattr(self._artop_modeAccessPoint, "uuid"):
                return self._artop_modeAccessPoint.uuid
        return
