# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetRawDataStreamGrant.py
from .RawDataStreamGrant import RawDataStreamGrant

class EthernetRawDataStreamGrant(RawDataStreamGrant):

    def __init__(self):
        super().__init__()
        from .EthernetRawDataStreamMapping import EthernetRawDataStreamMapping
        self._artop_ethernetRawDataStreamMappingRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ethernetRawDataStreamMappingRef": "ETHERNET-RAW-DATA-STREAM-MAPPING"})

    @property
    def ref_ethernetRawDataStreamMapping_(self):
        return self._artop_ethernetRawDataStreamMappingRef

    @property
    def ethernetRawDataStreamMapping_(self):
        if self._artop_ethernetRawDataStreamMappingRef is not None:
            if hasattr(self._artop_ethernetRawDataStreamMappingRef, "uuid"):
                return self._artop_ethernetRawDataStreamMappingRef.uuid
        return
