# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuRationalCoeffs.py
from .ARObject import ARObject

class CompuRationalCoeffs(ARObject):

    def __init__(self):
        super().__init__()
        from .CompuScaleRationalFormula import CompuScaleRationalFormula
        from .CompuNominatorDenominator import CompuNominatorDenominator
        self._artop_compuScaleRationalFormula = None
        self._artop_compuNumerator = None
        self._artop_compuDenominator = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_compuScaleRationalFormula':"COMPU-SCALE-RATIONAL-FORMULA", 
         '_artop_compuNumerator':"COMPU-NOMINATOR-DENOMINATOR", 
         '_artop_compuDenominator':"COMPU-NOMINATOR-DENOMINATOR"})

    @property
    def ref_compuScaleRationalFormula_(self):
        return self._artop_compuScaleRationalFormula

    @property
    def compuScaleRationalFormula_(self):
        if self._artop_compuScaleRationalFormula is not None:
            if hasattr(self._artop_compuScaleRationalFormula, "uuid"):
                return self._artop_compuScaleRationalFormula.uuid
        return

    @property
    def ref_compuNumerator_(self):
        return self._artop_compuNumerator

    @property
    def compuNumerator_(self):
        if self._artop_compuNumerator is not None:
            if hasattr(self._artop_compuNumerator, "uuid"):
                return self._artop_compuNumerator.uuid
        return

    @property
    def ref_compuDenominator_(self):
        return self._artop_compuDenominator

    @property
    def compuDenominator_(self):
        if self._artop_compuDenominator is not None:
            if hasattr(self._artop_compuDenominator, "uuid"):
                return self._artop_compuDenominator.uuid
        return
