# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryResultTopic1.py
from .ARObject import ARObject

class MsrQueryResultTopic1(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryTopic1 import MsrQueryTopic1
        from .Topic1 import Topic1
        self._artop_msrQueryTopic1 = None
        self._artop_topic1 = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_msrQueryTopic1':"MSR-QUERY-TOPIC-1", 
         '_artop_topic1':"TOPIC-1"})

    @property
    def ref_msrQueryTopic1_(self):
        return self._artop_msrQueryTopic1

    @property
    def msrQueryTopic1_(self):
        if self._artop_msrQueryTopic1 is not None:
            if hasattr(self._artop_msrQueryTopic1, "uuid"):
                return self._artop_msrQueryTopic1.uuid
        return

    @property
    def topic1s_Topic1(self):
        return self._artop_topic1
