# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucStringParamDef.py
from .EcucAbstractStringParamDef import EcucAbstractStringParamDef

class EcucStringParamDef(EcucAbstractStringParamDef):

    def __init__(self):
        super().__init__()
        from .EcucStringParamDefConditional import EcucStringParamDefConditional
        self._artop_ecucStringParamDefVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecucStringParamDefVariant": "ECUC-STRING-PARAM-DEF-CONDITIONAL"})

    @property
    def EcucStringParamDefVariants_EcucStringParamDefConditional(self):
        return self._artop_ecucStringParamDefVariant
