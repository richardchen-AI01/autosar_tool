# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TextTableValuePair.py
from .ARObject import ARObject

class TextTableValuePair(ARObject):

    def __init__(self):
        super().__init__()
        from .TextTableMapping import TextTableMapping
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        self._artop_textTableMapping = None
        self._artop_firstValue = None
        self._artop_secondValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_textTableMapping':"TEXT-TABLE-MAPPING", 
         '_artop_firstValue':"NUMERICAL-VALUE-VARIATION-POINT", 
         '_artop_secondValue':"NUMERICAL-VALUE-VARIATION-POINT"})

    @property
    def ref_textTableMapping_(self):
        return self._artop_textTableMapping

    @property
    def textTableMapping_(self):
        if self._artop_textTableMapping is not None:
            if hasattr(self._artop_textTableMapping, "uuid"):
                return self._artop_textTableMapping.uuid
        return

    @property
    def ref_firstValue_(self):
        return self._artop_firstValue

    @property
    def firstValue_(self):
        if self._artop_firstValue is not None:
            if hasattr(self._artop_firstValue, "uuid"):
                return self._artop_firstValue.uuid
        return

    @property
    def ref_secondValue_(self):
        return self._artop_secondValue

    @property
    def secondValue_(self):
        if self._artop_secondValue is not None:
            if hasattr(self._artop_secondValue, "uuid"):
                return self._artop_secondValue.uuid
        return
