# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EnumerationMappingEntry.py
from .ARObject import ARObject

class EnumerationMappingEntry(ARObject):

    def __init__(self):
        super().__init__()
        from .EnumerationMappingTable import EnumerationMappingTable
        self._artop_numericalValue = None
        self._artop_enumeratorValue = None
        self._artop_enumerationMappingTable = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_enumerationMappingTable": "ENUMERATION-MAPPING-TABLE"})

    @property
    def numericalValue_(self):
        return self._artop_numericalValue

    @property
    def enumeratorValue_(self):
        return self._artop_enumeratorValue

    @property
    def ref_enumerationMappingTable_(self):
        return self._artop_enumerationMappingTable

    @property
    def enumerationMappingTable_(self):
        if self._artop_enumerationMappingTable is not None:
            if hasattr(self._artop_enumerationMappingTable, "uuid"):
                return self._artop_enumerationMappingTable.uuid
        return
