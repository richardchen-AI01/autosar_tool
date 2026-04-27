# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PrmChar.py
from .ARObject import ARObject

class PrmChar(ARObject):

    def __init__(self):
        super().__init__()
        from .GeneralParameter import GeneralParameter
        from .DocumentationBlock import DocumentationBlock
        from .PrmCharContents import PrmCharContents
        self._artop_generalParameter = None
        self._artop_cond = None
        self._artop_prmCharContents = None
        self._artop_remark = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_generalParameter': '"GENERAL-PARAMETER"', 
         '_artop_cond': '"DOCUMENTATION-BLOCK"', 
         '_artop_prmCharContents': '"PRM-CHAR-CONTENTS"', 
         '_artop_remark': '"DOCUMENTATION-BLOCK"'})

    @property
    def ref_generalParameter_(self):
        return self._artop_generalParameter

    @property
    def generalParameter_(self):
        if self._artop_generalParameter is not None:
            if hasattr(self._artop_generalParameter, "uuid"):
                return self._artop_generalParameter.uuid
        return

    @property
    def ref_cond_(self):
        return self._artop_cond

    @property
    def cond_(self):
        if self._artop_cond is not None:
            if hasattr(self._artop_cond, "uuid"):
                return self._artop_cond.uuid
        return

    @property
    def ref_prmCharContents_(self):
        return self._artop_prmCharContents

    @property
    def prmCharContents_(self):
        if self._artop_prmCharContents is not None:
            if hasattr(self._artop_prmCharContents, "uuid"):
                return self._artop_prmCharContents.uuid
        return

    @property
    def ref_remark_(self):
        return self._artop_remark

    @property
    def remark_(self):
        if self._artop_remark is not None:
            if hasattr(self._artop_remark, "uuid"):
                return self._artop_remark.uuid
        return
