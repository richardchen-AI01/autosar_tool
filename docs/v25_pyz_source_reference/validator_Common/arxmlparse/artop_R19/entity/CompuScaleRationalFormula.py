# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuScaleRationalFormula.py
from .CompuScaleContents import CompuScaleContents

class CompuScaleRationalFormula(CompuScaleContents):

    def __init__(self):
        super().__init__()
        from .CompuRationalCoeffs import CompuRationalCoeffs
        self._artop_compuRationalCoeffs = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compuRationalCoeffs": "COMPU-RATIONAL-COEFFS"})

    @property
    def ref_compuRationalCoeffs_(self):
        return self._artop_compuRationalCoeffs

    @property
    def compuRationalCoeffs_(self):
        if self._artop_compuRationalCoeffs is not None:
            if hasattr(self._artop_compuRationalCoeffs, "uuid"):
                return self._artop_compuRationalCoeffs.uuid
        return
