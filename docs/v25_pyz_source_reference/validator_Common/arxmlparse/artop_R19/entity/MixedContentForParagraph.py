# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MixedContentForParagraph.py
from .ARObject import ARObject

class MixedContentForParagraph(ARObject):

    def __init__(self):
        super().__init__()
        from .SlParagraph import SlParagraph
        from .Traceable import Traceable
        from .Tt import Tt
        from .Br import Br
        from .Xref import Xref
        from .XrefTarget import XrefTarget
        from .EmphasisText import EmphasisText
        from .IndexEntry import IndexEntry
        from .Std import Std
        from .Xdoc import Xdoc
        from .Xfile import Xfile
        self._artop_sup = None
        self._artop_sub = None
        self._artop_mixed = None
        self._artop_ft = []
        self._artop_traceRef = []
        self._artop_tt = []
        self._artop_br = []
        self._artop_xref = []
        self._artop_xrefTarget = []
        self._artop_e = []
        self._artop_ie = []
        self._artop_std = []
        self._artop_xdoc = []
        self._artop_xfile = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ft': '"SL-PARAGRAPH"', 
         '_artop_traceRef': '"TRACEABLE"', 
         '_artop_tt': '"TT"', 
         '_artop_br': '"BR"', 
         '_artop_xref': '"XREF"', 
         '_artop_xrefTarget': '"XREF-TARGET"', 
         '_artop_e': '"EMPHASIS-TEXT"', 
         '_artop_ie': '"INDEX-ENTRY"', 
         '_artop_std': '"STD"', 
         '_artop_xdoc': '"XDOC"', 
         '_artop_xfile': '"XFILE"'})

    @property
    def sup_(self):
        return self._artop_sup

    @property
    def sub_(self):
        return self._artop_sub

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def fts_SlParagraph(self):
        return self._artop_ft

    @property
    def ref_traces_(self):
        return self._artop_traceRef

    @property
    def traces_(self):
        return self._artop_traceRef

    @property
    def tts_Tt(self):
        return self._artop_tt

    @property
    def brs_Br(self):
        return self._artop_br

    @property
    def xrefs_Xref(self):
        return self._artop_xref

    @property
    def xrefTargets_XrefTarget(self):
        return self._artop_xrefTarget

    @property
    def es_EmphasisText(self):
        return self._artop_e

    @property
    def ies_IndexEntry(self):
        return self._artop_ie

    @property
    def stds_Std(self):
        return self._artop_std

    @property
    def xdocs_Xdoc(self):
        return self._artop_xdoc

    @property
    def xfiles_Xfile(self):
        return self._artop_xfile
