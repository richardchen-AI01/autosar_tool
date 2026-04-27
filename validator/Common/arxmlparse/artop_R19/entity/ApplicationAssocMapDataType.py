# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationAssocMapDataType.py
from .ApplicationCompositeDataType import ApplicationCompositeDataType

class ApplicationAssocMapDataType(ApplicationCompositeDataType):

    def __init__(self):
        super().__init__()
        from .ApplicationAssocMapElement import ApplicationAssocMapElement
        self._artop_key = None
        self._artop_value = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_key':"APPLICATION-ASSOC-MAP-ELEMENT", 
         '_artop_value':"APPLICATION-ASSOC-MAP-ELEMENT"})

    @property
    def ref_key_(self):
        return self._artop_key

    @property
    def key_(self):
        if self._artop_key is not None:
            if hasattr(self._artop_key, "uuid"):
                return self._artop_key.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return
