# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariationPoint.py
from .ARObject import ARObject

class VariationPoint(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        from .DocumentationBlock import DocumentationBlock
        from .BlueprintFormula import BlueprintFormula
        from .BlueprintGenerator import BlueprintGenerator
        from .ConditionByFormula import ConditionByFormula
        from .PostBuildVariantCondition import PostBuildVariantCondition
        from .Sdg import Sdg
        self._artop_shortLabel = None
        self._artop_desc = None
        self._artop_blueprintCondition = None
        self._artop_formalBlueprintCondition = None
        self._artop_formalBlueprintGenerator = None
        self._artop_swSyscond = None
        self._artop_postBuildVariantCondition = []
        self._artop_sdg = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_desc': '"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"', 
         '_artop_blueprintCondition': '"DOCUMENTATION-BLOCK"', 
         '_artop_formalBlueprintCondition': '"BLUEPRINT-FORMULA"', 
         '_artop_formalBlueprintGenerator': '"BLUEPRINT-GENERATOR"', 
         '_artop_swSyscond': '"CONDITION-BY-FORMULA"', 
         '_artop_postBuildVariantCondition': '"POST-BUILD-VARIANT-CONDITION"', 
         '_artop_sdg': '"SDG"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_desc_(self):
        return self._artop_desc

    @property
    def desc_(self):
        if self._artop_desc is not None:
            if hasattr(self._artop_desc, "uuid"):
                return self._artop_desc.uuid
        return

    @property
    def ref_blueprintCondition_(self):
        return self._artop_blueprintCondition

    @property
    def blueprintCondition_(self):
        if self._artop_blueprintCondition is not None:
            if hasattr(self._artop_blueprintCondition, "uuid"):
                return self._artop_blueprintCondition.uuid
        return

    @property
    def ref_formalBlueprintCondition_(self):
        return self._artop_formalBlueprintCondition

    @property
    def formalBlueprintCondition_(self):
        if self._artop_formalBlueprintCondition is not None:
            if hasattr(self._artop_formalBlueprintCondition, "uuid"):
                return self._artop_formalBlueprintCondition.uuid
        return

    @property
    def ref_formalBlueprintGenerator_(self):
        return self._artop_formalBlueprintGenerator

    @property
    def formalBlueprintGenerator_(self):
        if self._artop_formalBlueprintGenerator is not None:
            if hasattr(self._artop_formalBlueprintGenerator, "uuid"):
                return self._artop_formalBlueprintGenerator.uuid
        return

    @property
    def ref_swSyscond_(self):
        return self._artop_swSyscond

    @property
    def swSyscond_(self):
        if self._artop_swSyscond is not None:
            if hasattr(self._artop_swSyscond, "uuid"):
                return self._artop_swSyscond.uuid
        return

    @property
    def postBuildVariantConditions_PostBuildVariantCondition(self):
        return self._artop_postBuildVariantCondition

    @property
    def ref_sdg_(self):
        return self._artop_sdg

    @property
    def sdg_(self):
        if self._artop_sdg is not None:
            if hasattr(self._artop_sdg, "uuid"):
                return self._artop_sdg.uuid
        return
