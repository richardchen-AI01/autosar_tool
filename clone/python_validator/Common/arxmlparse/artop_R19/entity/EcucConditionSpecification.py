# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucConditionSpecification.py
from .ARObject import ARObject

class EcucConditionSpecification(ARObject):

    def __init__(self):
        super().__init__()
        from .EcucConditionFormula import EcucConditionFormula
        from .EcucQuery import EcucQuery
        from .MlFormula import MlFormula
        self._artop_conditionFormula = None
        self._artop_ecucQuery = []
        self._artop_informalFormula = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_conditionFormula':"ECUC-CONDITION-FORMULA", 
         '_artop_ecucQuery':"ECUC-QUERY", 
         '_artop_informalFormula':"ML-FORMULA"})

    @property
    def ref_conditionFormula_(self):
        return self._artop_conditionFormula

    @property
    def conditionFormula_(self):
        if self._artop_conditionFormula is not None:
            if hasattr(self._artop_conditionFormula, "uuid"):
                return self._artop_conditionFormula.uuid
        return

    @property
    def ecucQueries_EcucQuery(self):
        return self._artop_ecucQuery

    @property
    def ref_informalFormula_(self):
        return self._artop_informalFormula

    @property
    def informalFormula_(self):
        if self._artop_informalFormula is not None:
            if hasattr(self._artop_informalFormula, "uuid"):
                return self._artop_informalFormula.uuid
        return
