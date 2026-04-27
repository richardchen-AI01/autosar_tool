# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuScaleConstantContents.py
from .CompuScaleContents import CompuScaleContents

class CompuScaleConstantContents(CompuScaleContents):

    def __init__(self):
        super().__init__()
        from .CompuConst import CompuConst
        self._artop_compuConst = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compuConst": "COMPU-CONST"})

    @property
    def ref_compuConst_(self):
        return self._artop_compuConst

    @property
    def compuConst_(self):
        if self._artop_compuConst is not None:
            if hasattr(self._artop_compuConst, "uuid"):
                return self._artop_compuConst.uuid
        return
