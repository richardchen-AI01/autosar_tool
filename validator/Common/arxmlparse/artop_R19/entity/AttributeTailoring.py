# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AttributeTailoring.py
from .DataFormatElementScope import DataFormatElementScope

class AttributeTailoring(DataFormatElementScope):

    def __init__(self):
        super().__init__()
        from .ClassContentConditional import ClassContentConditional
        from .MultiplicityRestrictionWithSeverity import MultiplicityRestrictionWithSeverity
        from .VariationRestrictionWithSeverity import VariationRestrictionWithSeverity
        self._artop_classContentConditional = None
        self._artop_multiplicityRestriction = None
        self._artop_variationRestriction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_classContentConditional':"CLASS-CONTENT-CONDITIONAL", 
         '_artop_multiplicityRestriction':"MULTIPLICITY-RESTRICTION-WITH-SEVERITY", 
         '_artop_variationRestriction':"VARIATION-RESTRICTION-WITH-SEVERITY"})

    @property
    def ref_classContentConditional_(self):
        return self._artop_classContentConditional

    @property
    def classContentConditional_(self):
        if self._artop_classContentConditional is not None:
            if hasattr(self._artop_classContentConditional, "uuid"):
                return self._artop_classContentConditional.uuid
        return

    @property
    def ref_multiplicityRestriction_(self):
        return self._artop_multiplicityRestriction

    @property
    def multiplicityRestriction_(self):
        if self._artop_multiplicityRestriction is not None:
            if hasattr(self._artop_multiplicityRestriction, "uuid"):
                return self._artop_multiplicityRestriction.uuid
        return

    @property
    def ref_variationRestriction_(self):
        return self._artop_variationRestriction

    @property
    def variationRestriction_(self):
        if self._artop_variationRestriction is not None:
            if hasattr(self._artop_variationRestriction, "uuid"):
                return self._artop_variationRestriction.uuid
        return
