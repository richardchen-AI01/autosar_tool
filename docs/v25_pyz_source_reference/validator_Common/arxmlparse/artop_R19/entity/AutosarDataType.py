# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AutosarDataType.py
from .AtpType import AtpType
from .ARElement import ARElement

class AutosarDataType(ARElement, AtpType):

    def __init__(self):
        super().__init__()
        from .SwDataDefProps import SwDataDefProps
        self._artop_swDataDefProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swDataDefProps": "SW-DATA-DEF-PROPS"})

    @property
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
        return
