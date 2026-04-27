# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalIPdu.py
from .IPdu import IPdu

class ISignalIPdu(IPdu):

    def __init__(self):
        super().__init__()
        from .IPduTiming import IPduTiming
        from .ISignalToIPduMapping import ISignalToIPduMapping
        from .SignalIPduCounter import SignalIPduCounter
        from .SignalIPduReplication import SignalIPduReplication
        self._artop_unusedBitPattern = None
        self._artop_iPduTimingSpecification = []
        self._artop_iSignalToPduMapping = []
        self._artop_pduCounter = []
        self._artop_pduReplication = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_iPduTimingSpecification': '"I-PDU-TIMING"', 
         '_artop_iSignalToPduMapping': '"I-SIGNAL-TO-I-PDU-MAPPING"', 
         '_artop_pduCounter': '"SIGNAL-I-PDU-COUNTER"', 
         '_artop_pduReplication': '"SIGNAL-I-PDU-REPLICATION"'})

    @property
    def unusedBitPattern_(self):
        if self._artop_unusedBitPattern:
            return int(self._artop_unusedBitPattern)
        return self._artop_unusedBitPattern

    @property
    def iPduTimingSpecifications_IPduTiming(self):
        return self._artop_iPduTimingSpecification

    @property
    def iSignalToPduMappings_ISignalToIPduMapping(self):
        return self._artop_iSignalToPduMapping

    @property
    def pduCounters_SignalIPduCounter(self):
        return self._artop_pduCounter

    @property
    def pduReplications_SignalIPduReplication(self):
        return self._artop_pduReplication
