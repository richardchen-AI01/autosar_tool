# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TraceableTable.py
from .Traceable import Traceable
from .Paginateable import Paginateable
from .Identifiable import Identifiable

class TraceableTable(Identifiable, Paginateable, Traceable):

    def __init__(self):
        super().__init__()
        from .TopicContent import TopicContent
        from .Table import Table
        self._artop_topicContent = None
        self._artop_table = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_topicContent':"TOPIC-CONTENT", 
         '_artop_table':"TABLE"})

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
    def ref_table_(self):
        return self._artop_table

    @property
    def table_(self):
        if self._artop_table is not None:
            if hasattr(self._artop_table, "uuid"):
                return self._artop_table.uuid
        return
