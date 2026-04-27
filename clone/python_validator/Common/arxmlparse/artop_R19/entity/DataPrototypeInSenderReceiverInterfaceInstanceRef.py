# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInSenderReceiverInterfaceInstanceRef.py
from .DataPrototypeInPortInterfaceInstanceRef import DataPrototypeInPortInterfaceInstanceRef

class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):

    def __init__(self):
        super().__init__()
        from .SenderReceiverInterface import SenderReceiverInterface
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_senderReceiverInterface = None
        self._artop_rootDataPrototypeInSrRef = None
        self._artop_contextDataPrototypeInSrRef = []
        self._artop_targetDataPrototypeInSrRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_senderReceiverInterface': '"SENDER-RECEIVER-INTERFACE"', 
         '_artop_rootDataPrototypeInSrRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeInSrRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeInSrRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_base_(self):
        return self._artop_senderReceiverInterface

    @property
    def base_(self):
        if self._artop_senderReceiverInterface is not None:
            if hasattr(self._artop_senderReceiverInterface, "uuid"):
                return self._artop_senderReceiverInterface.uuid
        return

    @property
    def ref_rootDataPrototypeInSr_(self):
        return self._artop_rootDataPrototypeInSrRef

    @property
    def rootDataPrototypeInSr_(self):
        if self._artop_rootDataPrototypeInSrRef is not None:
            if hasattr(self._artop_rootDataPrototypeInSrRef, "uuid"):
                return self._artop_rootDataPrototypeInSrRef.uuid
        return

    @property
    def ref_contextDataPrototypeInSrs_(self):
        return self._artop_contextDataPrototypeInSrRef

    @property
    def contextDataPrototypeInSrs_(self):
        return self._artop_contextDataPrototypeInSrRef

    @property
    def ref_targetDataPrototypeInSr_(self):
        return self._artop_targetDataPrototypeInSrRef

    @property
    def targetDataPrototypeInSr_(self):
        if self._artop_targetDataPrototypeInSrRef is not None:
            if hasattr(self._artop_targetDataPrototypeInSrRef, "uuid"):
                return self._artop_targetDataPrototypeInSrRef.uuid
        return
