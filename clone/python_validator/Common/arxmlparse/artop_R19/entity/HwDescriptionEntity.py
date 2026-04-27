# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwDescriptionEntity.py
from .Referrable import Referrable

class HwDescriptionEntity(Referrable):

    def __init__(self):
        super().__init__()
        from .HwType import HwType
        from .HwCategory import HwCategory
        from .HwAttributeValue import HwAttributeValue
        self._artop_hwTypeRef = None
        self._artop_hwCategoryRef = []
        self._artop_hwAttributeValue = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_hwTypeRef':"HW-TYPE", 
         '_artop_hwCategoryRef':"HW-CATEGORY", 
         '_artop_hwAttributeValue':"HW-ATTRIBUTE-VALUE"})

    @property
    def ref_hwType_(self):
        return self._artop_hwTypeRef

    @property
    def hwType_(self):
        if self._artop_hwTypeRef is not None:
            if hasattr(self._artop_hwTypeRef, "uuid"):
                return self._artop_hwTypeRef.uuid
        return

    @property
    def ref_hwCategories_(self):
        return self._artop_hwCategoryRef

    @property
    def hwCategories_(self):
        return self._artop_hwCategoryRef

    @property
    def hwAttributeValues_HwAttributeValue(self):
        return self._artop_hwAttributeValue
