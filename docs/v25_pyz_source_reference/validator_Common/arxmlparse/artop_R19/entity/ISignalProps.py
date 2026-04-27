# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalProps.py
from .ARObject import ARObject

class ISignalProps(ARObject):

    def __init__(self):
        super().__init__()
        from .ISignal import ISignal
        self._artop_handleOutOfRange = None
        self._artop_iSignal = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_iSignal": "I-SIGNAL"})

    @property
    def handleOutOfRange_(self):
        return self._artop_handleOutOfRange

    @property
    def ref_iSignal_(self):
        return self._artop_iSignal

    @property
    def iSignal_(self):
        if self._artop_iSignal is not None:
            if hasattr(self._artop_iSignal, "uuid"):
                return self._artop_iSignal.uuid
        return
