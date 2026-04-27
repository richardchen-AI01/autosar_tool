# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SenderReceiverInterface.py
from .DataInterface import DataInterface

class SenderReceiverInterface(DataInterface):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototype import VariableDataPrototype
        from .InvalidationPolicy import InvalidationPolicy
        from .MetaDataItemSet import MetaDataItemSet
        self._artop_dataElement = []
        self._artop_invalidationPolicy = []
        self._artop_metaDataItemSet = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElement':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_invalidationPolicy':"INVALIDATION-POLICY", 
         '_artop_metaDataItemSet':"META-DATA-ITEM-SET"})

    @property
    def dataElements_VariableDataPrototype(self):
        return self._artop_dataElement

    @property
    def invalidationPolicies_InvalidationPolicy(self):
        return self._artop_invalidationPolicy

    @property
    def metaDataItemSets_MetaDataItemSet(self):
        return self._artop_metaDataItemSet
