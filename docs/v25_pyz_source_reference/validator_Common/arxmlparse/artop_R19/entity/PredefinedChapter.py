# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PredefinedChapter.py
from .ARObject import ARObject

class PredefinedChapter(ARObject):

    def __init__(self):
        super().__init__()
        from .Documentation import Documentation
        from .ChapterModel import ChapterModel
        self._artop_documentation = None
        self._artop_chapterModel = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_documentation':"DOCUMENTATION", 
         '_artop_chapterModel':"CHAPTER-MODEL"})

    @property
    def ref_documentation_(self):
        return self._artop_documentation

    @property
    def documentation_(self):
        if self._artop_documentation is not None:
            if hasattr(self._artop_documentation, "uuid"):
                return self._artop_documentation.uuid
        return

    @property
    def ref_chapterModel_(self):
        return self._artop_chapterModel

    @property
    def chapterModel_(self):
        if self._artop_chapterModel is not None:
            if hasattr(self._artop_chapterModel, "uuid"):
                return self._artop_chapterModel.uuid
        return
