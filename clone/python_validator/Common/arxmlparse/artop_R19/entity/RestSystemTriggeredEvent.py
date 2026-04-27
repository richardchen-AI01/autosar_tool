# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestSystemTriggeredEvent.py
from .ARObject import ARObject

class RestSystemTriggeredEvent(ARObject):

    def __init__(self):
        super().__init__()
        from .RestResourceDef import RestResourceDef
        from .RestElementDef import RestElementDef
        self._artop_restResourceDef = None
        self._artop_elementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_restResourceDef':"REST-RESOURCE-DEF", 
         '_artop_elementRef':"REST-ELEMENT-DEF"})

    @property
    def ref_restResourceDef_(self):
        return self._artop_restResourceDef

    @property
    def restResourceDef_(self):
        if self._artop_restResourceDef is not None:
            if hasattr(self._artop_restResourceDef, "uuid"):
                return self._artop_restResourceDef.uuid
        return

    @property
    def ref_element_(self):
        return self._artop_elementRef

    @property
    def element_(self):
        if self._artop_elementRef is not None:
            if hasattr(self._artop_elementRef, "uuid"):
                return self._artop_elementRef.uuid
        return
