# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintFormula.py
from .SwSystemconstDependentFormula import SwSystemconstDependentFormula

class BlueprintFormula(SwSystemconstDependentFormula):

    def __init__(self):
        super().__init__()
        from .VariationPoint import VariationPoint
        from .EcucQuery import EcucQuery
        from .EcucDefinitionElement import EcucDefinitionElement
        from .MultiLanguageVerbatim import MultiLanguageVerbatim
        self._artop_variationPoint = None
        self._artop_ecucQueryRef = []
        self._artop_ecucRef = []
        self._artop_verbatim = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_variationPoint': '"VARIATION-POINT"', 
         '_artop_ecucQueryRef': '"ECUC-QUERY"', 
         '_artop_ecucRef': '"ECUC-DEFINITION-ELEMENT"', 
         '_artop_verbatim': '"MULTI-LANGUAGE-VERBATIM"'})

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

    @property
    def ref_ecucQueries_(self):
        return self._artop_ecucQueryRef

    @property
    def ecucQueries_(self):
        return self._artop_ecucQueryRef

    @property
    def ref_ecucs_(self):
        return self._artop_ecucRef

    @property
    def ecucs_(self):
        return self._artop_ecucRef

    @property
    def verbatims_MultiLanguageVerbatim(self):
        return self._artop_verbatim
