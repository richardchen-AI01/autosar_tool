# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestPrimitivePropertyDef.py
from .RestAbstractPropertyDef import RestAbstractPropertyDef

class RestPrimitivePropertyDef(RestAbstractPropertyDef):

    def __init__(self):
        super().__init__()
        from .RestArrayPropertyDef import RestArrayPropertyDef
        self._artop_restArrayPropertyDef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_restArrayPropertyDef": "REST-ARRAY-PROPERTY-DEF"})

    @property
    def ref_restArrayPropertyDef_(self):
        return self._artop_restArrayPropertyDef

    @property
    def restArrayPropertyDef_(self):
        if self._artop_restArrayPropertyDef is not None:
            if hasattr(self._artop_restArrayPropertyDef, "uuid"):
                return self._artop_restArrayPropertyDef.uuid
        return
