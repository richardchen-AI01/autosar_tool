# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SystemSignal.py
from .ARElement import ARElement

class SystemSignal(ARElement):

    def __init__(self):
        super().__init__()
        from .SwDataDefProps import SwDataDefProps
        self._artop_dynamicLength = None
        self._artop_physicalProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_physicalProps": "SW-DATA-DEF-PROPS"})

    @property
    def dynamicLength_(self):
        if self._artop_dynamicLength:
            if self._artop_dynamicLength == "true":
                return True
            return False
        else:
            return self._artop_dynamicLength

    @property
    def ref_physicalProps_(self):
        return self._artop_physicalProps

    @property
    def physicalProps_(self):
        if self._artop_physicalProps is not None:
            if hasattr(self._artop_physicalProps, "uuid"):
                return self._artop_physicalProps.uuid
        return
