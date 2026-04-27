# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucMultilineStringParamDefConditional.py
from .EcucMultilineStringParamDefContent import EcucMultilineStringParamDefContent

class EcucMultilineStringParamDefConditional(EcucMultilineStringParamDefContent):

    def __init__(self):
        super().__init__()
        from .EcucMultilineStringParamDef import EcucMultilineStringParamDef
        from .VariationPoint import VariationPoint
        self._artop_ecucMultilineStringParamDef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucMultilineStringParamDef':"ECUC-MULTILINE-STRING-PARAM-DEF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_ecucMultilineStringParamDef_(self):
        return self._artop_ecucMultilineStringParamDef

    @property
    def ecucMultilineStringParamDef_(self):
        if self._artop_ecucMultilineStringParamDef is not None:
            if hasattr(self._artop_ecucMultilineStringParamDef, "uuid"):
                return self._artop_ecucMultilineStringParamDef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
