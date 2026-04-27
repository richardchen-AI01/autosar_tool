# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExternalTriggeringPointIdent.py
from .IdentCaption import IdentCaption
from .AbstractAccessPoint import AbstractAccessPoint

class ExternalTriggeringPointIdent(AbstractAccessPoint, IdentCaption):

    def __init__(self):
        super().__init__()
        from .ExternalTriggeringPoint import ExternalTriggeringPoint
        self._artop_externalTriggeringPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_externalTriggeringPoint": "EXTERNAL-TRIGGERING-POINT"})

    @property
    def ref_externalTriggeringPoint_(self):
        return self._artop_externalTriggeringPoint

    @property
    def externalTriggeringPoint_(self):
        if self._artop_externalTriggeringPoint is not None:
            if hasattr(self._artop_externalTriggeringPoint, "uuid"):
                return self._artop_externalTriggeringPoint.uuid
        return
