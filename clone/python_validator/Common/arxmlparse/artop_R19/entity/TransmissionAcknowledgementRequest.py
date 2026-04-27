# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransmissionAcknowledgementRequest.py
from .ARObject import ARObject

class TransmissionAcknowledgementRequest(ARObject):

    def __init__(self):
        super().__init__()
        from .SenderComSpec import SenderComSpec
        self._artop_timeout = None
        self._artop_senderComSpec = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_senderComSpec": "SENDER-COM-SPEC"})

    @property
    def timeout_(self):
        return self._artop_timeout

    @property
    def ref_senderComSpec_(self):
        return self._artop_senderComSpec

    @property
    def senderComSpec_(self):
        if self._artop_senderComSpec is not None:
            if hasattr(self._artop_senderComSpec, "uuid"):
                return self._artop_senderComSpec.uuid
        return
