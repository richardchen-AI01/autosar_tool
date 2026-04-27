# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McGroupDataRefSetContent.py
from .ARObject import ARObject

class McGroupDataRefSetContent(ARObject):

    def __init__(self):
        super().__init__()
        from .FlatInstanceDescriptor import FlatInstanceDescriptor
        from .McDataInstance import McDataInstance
        self._artop_flatMapEntryRef = []
        self._artop_mcDataInstanceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flatMapEntryRef':"FLAT-INSTANCE-DESCRIPTOR", 
         '_artop_mcDataInstanceRef':"MC-DATA-INSTANCE"})

    @property
    def ref_flatMapEntries_(self):
        return self._artop_flatMapEntryRef

    @property
    def flatMapEntries_(self):
        return self._artop_flatMapEntryRef

    @property
    def ref_mcDataInstances_(self):
        return self._artop_mcDataInstanceRef

    @property
    def mcDataInstances_(self):
        return self._artop_mcDataInstanceRef
