# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ChapterOrMsrQuery.py
from .ARObject import ARObject

class ChapterOrMsrQuery(ARObject):

    def __init__(self):
        super().__init__()
        from .ChapterModel import ChapterModel
        from .Chapter import Chapter
        from .MsrQueryChapter import MsrQueryChapter
        self._artop_mixed = None
        self._artop_chapterModel = None
        self._artop_chapter = []
        self._artop_msrQueryChapter = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_chapterModel':"CHAPTER-MODEL", 
         '_artop_chapter':"CHAPTER", 
         '_artop_msrQueryChapter':"MSR-QUERY-CHAPTER"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_chapterModel_(self):
        return self._artop_chapterModel

    @property
    def chapterModel_(self):
        if self._artop_chapterModel is not None:
            if hasattr(self._artop_chapterModel, "uuid"):
                return self._artop_chapterModel.uuid
        return

    @property
    def chapters_Chapter(self):
        return self._artop_chapter

    @property
    def msrQueryChapters_MsrQueryChapter(self):
        return self._artop_msrQueryChapter
