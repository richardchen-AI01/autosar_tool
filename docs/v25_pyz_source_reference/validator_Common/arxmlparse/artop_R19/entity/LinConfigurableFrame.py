# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinConfigurableFrame.py
from .ARObject import ARObject

class LinConfigurableFrame(ARObject):

    def __init__(self):
        super().__init__()
        from .LinCommunicationConnector import LinCommunicationConnector
        from .LinFrame import LinFrame
        self._artop_messageId = None
        self._artop_linCommunicationConnector = None
        self._artop_frameRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_linCommunicationConnector':"LIN-COMMUNICATION-CONNECTOR", 
         '_artop_frameRef':"LIN-FRAME"})

    @property
    def messageId_(self):
        return self._artop_messageId

    @property
    def ref_linCommunicationConnector_(self):
        return self._artop_linCommunicationConnector

    @property
    def linCommunicationConnector_(self):
        if self._artop_linCommunicationConnector is not None:
            if hasattr(self._artop_linCommunicationConnector, "uuid"):
                return self._artop_linCommunicationConnector.uuid
        return

    @property
    def ref_frame_(self):
        return self._artop_frameRef

    @property
    def frame_(self):
        if self._artop_frameRef is not None:
            if hasattr(self._artop_frameRef, "uuid"):
                return self._artop_frameRef.uuid
        return
