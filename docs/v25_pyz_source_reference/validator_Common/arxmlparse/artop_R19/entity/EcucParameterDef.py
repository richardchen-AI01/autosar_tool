# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucParameterDef.py
from .EcucCommonAttributes import EcucCommonAttributes

class EcucParameterDef(EcucCommonAttributes):

    def __init__(self):
        super().__init__()
        from .EcucDerivationSpecification import EcucDerivationSpecification
        self._artop_symbolicNameValue = None
        self._artop_withAuto = None
        self._artop_derivation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_derivation": "ECUC-DERIVATION-SPECIFICATION"})

    @property
    def symbolicNameValue_(self):
        if self._artop_symbolicNameValue:
            if self._artop_symbolicNameValue == "true":
                return True
            return False
        else:
            return self._artop_symbolicNameValue

    @property
    def withAuto_(self):
        if self._artop_withAuto:
            if self._artop_withAuto == "true":
                return True
            return False
        else:
            return self._artop_withAuto

    @property
    def ref_derivation_(self):
        return self._artop_derivation

    @property
    def derivation_(self):
        if self._artop_derivation is not None:
            if hasattr(self._artop_derivation, "uuid"):
                return self._artop_derivation.uuid
        return
