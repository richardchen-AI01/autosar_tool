# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwCalprmAxisSet.py
from .ARObject import ARObject

class SwCalprmAxisSet(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsContent import SwDataDefPropsContent
        from .SwCalprmAxis import SwCalprmAxis
        self._artop_swDataDefPropsContent = None
        self._artop_swCalprmAxis = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swDataDefPropsContent':"SW-DATA-DEF-PROPS-CONTENT", 
         '_artop_swCalprmAxis':"SW-CALPRM-AXIS"})

    @property
    def ref_swDataDefPropsContent_(self):
        return self._artop_swDataDefPropsContent

    @property
    def swDataDefPropsContent_(self):
        if self._artop_swDataDefPropsContent is not None:
            if hasattr(self._artop_swDataDefPropsContent, "uuid"):
                return self._artop_swDataDefPropsContent.uuid
        return

    @property
    def swCalprmAxis_SwCalprmAxis(self):
        return self._artop_swCalprmAxis
