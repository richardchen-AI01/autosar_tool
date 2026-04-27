# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DynamicPart.py
from .MultiplexedPart import MultiplexedPart

class DynamicPart(MultiplexedPart):

    def __init__(self):
        super().__init__()
        from .MultiplexedIPdu import MultiplexedIPdu
        from .DynamicPartAlternative import DynamicPartAlternative
        from .VariationPoint import VariationPoint
        self._artop_multiplexedIPdu = None
        self._artop_dynamicPartAlternative = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_multiplexedIPdu':"MULTIPLEXED-I-PDU", 
         '_artop_dynamicPartAlternative':"DYNAMIC-PART-ALTERNATIVE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_multiplexedIPdu_(self):
        return self._artop_multiplexedIPdu

    @property
    def multiplexedIPdu_(self):
        if self._artop_multiplexedIPdu is not None:
            if hasattr(self._artop_multiplexedIPdu, "uuid"):
                return self._artop_multiplexedIPdu.uuid
        return

    @property
    def dynamicPartAlternatives_DynamicPartAlternative(self):
        return self._artop_dynamicPartAlternative

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
