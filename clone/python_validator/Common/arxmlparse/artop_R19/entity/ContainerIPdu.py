# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ContainerIPdu.py
from .IPdu import IPdu

class ContainerIPdu(IPdu):

    def __init__(self):
        super().__init__()
        from .PduTriggering import PduTriggering
        self._artop_containerTimeout = None
        self._artop_containerTrigger = None
        self._artop_headerType = None
        self._artop_minimumRxContainerQueueSize = None
        self._artop_minimumTxContainerQueueSize = None
        self._artop_rxAcceptContainedIPdu = None
        self._artop_thresholdSize = None
        self._artop_unusedBitPattern = None
        self._artop_containedPduTriggeringRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_containedPduTriggeringRef": "PDU-TRIGGERING"})

    @property
    def containerTimeout_(self):
        return self._artop_containerTimeout

    @property
    def containerTrigger_(self):
        return self._artop_containerTrigger

    @property
    def headerType_(self):
        return self._artop_headerType

    @property
    def minimumRxContainerQueueSize_(self):
        return self._artop_minimumRxContainerQueueSize

    @property
    def minimumTxContainerQueueSize_(self):
        return self._artop_minimumTxContainerQueueSize

    @property
    def rxAcceptContainedIPdu_(self):
        return self._artop_rxAcceptContainedIPdu

    @property
    def thresholdSize_(self):
        return self._artop_thresholdSize

    @property
    def unusedBitPattern_(self):
        return self._artop_unusedBitPattern

    @property
    def ref_containedPduTriggerings_(self):
        return self._artop_containedPduTriggeringRef

    @property
    def containedPduTriggerings_(self):
        return self._artop_containedPduTriggeringRef
