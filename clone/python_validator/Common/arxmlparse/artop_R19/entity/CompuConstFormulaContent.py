# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuConstFormulaContent.py
from .CompuConstContent import CompuConstContent

class CompuConstFormulaContent(CompuConstContent):

    def __init__(self):
        super().__init__()
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        self._artop_vf = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_vf": "NUMERICAL-VALUE-VARIATION-POINT"})

    @property
    def ref_vf_(self):
        return self._artop_vf

    @property
    def vf_(self):
        if self._artop_vf is not None:
            if hasattr(self._artop_vf, "uuid"):
                return self._artop_vf.uuid
        return
