# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmPdu.py
from .Pdu import Pdu

class NmPdu(Pdu):

    def __init__(self):
        super().__init__()
        from .ISignalToIPduMapping import ISignalToIPduMapping
        self._artop_nmDataInformation = None
        self._artop_nmVoteInformation = None
        self._artop_unusedBitPattern = None
        self._artop_iSignalToIPduMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_iSignalToIPduMapping": "I-SIGNAL-TO-I-PDU-MAPPING"})

    @property
    def nmDataInformation_(self):
        if self._artop_nmDataInformation:
            if self._artop_nmDataInformation == "true":
                return True
            return False
        else:
            return self._artop_nmDataInformation

    @property
    def nmVoteInformation_(self):
        if self._artop_nmVoteInformation:
            if self._artop_nmVoteInformation == "true":
                return True
            return False
        else:
            return self._artop_nmVoteInformation

    @property
    def unusedBitPattern_(self):
        if self._artop_unusedBitPattern:
            return int(self._artop_unusedBitPattern)
        return self._artop_unusedBitPattern

    @property
    def iSignalToIPduMappings_ISignalToIPduMapping(self):
        return self._artop_iSignalToIPduMapping
