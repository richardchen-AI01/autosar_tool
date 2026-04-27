# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalIPduGroup.py
from .FibexElement import FibexElement

class ISignalIPduGroup(FibexElement):

    def __init__(self):
        super().__init__()
        from .ISignalIPduRefConditional import ISignalIPduRefConditional
        from .NmPduRefConditional import NmPduRefConditional
        self._artop_communicationDirection = None
        self._artop_communicationMode = None
        self._artop_containedISignalIPduGroupRef = []
        self._artop_iSignalIPdu = []
        self._artop_nmPdu = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_containedISignalIPduGroupRef':"I-SIGNAL-I-PDU-GROUP", 
         '_artop_iSignalIPdu':"I-SIGNAL-I-PDU-REF-CONDITIONAL", 
         '_artop_nmPdu':"NM-PDU-REF-CONDITIONAL"})

    @property
    def communicationDirection_(self):
        return self._artop_communicationDirection

    @property
    def communicationMode_(self):
        return self._artop_communicationMode

    @property
    def ref_containedISignalIPduGroups_(self):
        return self._artop_containedISignalIPduGroupRef

    @property
    def containedISignalIPduGroups_(self):
        return self._artop_containedISignalIPduGroupRef

    @property
    def iSignalIPdus_ISignalIPduRefConditional(self):
        return self._artop_iSignalIPdu

    @property
    def nmPdus_NmPduRefConditional(self):
        return self._artop_nmPdu
