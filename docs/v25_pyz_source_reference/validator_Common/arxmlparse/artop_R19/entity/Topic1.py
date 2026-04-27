# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Topic1.py
from .Paginateable import Paginateable
from .Identifiable import Identifiable

class Topic1(Identifiable, Paginateable):

    def __init__(self):
        super().__init__()
        from .TopicContentOrMsrQuery import TopicContentOrMsrQuery
        from .VariationPoint import VariationPoint
        self._artop_helpEntry = None
        self._artop_topicContent = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_topicContent':"TOPIC-CONTENT-OR-MSR-QUERY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def helpEntry_(self):
        return self._artop_helpEntry

    @property
    def ref_topicContent_(self):
        return self._artop_topicContent

    @property
    def topicContent_(self):
        if self._artop_topicContent is not None:
            if hasattr(self._artop_topicContent, "uuid"):
                return self._artop_topicContent.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
