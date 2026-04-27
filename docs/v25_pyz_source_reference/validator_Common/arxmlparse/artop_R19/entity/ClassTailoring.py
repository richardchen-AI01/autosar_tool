# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClassTailoring.py
from .ARObject import ARObject

class ClassTailoring(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiplicityRestrictionWithSeverity import MultiplicityRestrictionWithSeverity
        from .VariationRestrictionWithSeverity import VariationRestrictionWithSeverity
        from .ClassContentConditional import ClassContentConditional
        self._artop_multiplicityRestriction = None
        self._artop_variationRestriction = None
        self._artop_classContent = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_multiplicityRestriction':"MULTIPLICITY-RESTRICTION-WITH-SEVERITY", 
         '_artop_variationRestriction':"VARIATION-RESTRICTION-WITH-SEVERITY", 
         '_artop_classContent':"CLASS-CONTENT-CONDITIONAL"})

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

    @property
    def classContents_ClassContentConditional(self):
        return self._artop_classContent
