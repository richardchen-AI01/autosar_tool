# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractCanCommunicationControllerContent.py
from .CommunicationControllerContent import CommunicationControllerContent

class AbstractCanCommunicationControllerContent(CommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .AbstractCanCommunicationControllerAttributes import AbstractCanCommunicationControllerAttributes
        self._artop_canControllerAttributes = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_canControllerAttributes": "ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES"})

    @property
    def ref_canControllerAttributes_(self):
        return self._artop_canControllerAttributes

    @property
    def canControllerAttributes_(self):
        if self._artop_canControllerAttributes is not None:
            if hasattr(self._artop_canControllerAttributes, "uuid"):
                return self._artop_canControllerAttributes.uuid
        return
