# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucDerivationSpecification.py
from .ARObject import ARObject

class EcucDerivationSpecification(ARObject):

    def __init__(self):
        super().__init__()
        from .EcucParameterDef import EcucParameterDef
        from .EcucParameterDerivationFormula import EcucParameterDerivationFormula
        from .EcucQuery import EcucQuery
        from .MlFormula import MlFormula
        self._artop_ecucParameterDef = None
        self._artop_calculationFormula = None
        self._artop_ecucQuery = []
        self._artop_informalFormula = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ecucParameterDef': '"ECUC-PARAMETER-DEF"', 
         '_artop_calculationFormula': '"ECUC-PARAMETER-DERIVATION-FORMULA"', 
         '_artop_ecucQuery': '"ECUC-QUERY"', 
         '_artop_informalFormula': '"ML-FORMULA"'})

    @property
    def ref_ecucParameterDef_(self):
        return self._artop_ecucParameterDef

    @property
    def ecucParameterDef_(self):
        if self._artop_ecucParameterDef is not None:
            if hasattr(self._artop_ecucParameterDef, "uuid"):
                return self._artop_ecucParameterDef.uuid
        return

    @property
    def ref_calculationFormula_(self):
        return self._artop_calculationFormula

    @property
    def calculationFormula_(self):
        if self._artop_calculationFormula is not None:
            if hasattr(self._artop_calculationFormula, "uuid"):
                return self._artop_calculationFormula.uuid
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
