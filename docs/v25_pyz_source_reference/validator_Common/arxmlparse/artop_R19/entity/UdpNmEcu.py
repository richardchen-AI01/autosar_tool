# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UdpNmEcu.py
from .BusspecificNmEcu import BusspecificNmEcu

class UdpNmEcu(BusspecificNmEcu):

    def __init__(self):
        super().__init__()
        self._artop_nmRepeatMsgIndicationEnabled = None
        self._artop_nmSynchronizationPointEnabled = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def nmRepeatMsgIndicationEnabled_(self):
        if self._artop_nmRepeatMsgIndicationEnabled:
            if self._artop_nmRepeatMsgIndicationEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmRepeatMsgIndicationEnabled

    @property
    def nmSynchronizationPointEnabled_(self):
        if self._artop_nmSynchronizationPointEnabled:
            if self._artop_nmSynchronizationPointEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmSynchronizationPointEnabled
