# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucEnumerationLiteralDef.py
from .Identifiable import Identifiable

class EcucEnumerationLiteralDef(Identifiable):

    def __init__(self):
        super().__init__()
        from .EcucEnumerationParamDef import EcucEnumerationParamDef
        from .EcucConditionSpecification import EcucConditionSpecification
        self._artop_origin = None
        self._artop_ecucEnumerationParamDef = None
        self._artop_ecucCond = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucEnumerationParamDef':"ECUC-ENUMERATION-PARAM-DEF", 
         '_artop_ecucCond':"ECUC-CONDITION-SPECIFICATION"})

    @property
    def origin_(self):
        return self._artop_origin

    @property
    def ref_ecucEnumerationParamDef_(self):
        return self._artop_ecucEnumerationParamDef

    @property
    def ecucEnumerationParamDef_(self):
        if self._artop_ecucEnumerationParamDef is not None:
            if hasattr(self._artop_ecucEnumerationParamDef, "uuid"):
                return self._artop_ecucEnumerationParamDef.uuid
        return

    @property
    def ref_ecucCond_(self):
        return self._artop_ecucCond

    @property
    def ecucCond_(self):
        if self._artop_ecucCond is not None:
            if hasattr(self._artop_ecucCond, "uuid"):
                return self._artop_ecucCond.uuid
        return
