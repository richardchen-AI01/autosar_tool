# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Prms.py
from .Paginateable import Paginateable

class Prms(Paginateable):

    def __init__(self):
        super().__init__()
        from .ChapterContent import ChapterContent
        from .MultilanguageLongName import MultilanguageLongName
        from .GeneralParameter import GeneralParameter
        self._artop_chapterContent = None
        self._artop_label = None
        self._artop_prm = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_chapterContent':"CHAPTER-CONTENT", 
         '_artop_label':"MULTILANGUAGE-LONG-NAME", 
         '_artop_prm':"GENERAL-PARAMETER"})

    @property
    def ref_chapterContent_(self):
        return self._artop_chapterContent

    @property
    def chapterContent_(self):
        if self._artop_chapterContent is not None:
            if hasattr(self._artop_chapterContent, "uuid"):
                return self._artop_chapterContent.uuid
        return

    @property
    def ref_label_(self):
        return self._artop_label

    @property
    def label_(self):
        if self._artop_label is not None:
            if hasattr(self._artop_label, "uuid"):
                return self._artop_label.uuid
        return

    @property
    def prms_GeneralParameter(self):
        return self._artop_prm
