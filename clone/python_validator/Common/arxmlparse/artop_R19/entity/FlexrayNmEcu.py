# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayNmEcu.py
from .BusspecificNmEcu import BusspecificNmEcu

class FlexrayNmEcu(BusspecificNmEcu):

    def __init__(self):
        super().__init__()
        self._artop_nmHwVoteEnabled = None
        self._artop_nmMainFunctionAcrossFrCycle = None
        self._artop_nmRepeatMessageBitEnable = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def nmHwVoteEnabled_(self):
        if self._artop_nmHwVoteEnabled:
            if self._artop_nmHwVoteEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmHwVoteEnabled

    @property
    def nmMainFunctionAcrossFrCycle_(self):
        if self._artop_nmMainFunctionAcrossFrCycle:
            if self._artop_nmMainFunctionAcrossFrCycle == "true":
                return True
            return False
        else:
            return self._artop_nmMainFunctionAcrossFrCycle

    @property
    def nmRepeatMessageBitEnable_(self):
        if self._artop_nmRepeatMessageBitEnable:
            if self._artop_nmRepeatMessageBitEnable == "true":
                return True
            return False
        else:
            return self._artop_nmRepeatMessageBitEnable
