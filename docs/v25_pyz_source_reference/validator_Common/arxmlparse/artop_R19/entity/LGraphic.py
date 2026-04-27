# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LGraphic.py
from .LanguageSpecific import LanguageSpecific

class LGraphic(LanguageSpecific):

    def __init__(self):
        super().__init__()
        from .Graphic import Graphic
        from .Map import Map
        self._artop_graphic = None
        self._artop_map = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_graphic':"GRAPHIC", 
         '_artop_map':"MAP"})

    @property
    def ref_graphic_(self):
        return self._artop_graphic

    @property
    def graphic_(self):
        if self._artop_graphic is not None:
            if hasattr(self._artop_graphic, "uuid"):
                return self._artop_graphic.uuid
        return

    @property
    def ref_map_(self):
        return self._artop_map

    @property
    def map_(self):
        if self._artop_map is not None:
            if hasattr(self._artop_map, "uuid"):
                return self._artop_map.uuid
        return
