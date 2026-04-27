# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TextTableMapping.py
from .ARObject import ARObject

class TextTableMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .TextTableValuePair import TextTableValuePair
        self._artop_identicalMapping = None
        self._artop_mappingDirection = None
        self._artop_bitfieldTextTableMaskFirst = None
        self._artop_bitfieldTextTableMaskSecond = None
        self._artop_valuePair = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bitfieldTextTableMaskFirst':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_bitfieldTextTableMaskSecond':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_valuePair':"TEXT-TABLE-VALUE-PAIR"})

    @property
    def identicalMapping_(self):
        if self._artop_identicalMapping:
            if self._artop_identicalMapping == "true":
                return True
            return False
        else:
            return self._artop_identicalMapping

    @property
    def mappingDirection_(self):
        return self._artop_mappingDirection

    @property
    def ref_bitfieldTextTableMaskFirst_(self):
        return self._artop_bitfieldTextTableMaskFirst

    @property
    def bitfieldTextTableMaskFirst_(self):
        if self._artop_bitfieldTextTableMaskFirst is not None:
            if hasattr(self._artop_bitfieldTextTableMaskFirst, "uuid"):
                return self._artop_bitfieldTextTableMaskFirst.uuid
        return

    @property
    def ref_bitfieldTextTableMaskSecond_(self):
        return self._artop_bitfieldTextTableMaskSecond

    @property
    def bitfieldTextTableMaskSecond_(self):
        if self._artop_bitfieldTextTableMaskSecond is not None:
            if hasattr(self._artop_bitfieldTextTableMaskSecond, "uuid"):
                return self._artop_bitfieldTextTableMaskSecond.uuid
        return

    @property
    def valuePairs_TextTableValuePair(self):
        return self._artop_valuePair
