# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EnumerationMappingTable.py
from .PackageableElement import PackageableElement

class EnumerationMappingTable(PackageableElement):

    def __init__(self):
        super().__init__()
        from .EnumerationMappingEntry import EnumerationMappingEntry
        self._artop_entry = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_entry": "ENUMERATION-MAPPING-ENTRY"})

    @property
    def entries_EnumerationMappingEntry(self):
        return self._artop_entry
