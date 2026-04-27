# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryChapter.py
from .Paginateable import Paginateable

class MsrQueryChapter(Paginateable):

    def __init__(self):
        super().__init__()
        from .ChapterOrMsrQuery import ChapterOrMsrQuery
        from .MsrQueryProps import MsrQueryProps
        from .MsrQueryResultChapter import MsrQueryResultChapter
        self._artop_chapterOrMsrQuery = None
        self._artop_msrQueryProps = None
        self._artop_msrQueryResultChapter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_chapterOrMsrQuery':"CHAPTER-OR-MSR-QUERY", 
         '_artop_msrQueryProps':"MSR-QUERY-PROPS", 
         '_artop_msrQueryResultChapter':"MSR-QUERY-RESULT-CHAPTER"})

    @property
    def ref_chapterOrMsrQuery_(self):
        return self._artop_chapterOrMsrQuery

    @property
    def chapterOrMsrQuery_(self):
        if self._artop_chapterOrMsrQuery is not None:
            if hasattr(self._artop_chapterOrMsrQuery, "uuid"):
                return self._artop_chapterOrMsrQuery.uuid
        return

    @property
    def ref_msrQueryProps_(self):
        return self._artop_msrQueryProps

    @property
    def msrQueryProps_(self):
        if self._artop_msrQueryProps is not None:
            if hasattr(self._artop_msrQueryProps, "uuid"):
                return self._artop_msrQueryProps.uuid
        return

    @property
    def ref_msrQueryResultChapter_(self):
        return self._artop_msrQueryResultChapter

    @property
    def msrQueryResultChapter_(self):
        if self._artop_msrQueryResultChapter is not None:
            if hasattr(self._artop_msrQueryResultChapter, "uuid"):
                return self._artop_msrQueryResultChapter.uuid
        return
