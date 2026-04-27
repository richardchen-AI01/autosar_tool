# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LPlainText.py
from .MixedContentForPlainText import MixedContentForPlainText
from .LanguageSpecific import LanguageSpecific

class LPlainText(LanguageSpecific, MixedContentForPlainText):

    def __init__(self):
        super().__init__()
        from .MultiLanguagePlainText import MultiLanguagePlainText
        self._artop_multiLanguagePlainText = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_multiLanguagePlainText": "MULTI-LANGUAGE-PLAIN-TEXT"})

    @property
    def ref_multiLanguagePlainText_(self):
        return self._artop_multiLanguagePlainText

    @property
    def multiLanguagePlainText_(self):
        if self._artop_multiLanguagePlainText is not None:
            if hasattr(self._artop_multiLanguagePlainText, "uuid"):
                return self._artop_multiLanguagePlainText.uuid
        return
