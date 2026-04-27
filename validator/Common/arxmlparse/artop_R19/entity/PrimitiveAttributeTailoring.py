# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PrimitiveAttributeTailoring.py
from .AttributeTailoring import AttributeTailoring

class PrimitiveAttributeTailoring(AttributeTailoring):

    def __init__(self):
        super().__init__()
        from .ValueRestrictionWithSeverity import ValueRestrictionWithSeverity
        self._artop_defaultValueHandling = None
        self._artop_primitiveAttributeTailoring = None
        self._artop_subAttributeTailoring = []
        self._artop_valueRestriction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_primitiveAttributeTailoring':"PRIMITIVE-ATTRIBUTE-TAILORING", 
         '_artop_subAttributeTailoring':"PRIMITIVE-ATTRIBUTE-TAILORING", 
         '_artop_valueRestriction':"VALUE-RESTRICTION-WITH-SEVERITY"})

    @property
    def defaultValueHandling_(self):
        return self._artop_defaultValueHandling

    @property
    def ref_primitiveAttributeTailoring_(self):
        return self._artop_primitiveAttributeTailoring

    @property
    def primitiveAttributeTailoring_(self):
        if self._artop_primitiveAttributeTailoring is not None:
            if hasattr(self._artop_primitiveAttributeTailoring, "uuid"):
                return self._artop_primitiveAttributeTailoring.uuid
        return

    @property
    def subAttributeTailorings_PrimitiveAttributeTailoring(self):
        return self._artop_subAttributeTailoring

    @property
    def ref_valueRestriction_(self):
        return self._artop_valueRestriction

    @property
    def valueRestriction_(self):
        if self._artop_valueRestriction is not None:
            if hasattr(self._artop_valueRestriction, "uuid"):
                return self._artop_valueRestriction.uuid
        return
