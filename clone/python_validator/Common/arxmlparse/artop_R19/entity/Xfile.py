# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Xfile.py
from .SingleLanguageReferrable import SingleLanguageReferrable

class Xfile(SingleLanguageReferrable):

    def __init__(self):
        super().__init__()
        from .MixedContentForParagraph import MixedContentForParagraph
        from .Url import Url
        self._artop_tool = None
        self._artop_toolVersion = None
        self._artop_mixedContentForParagraph = None
        self._artop_url = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_mixedContentForParagraph':"MIXED-CONTENT-FOR-PARAGRAPH", 
         '_artop_url':"URL"})

    @property
    def tool_(self):
        return self._artop_tool

    @property
    def toolVersion_(self):
        return self._artop_toolVersion

    @property
    def ref_mixedContentForParagraph_(self):
        return self._artop_mixedContentForParagraph

    @property
    def mixedContentForParagraph_(self):
        if self._artop_mixedContentForParagraph is not None:
            if hasattr(self._artop_mixedContentForParagraph, "uuid"):
                return self._artop_mixedContentForParagraph.uuid
        return

    @property
    def ref_url_(self):
        return self._artop_url

    @property
    def url_(self):
        if self._artop_url is not None:
            if hasattr(self._artop_url, "uuid"):
                return self._artop_url.uuid
        return
