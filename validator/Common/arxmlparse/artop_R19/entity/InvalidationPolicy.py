# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InvalidationPolicy.py
from .ARObject import ARObject

class InvalidationPolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .SenderReceiverInterface import SenderReceiverInterface
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_handleInvalid = None
        self._artop_senderReceiverInterface = None
        self._artop_dataElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_senderReceiverInterface':"SENDER-RECEIVER-INTERFACE", 
         '_artop_dataElementRef':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def handleInvalid_(self):
        return self._artop_handleInvalid

    @property
    def ref_senderReceiverInterface_(self):
        return self._artop_senderReceiverInterface

    @property
    def senderReceiverInterface_(self):
        if self._artop_senderReceiverInterface is not None:
            if hasattr(self._artop_senderReceiverInterface, "uuid"):
                return self._artop_senderReceiverInterface.uuid
        return

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return
