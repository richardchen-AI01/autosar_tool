# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortInterfaceToDataTypeMapping.py
from .UploadablePackageElement import UploadablePackageElement

class PortInterfaceToDataTypeMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .DataTypeMappingSet import DataTypeMappingSet
        from .PortInterface import PortInterface
        self._artop_dataTypeMappingSetRef = []
        self._artop_portInterfaceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTypeMappingSetRef':"DATA-TYPE-MAPPING-SET", 
         '_artop_portInterfaceRef':"PORT-INTERFACE"})

    @property
    def ref_dataTypeMappingSets_(self):
        return self._artop_dataTypeMappingSetRef

    @property
    def dataTypeMappingSets_(self):
        return self._artop_dataTypeMappingSetRef

    @property
    def ref_portInterface_(self):
        return self._artop_portInterfaceRef

    @property
    def portInterface_(self):
        if self._artop_portInterfaceRef is not None:
            if hasattr(self._artop_portInterfaceRef, "uuid"):
                return self._artop_portInterfaceRef.uuid
        return
