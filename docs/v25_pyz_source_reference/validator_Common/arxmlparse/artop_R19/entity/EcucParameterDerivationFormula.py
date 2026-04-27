# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucParameterDerivationFormula.py
from .FormulaExpression import FormulaExpression

class EcucParameterDerivationFormula(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .EcucDerivationSpecification import EcucDerivationSpecification
        from .EcucQuery import EcucQuery
        self._artop_ecucDerivationSpecification = None
        self._artop_ecucQueryRef = []
        self._artop_ecucQueryStringRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucDerivationSpecification':"ECUC-DERIVATION-SPECIFICATION", 
         '_artop_ecucQueryRef':"ECUC-QUERY", 
         '_artop_ecucQueryStringRef':"ECUC-QUERY"})

    @property
    def ref_ecucDerivationSpecification_(self):
        return self._artop_ecucDerivationSpecification

    @property
    def ecucDerivationSpecification_(self):
        if self._artop_ecucDerivationSpecification is not None:
            if hasattr(self._artop_ecucDerivationSpecification, "uuid"):
                return self._artop_ecucDerivationSpecification.uuid
        return

    @property
    def ref_ecucQueries_(self):
        return self._artop_ecucQueryRef

    @property
    def ecucQueries_(self):
        return self._artop_ecucQueryRef

    @property
    def ref_ecucQueryStrings_(self):
        return self._artop_ecucQueryStringRef

    @property
    def ecucQueryStrings_(self):
        return self._artop_ecucQueryStringRef
