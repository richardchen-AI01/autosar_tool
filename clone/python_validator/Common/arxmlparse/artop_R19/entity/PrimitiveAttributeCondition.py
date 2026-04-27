# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PrimitiveAttributeCondition.py
from .AbstractValueRestriction import AbstractValueRestriction
from .AttributeCondition import AttributeCondition

class PrimitiveAttributeCondition(AttributeCondition, AbstractValueRestriction):

    def __init__(self):
        super().__init__()
        from .PrimitiveAttributeTailoring import PrimitiveAttributeTailoring
        self._artop_attributeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_attributeRef": "PRIMITIVE-ATTRIBUTE-TAILORING"})

    @property
    def ref_attribute_(self):
        return self._artop_attributeRef

    @property
    def attribute_(self):
        if self._artop_attributeRef is not None:
            if hasattr(self._artop_attributeRef, "uuid"):
                return self._artop_attributeRef.uuid
        return
