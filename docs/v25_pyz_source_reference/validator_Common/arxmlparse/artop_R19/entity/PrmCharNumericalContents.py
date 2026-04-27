# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PrmCharNumericalContents.py
from .PrmCharContents import PrmCharContents

class PrmCharNumericalContents(PrmCharContents):

    def __init__(self):
        super().__init__()
        from .PrmCharNumericalValue import PrmCharNumericalValue
        from .SingleLanguageUnitNames import SingleLanguageUnitNames
        self._artop_prmCharNumericalValueType = None
        self._artop_prmUnit = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_prmCharNumericalValueType':"PRM-CHAR-NUMERICAL-VALUE", 
         '_artop_prmUnit':"SINGLE-LANGUAGE-UNIT-NAMES"})

    @property
    def ref_prmCharNumericalValueType_(self):
        return self._artop_prmCharNumericalValueType

    @property
    def prmCharNumericalValueType_(self):
        if self._artop_prmCharNumericalValueType is not None:
            if hasattr(self._artop_prmCharNumericalValueType, "uuid"):
                return self._artop_prmCharNumericalValueType.uuid
        return

    @property
    def ref_prmUnit_(self):
        return self._artop_prmUnit

    @property
    def prmUnit_(self):
        if self._artop_prmUnit is not None:
            if hasattr(self._artop_prmUnit, "uuid"):
                return self._artop_prmUnit.uuid
        return
