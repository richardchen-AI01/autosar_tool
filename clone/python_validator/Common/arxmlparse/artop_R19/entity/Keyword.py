# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Keyword.py
from .Identifiable import Identifiable

class Keyword(Identifiable):

    def __init__(self):
        super().__init__()
        from .KeywordSet import KeywordSet
        self._artop_abbrName = None
        self._artop_classification = None
        self._artop_keywordSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_keywordSet": "KEYWORD-SET"})

    @property
    def abbrName_(self):
        return self._artop_abbrName

    @property
    def classification_(self):
        return self._artop_classification

    @property
    def ref_keywordSet_(self):
        return self._artop_keywordSet

    @property
    def keywordSet_(self):
        if self._artop_keywordSet is not None:
            if hasattr(self._artop_keywordSet, "uuid"):
                return self._artop_keywordSet.uuid
        return
