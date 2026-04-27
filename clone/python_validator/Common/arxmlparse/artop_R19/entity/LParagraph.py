# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LParagraph.py
from .MixedContentForParagraph import MixedContentForParagraph
from .LanguageSpecific import LanguageSpecific

class LParagraph(LanguageSpecific, MixedContentForParagraph):

    def __init__(self):
        super().__init__()
        from .MultiLanguageParagraph import MultiLanguageParagraph
        self._artop_multiLanguageParagraph = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_multiLanguageParagraph": "MULTI-LANGUAGE-PARAGRAPH"})

    @property
    def ref_multiLanguageParagraph_(self):
        return self._artop_multiLanguageParagraph

    @property
    def multiLanguageParagraph_(self):
        if self._artop_multiLanguageParagraph is not None:
            if hasattr(self._artop_multiLanguageParagraph, "uuid"):
                return self._artop_multiLanguageParagraph.uuid
        return
