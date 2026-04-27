# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdgCaption.py
from .MultilanguageReferrable import MultilanguageReferrable

class SdgCaption(MultilanguageReferrable):

    def __init__(self):
        super().__init__()
        from .Sdg import Sdg
        from .MultiLanguageOverviewParagraph import MultiLanguageOverviewParagraph
        self._artop_sdg = None
        self._artop_desc = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sdg':"SDG", 
         '_artop_desc':"MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"})

    @property
    def ref_sdg_(self):
        return self._artop_sdg

    @property
    def sdg_(self):
        if self._artop_sdg is not None:
            if hasattr(self._artop_sdg, "uuid"):
                return self._artop_sdg.uuid
        return

    @property
    def ref_desc_(self):
        return self._artop_desc

    @property
    def desc_(self):
        if self._artop_desc is not None:
            if hasattr(self._artop_desc, "uuid"):
                return self._artop_desc.uuid
        return
