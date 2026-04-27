# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RawDataStreamGrant.py
from .Grant import Grant

class RawDataStreamGrant(Grant):

    def __init__(self):
        super().__init__()
        from .RawDataStreamGrantDesign import RawDataStreamGrantDesign
        self._artop_designRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_designRef": "RAW-DATA-STREAM-GRANT-DESIGN"})

    @property
    def ref_design_(self):
        return self._artop_designRef

    @property
    def design_(self):
        if self._artop_designRef is not None:
            if hasattr(self._artop_designRef, "uuid"):
                return self._artop_designRef.uuid
        return
