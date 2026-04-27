# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwAxisGrouped.py
from .SwCalprmAxisTypeProps import SwCalprmAxisTypeProps

class SwAxisGrouped(SwCalprmAxisTypeProps):

    def __init__(self):
        super().__init__()
        from .ApplicationPrimitiveDataType import ApplicationPrimitiveDataType
        from .SwCalprmRefProxy import SwCalprmRefProxy
        self._artop_swAxisIndex = None
        self._artop_sharedAxisTypeRef = None
        self._artop_swCalprmRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sharedAxisTypeRef':"APPLICATION-PRIMITIVE-DATA-TYPE", 
         '_artop_swCalprmRef':"SW-CALPRM-REF-PROXY"})

    @property
    def swAxisIndex_(self):
        return self._artop_swAxisIndex

    @property
    def ref_sharedAxisType_(self):
        return self._artop_sharedAxisTypeRef

    @property
    def sharedAxisType_(self):
        if self._artop_sharedAxisTypeRef is not None:
            if hasattr(self._artop_sharedAxisTypeRef, "uuid"):
                return self._artop_sharedAxisTypeRef.uuid
        return

    @property
    def ref_swCalprmRef_(self):
        return self._artop_swCalprmRef

    @property
    def swCalprmRef_(self):
        if self._artop_swCalprmRef is not None:
            if hasattr(self._artop_swCalprmRef, "uuid"):
                return self._artop_swCalprmRef.uuid
        return
