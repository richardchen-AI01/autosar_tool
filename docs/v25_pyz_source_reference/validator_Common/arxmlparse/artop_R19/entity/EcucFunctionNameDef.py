# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucFunctionNameDef.py
from .EcucAbstractStringParamDef import EcucAbstractStringParamDef

class EcucFunctionNameDef(EcucAbstractStringParamDef):

    def __init__(self):
        super().__init__()
        from .EcucFunctionNameDefConditional import EcucFunctionNameDefConditional
        self._artop_ecucFunctionNameDefVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecucFunctionNameDefVariant": "ECUC-FUNCTION-NAME-DEF-CONDITIONAL"})

    @property
    def EcucFunctionNameDefVariants_EcucFunctionNameDefConditional(self):
        return self._artop_ecucFunctionNameDefVariant
