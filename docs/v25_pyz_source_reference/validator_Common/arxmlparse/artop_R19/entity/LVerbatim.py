# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LVerbatim.py
from .MixedContentForVerbatim import MixedContentForVerbatim
from .LanguageSpecific import LanguageSpecific

class LVerbatim(LanguageSpecific, MixedContentForVerbatim):

    def __init__(self):
        super().__init__()
        from .MultiLanguageVerbatim import MultiLanguageVerbatim
        self._artop_multiLanguageVerbatim = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_multiLanguageVerbatim": "MULTI-LANGUAGE-VERBATIM"})

    @property
    def ref_multiLanguageVerbatim_(self):
        return self._artop_multiLanguageVerbatim

    @property
    def multiLanguageVerbatim_(self):
        if self._artop_multiLanguageVerbatim is not None:
            if hasattr(self._artop_multiLanguageVerbatim, "uuid"):
                return self._artop_multiLanguageVerbatim.uuid
        return
