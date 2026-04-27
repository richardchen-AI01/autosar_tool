# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MixedContentForVerbatim.py
from .WhitespaceControlled import WhitespaceControlled

class MixedContentForVerbatim(WhitespaceControlled):

    def __init__(self):
        super().__init__()
        from .Tt import Tt
        from .EmphasisText import EmphasisText
        from .Xref import Xref
        from .Br import Br
        self._artop_mixed = None
        self._artop_tt = []
        self._artop_e = []
        self._artop_xref = []
        self._artop_br = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_tt': '"TT"', 
         '_artop_e': '"EMPHASIS-TEXT"', 
         '_artop_xref': '"XREF"', 
         '_artop_br': '"BR"'})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def tts_Tt(self):
        return self._artop_tt

    @property
    def es_EmphasisText(self):
        return self._artop_e

    @property
    def xrefs_Xref(self):
        return self._artop_xref

    @property
    def brs_Br(self):
        return self._artop_br
