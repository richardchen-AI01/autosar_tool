# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvBlockSwComponentType.py
from .AtomicSwComponentType import AtomicSwComponentType

class NvBlockSwComponentType(AtomicSwComponentType):

    def __init__(self):
        super().__init__()
        from .BulkNvDataDescriptor import BulkNvDataDescriptor
        from .NvBlockDescriptor import NvBlockDescriptor
        self._artop_bulkNvDataDescriptor = []
        self._artop_nvBlockDescriptor = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bulkNvDataDescriptor':"BULK-NV-DATA-DESCRIPTOR", 
         '_artop_nvBlockDescriptor':"NV-BLOCK-DESCRIPTOR"})

    @property
    def bulkNvDataDescriptors_BulkNvDataDescriptor(self):
        return self._artop_bulkNvDataDescriptor

    @property
    def nvBlockDescriptors_NvBlockDescriptor(self):
        return self._artop_nvBlockDescriptor
