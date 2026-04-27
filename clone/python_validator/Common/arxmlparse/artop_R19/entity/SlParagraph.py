# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SlParagraph.py
from .MixedContentForParagraph import MixedContentForParagraph

class SlParagraph(MixedContentForParagraph):

    def __init__(self):
        super().__init__()
        from .MixedContentForParagraph import MixedContentForParagraph
        self._artop_l = None
        self._artop_mixedContentForParagraph = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_mixedContentForParagraph": "MIXED-CONTENT-FOR-PARAGRAPH"})

    @property
    def l_(self):
        return self._artop_l

    @property
    def ref_mixedContentForParagraph_(self):
        return self._artop_mixedContentForParagraph

    @property
    def mixedContentForParagraph_(self):
        if self._artop_mixedContentForParagraph is not None:
            if hasattr(self._artop_mixedContentForParagraph, "uuid"):
                return self._artop_mixedContentForParagraph.uuid
        return
