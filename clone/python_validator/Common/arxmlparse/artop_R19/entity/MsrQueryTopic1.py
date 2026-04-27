# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryTopic1.py
from .Paginateable import Paginateable

class MsrQueryTopic1(Paginateable):

    def __init__(self):
        super().__init__()
        from .TopicOrMsrQuery import TopicOrMsrQuery
        from .MsrQueryProps import MsrQueryProps
        from .MsrQueryResultTopic1 import MsrQueryResultTopic1
        self._artop_topicOrMsrQuery = None
        self._artop_msrQueryProps = None
        self._artop_msrQueryResultTopic1 = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_topicOrMsrQuery':"TOPIC-OR-MSR-QUERY", 
         '_artop_msrQueryProps':"MSR-QUERY-PROPS", 
         '_artop_msrQueryResultTopic1':"MSR-QUERY-RESULT-TOPIC-1"})

    @property
    def ref_topicOrMsrQuery_(self):
        return self._artop_topicOrMsrQuery

    @property
    def topicOrMsrQuery_(self):
        if self._artop_topicOrMsrQuery is not None:
            if hasattr(self._artop_topicOrMsrQuery, "uuid"):
                return self._artop_topicOrMsrQuery.uuid
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
    def ref_msrQueryResultTopic1_(self):
        return self._artop_msrQueryResultTopic1

    @property
    def msrQueryResultTopic1_(self):
        if self._artop_msrQueryResultTopic1 is not None:
            if hasattr(self._artop_msrQueryResultTopic1, "uuid"):
                return self._artop_msrQueryResultTopic1.uuid
        return
