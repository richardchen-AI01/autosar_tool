# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwSystemconstDependentFormula.py
from .FormulaExpression import FormulaExpression

class SwSystemconstDependentFormula(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .SwSystemconst import SwSystemconst
        self._artop_syscStringRef = []
        self._artop_syscRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_syscStringRef':"SW-SYSTEMCONST", 
         '_artop_syscRef':"SW-SYSTEMCONST"})

    @property
    def ref_syscStrings_(self):
        return self._artop_syscStringRef

    @property
    def syscStrings_(self):
        return self._artop_syscStringRef

    @property
    def ref_syscs_(self):
        return self._artop_syscRef

    @property
    def syscs_(self):
        return self._artop_syscRef
