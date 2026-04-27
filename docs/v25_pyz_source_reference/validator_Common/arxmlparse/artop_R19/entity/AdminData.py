# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AdminData.py
from .ARObject import ARObject

class AdminData(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiLanguagePlainText import MultiLanguagePlainText
        from .DocRevision import DocRevision
        from .Sdg import Sdg
        self._artop_language = None
        self._artop_usedLanguages = None
        self._artop_docRevision = []
        self._artop_sdg = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_usedLanguages':"MULTI-LANGUAGE-PLAIN-TEXT", 
         '_artop_docRevision':"DOC-REVISION", 
         '_artop_sdg':"SDG"})

    @property
    def language_(self):
        return self._artop_language

    @property
    def ref_usedLanguages_(self):
        return self._artop_usedLanguages

    @property
    def usedLanguages_(self):
        if self._artop_usedLanguages is not None:
            if hasattr(self._artop_usedLanguages, "uuid"):
                return self._artop_usedLanguages.uuid
        return

    @property
    def docRevisions_DocRevision(self):
        return self._artop_docRevision

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg
