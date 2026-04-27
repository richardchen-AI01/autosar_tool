# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GeneralParameter.py
from .Identifiable import Identifiable

class GeneralParameter(Identifiable):

    def __init__(self):
        super().__init__()
        from .Prms import Prms
        from .PrmChar import PrmChar
        self._artop_prms = None
        self._artop_prmChar = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_prms':"PRMS", 
         '_artop_prmChar':"PRM-CHAR"})

    @property
    def ref_prms_(self):
        return self._artop_prms

    @property
    def prms_(self):
        if self._artop_prms is not None:
            if hasattr(self._artop_prms, "uuid"):
                return self._artop_prms.uuid
        return

    @property
    def prmChars_PrmChar(self):
        return self._artop_prmChar
