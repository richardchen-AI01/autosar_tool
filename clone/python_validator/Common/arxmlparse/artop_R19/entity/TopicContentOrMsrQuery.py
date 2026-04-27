# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TopicContentOrMsrQuery.py
from .ARObject import ARObject

class TopicContentOrMsrQuery(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryP1 import MsrQueryP1
        from .TopicContent import TopicContent
        self._artop_mixed = None
        self._artop_msrQueryP1 = []
        self._artop_topicContent = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_msrQueryP1':"MSR-QUERY-P-1", 
         '_artop_topicContent':"TOPIC-CONTENT"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def msrQueryP1s_MsrQueryP1(self):
        return self._artop_msrQueryP1

    @property
    def topicContents_TopicContent(self):
        return self._artop_topicContent
