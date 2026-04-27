# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestEnumeratorDef.py
from .ARObject import ARObject

class RestEnumeratorDef(ARObject):

    def __init__(self):
        super().__init__()
        from .RestStringPropertyDef import RestStringPropertyDef
        self._artop_value = None
        self._artop_restStringPropertyDef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_restStringPropertyDef": "REST-STRING-PROPERTY-DEF"})

    @property
    def value_(self):
        return self._artop_value

    @property
    def ref_restStringPropertyDef_(self):
        return self._artop_restStringPropertyDef

    @property
    def restStringPropertyDef_(self):
        if self._artop_restStringPropertyDef is not None:
            if hasattr(self._artop_restStringPropertyDef, "uuid"):
                return self._artop_restStringPropertyDef.uuid
        return
