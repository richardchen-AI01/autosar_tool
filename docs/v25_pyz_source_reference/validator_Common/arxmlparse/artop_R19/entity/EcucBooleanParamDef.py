# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucBooleanParamDef.py
from .EcucParameterDef import EcucParameterDef

class EcucBooleanParamDef(EcucParameterDef):

    def __init__(self):
        super().__init__()
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        self._artop_defaultValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_defaultValue": "BOOLEAN-VALUE-VARIATION-POINT"})

    @property
    def ref_defaultValue_(self):
        return self._artop_defaultValue

    @property
    def defaultValue_(self):
        if self._artop_defaultValue is not None:
            if hasattr(self._artop_defaultValue, "uuid"):
                return self._artop_defaultValue.uuid
        return
