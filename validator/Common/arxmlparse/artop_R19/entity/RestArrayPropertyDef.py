# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestArrayPropertyDef.py
from .RestAbstractPropertyDef import RestAbstractPropertyDef

class RestArrayPropertyDef(RestAbstractPropertyDef):

    def __init__(self):
        super().__init__()
        from .RestPrimitivePropertyDef import RestPrimitivePropertyDef
        self._artop_element = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_element": "REST-PRIMITIVE-PROPERTY-DEF"})

    @property
    def ref_element_(self):
        return self._artop_element

    @property
    def element_(self):
        if self._artop_element is not None:
            if hasattr(self._artop_element, "uuid"):
                return self._artop_element.uuid
        return
