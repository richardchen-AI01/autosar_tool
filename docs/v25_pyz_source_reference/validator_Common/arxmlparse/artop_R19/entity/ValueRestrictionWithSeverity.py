# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ValueRestrictionWithSeverity.py
from .AbstractValueRestriction import AbstractValueRestriction
from .RestrictionWithSeverity import RestrictionWithSeverity

class ValueRestrictionWithSeverity(RestrictionWithSeverity, AbstractValueRestriction):

    def __init__(self):
        super().__init__()
        from .PrimitiveAttributeTailoring import PrimitiveAttributeTailoring
        self._artop_primitiveAttributeTailoring = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_primitiveAttributeTailoring": "PRIMITIVE-ATTRIBUTE-TAILORING"})

    @property
    def ref_primitiveAttributeTailoring_(self):
        return self._artop_primitiveAttributeTailoring

    @property
    def primitiveAttributeTailoring_(self):
        if self._artop_primitiveAttributeTailoring is not None:
            if hasattr(self._artop_primitiveAttributeTailoring, "uuid"):
                return self._artop_primitiveAttributeTailoring.uuid
        return
