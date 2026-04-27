# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryP1.py
from .Paginateable import Paginateable

class MsrQueryP1(Paginateable):

    def __init__(self):
        super().__init__()
        from .TopicContentOrMsrQuery import TopicContentOrMsrQuery
        from .MsrQueryProps import MsrQueryProps
        from .TopicContent import TopicContent
        self._artop_topicContentOrMsrQuery = None
        self._artop_msrQueryProps = None
        self._artop_msrQueryResultP1 = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_topicContentOrMsrQuery':"TOPIC-CONTENT-OR-MSR-QUERY", 
         '_artop_msrQueryProps':"MSR-QUERY-PROPS", 
         '_artop_msrQueryResultP1':"TOPIC-CONTENT"})

    @property
    def ref_topicContentOrMsrQuery_(self):
        return self._artop_topicContentOrMsrQuery

    @property
    def topicContentOrMsrQuery_(self):
        if self._artop_topicContentOrMsrQuery is not None:
            if hasattr(self._artop_topicContentOrMsrQuery, "uuid"):
                return self._artop_topicContentOrMsrQuery.uuid
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
    def ref_msrQueryResultP1_(self):
        return self._artop_msrQueryResultP1

    @property
    def msrQueryResultP1_(self):
        if self._artop_msrQueryResultP1 is not None:
            if hasattr(self._artop_msrQueryResultP1, "uuid"):
                return self._artop_msrQueryResultP1.uuid
        return
