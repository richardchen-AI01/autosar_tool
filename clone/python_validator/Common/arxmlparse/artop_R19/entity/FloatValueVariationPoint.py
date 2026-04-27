# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FloatValueVariationPoint.py
from .AttributeValueVariationPoint import AttributeValueVariationPoint

class FloatValueVariationPoint(AttributeValueVariationPoint):

    def __init__(self):
        super().__init__()
        from .EcucFloatParamDef import EcucFloatParamDef
        self._artop_ecucFloatParamDef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecucFloatParamDef": "ECUC-FLOAT-PARAM-DEF"})

    @property
    def ref_ecucFloatParamDef_(self):
        return self._artop_ecucFloatParamDef

    @property
    def ecucFloatParamDef_(self):
        if self._artop_ecucFloatParamDef is not None:
            if hasattr(self._artop_ecucFloatParamDef, "uuid"):
                return self._artop_ecucFloatParamDef.uuid
        return
