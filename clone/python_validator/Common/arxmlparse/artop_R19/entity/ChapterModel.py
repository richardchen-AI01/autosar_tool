# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ChapterModel.py
from .ARObject import ARObject

class ChapterModel(ARObject):

    def __init__(self):
        super().__init__()
        from .ChapterContent import ChapterContent
        from .TopicOrMsrQuery import TopicOrMsrQuery
        from .ChapterOrMsrQuery import ChapterOrMsrQuery
        self._artop_chapterContent = None
        self._artop_topic1 = None
        self._artop_chapter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_chapterContent':"CHAPTER-CONTENT", 
         '_artop_topic1':"TOPIC-OR-MSR-QUERY", 
         '_artop_chapter':"CHAPTER-OR-MSR-QUERY"})

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
    def ref_topic1_(self):
        return self._artop_topic1

    @property
    def topic1_(self):
        if self._artop_topic1 is not None:
            if hasattr(self._artop_topic1, "uuid"):
                return self._artop_topic1.uuid
        return

    @property
    def ref_chapter_(self):
        return self._artop_chapter

    @property
    def chapter_(self):
        if self._artop_chapter is not None:
            if hasattr(self._artop_chapter, "uuid"):
                return self._artop_chapter.uuid
        return
