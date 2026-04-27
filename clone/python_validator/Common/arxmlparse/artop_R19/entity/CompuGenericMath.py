# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuGenericMath.py
from .FormulaExpression import FormulaExpression

class CompuGenericMath(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .SwDataDependency import SwDataDependency
        self._artop_level = None
        self._artop_swDataDependency = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swDataDependency": "SW-DATA-DEPENDENCY"})

    @property
    def level_(self):
        return self._artop_level

    @property
    def ref_swDataDependency_(self):
        return self._artop_swDataDependency

    @property
    def swDataDependency_(self):
        if self._artop_swDataDependency is not None:
            if hasattr(self._artop_swDataDependency, "uuid"):
                return self._artop_swDataDependency.uuid
        return
