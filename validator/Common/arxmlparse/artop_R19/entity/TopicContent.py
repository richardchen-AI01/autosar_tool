# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TopicContent.py
from .ARObject import ARObject

class TopicContent(ARObject):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .Table import Table
        from .TraceableTable import TraceableTable
        self._artop_mixed = None
        self._artop_blockLevelContent = []
        self._artop_table = []
        self._artop_traceableTable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_blockLevelContent':"DOCUMENTATION-BLOCK", 
         '_artop_table':"TABLE", 
         '_artop_traceableTable':"TRACEABLE-TABLE"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def blockLevelContents_DocumentationBlock(self):
        return self._artop_blockLevelContent

    @property
    def tables_Table(self):
        return self._artop_table

    @property
    def traceableTables_TraceableTable(self):
        return self._artop_traceableTable
