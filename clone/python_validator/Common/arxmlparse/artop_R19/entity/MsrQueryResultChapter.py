# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryResultChapter.py
from .ARObject import ARObject

class MsrQueryResultChapter(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryChapter import MsrQueryChapter
        from .Chapter import Chapter
        self._artop_msrQueryChapter = None
        self._artop_chapter = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_msrQueryChapter':"MSR-QUERY-CHAPTER", 
         '_artop_chapter':"CHAPTER"})

    @property
    def ref_msrQueryChapter_(self):
        return self._artop_msrQueryChapter

    @property
    def msrQueryChapter_(self):
        if self._artop_msrQueryChapter is not None:
            if hasattr(self._artop_msrQueryChapter, "uuid"):
                return self._artop_msrQueryChapter.uuid
        return

    @property
    def chapters_Chapter(self):
        return self._artop_chapter
