# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MetaDataItemSet.py
from .ARObject import ARObject

class MetaDataItemSet(ARObject):

    def __init__(self):
        super().__init__()
        from .SenderReceiverInterface import SenderReceiverInterface
        from .VariableDataPrototype import VariableDataPrototype
        from .MetaDataItem import MetaDataItem
        self._artop_senderReceiverInterface = None
        self._artop_dataElementRef = []
        self._artop_metaDataItem = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_senderReceiverInterface':"SENDER-RECEIVER-INTERFACE", 
         '_artop_dataElementRef':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_metaDataItem':"META-DATA-ITEM"})

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
    def ref_dataElements_(self):
        return self._artop_dataElementRef

    @property
    def dataElements_(self):
        return self._artop_dataElementRef

    @property
    def metaDataItems_MetaDataItem(self):
        return self._artop_metaDataItem
