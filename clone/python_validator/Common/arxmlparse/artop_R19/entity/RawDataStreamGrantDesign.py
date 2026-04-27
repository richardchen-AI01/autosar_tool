# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RawDataStreamGrantDesign.py
from .GrantDesign import GrantDesign

class RawDataStreamGrantDesign(GrantDesign):

    def __init__(self):
        super().__init__()
        from .RawDataStreamInterface import RawDataStreamInterface
        self._artop_rawDataStreamRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_rawDataStreamRef": "RAW-DATA-STREAM-INTERFACE"})

    @property
    def ref_rawDataStream_(self):
        return self._artop_rawDataStreamRef

    @property
    def rawDataStream_(self):
        if self._artop_rawDataStreamRef is not None:
            if hasattr(self._artop_rawDataStreamRef, "uuid"):
                return self._artop_rawDataStreamRef.uuid
        return
