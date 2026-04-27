# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucValidationCondition.py
from .Identifiable import Identifiable

class EcucValidationCondition(Identifiable):

    def __init__(self):
        super().__init__()
        from .EcucDefinitionElement import EcucDefinitionElement
        from .EcucQuery import EcucQuery
        from .EcucConditionFormula import EcucConditionFormula
        self._artop_ecucDefinitionElement = None
        self._artop_ecucQuery = []
        self._artop_validationFormula = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucDefinitionElement':"ECUC-DEFINITION-ELEMENT", 
         '_artop_ecucQuery':"ECUC-QUERY", 
         '_artop_validationFormula':"ECUC-CONDITION-FORMULA"})

    @property
    def ref_ecucDefinitionElement_(self):
        return self._artop_ecucDefinitionElement

    @property
    def ecucDefinitionElement_(self):
        if self._artop_ecucDefinitionElement is not None:
            if hasattr(self._artop_ecucDefinitionElement, "uuid"):
                return self._artop_ecucDefinitionElement.uuid
        return

    @property
    def ecucQueries_EcucQuery(self):
        return self._artop_ecucQuery

    @property
    def ref_validationFormula_(self):
        return self._artop_validationFormula

    @property
    def validationFormula_(self):
        if self._artop_validationFormula is not None:
            if hasattr(self._artop_validationFormula, "uuid"):
                return self._artop_validationFormula.uuid
        return
