# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestObjectRef.py
from .RestPrimitivePropertyDef import RestPrimitivePropertyDef

class RestObjectRef(RestPrimitivePropertyDef):

    def __init__(self):
        super().__init__()
        from .RestElementDef import RestElementDef
        self._artop_role = None
        self._artop_objectRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_objectRef": "REST-ELEMENT-DEF"})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_objects_(self):
        return self._artop_objectRef

    @property
    def objects_(self):
        return self._artop_objectRef
