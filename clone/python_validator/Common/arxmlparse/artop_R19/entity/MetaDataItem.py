# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MetaDataItem.py
from .ARObject import ARObject

class MetaDataItem(ARObject):

    def __init__(self):
        super().__init__()
        from .MetaDataItemSet import MetaDataItemSet
        from .TextValueSpecification import TextValueSpecification
        self._artop_length = None
        self._artop_metaDataItemSet = None
        self._artop_metaDataItemType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_metaDataItemSet':"META-DATA-ITEM-SET", 
         '_artop_metaDataItemType':"TEXT-VALUE-SPECIFICATION"})

    @property
    def length_(self):
        return self._artop_length

    @property
    def ref_metaDataItemSet_(self):
        return self._artop_metaDataItemSet

    @property
    def metaDataItemSet_(self):
        if self._artop_metaDataItemSet is not None:
            if hasattr(self._artop_metaDataItemSet, "uuid"):
                return self._artop_metaDataItemSet.uuid
        return

    @property
    def ref_metaDataItemType_(self):
        return self._artop_metaDataItemType

    @property
    def metaDataItemType_(self):
        if self._artop_metaDataItemType is not None:
            if hasattr(self._artop_metaDataItemType, "uuid"):
                return self._artop_metaDataItemType.uuid
        return
