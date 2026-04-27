# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Map.py
from .ARObject import ARObject

class Map(ARObject):

    def __init__(self):
        super().__init__()
        from .LGraphic import LGraphic
        from .Area import Area
        self._artop_class_ = None
        self._artop_name = None
        self._artop_onclick = None
        self._artop_ondblclick = None
        self._artop_onkeydown = None
        self._artop_onkeypress = None
        self._artop_onkeyup = None
        self._artop_onmousedown = None
        self._artop_onmousemove = None
        self._artop_onmouseout = None
        self._artop_onmouseover = None
        self._artop_onmouseup = None
        self._artop_style = None
        self._artop_title = None
        self._artop_lGraphic = None
        self._artop_area = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_lGraphic':"L-GRAPHIC", 
         '_artop_area':"AREA"})

    @property
    def class__(self):
        return self._artop_class_

    @property
    def name_(self):
        return self._artop_name

    @property
    def onclick_(self):
        return self._artop_onclick

    @property
    def ondblclick_(self):
        return self._artop_ondblclick

    @property
    def onkeydown_(self):
        return self._artop_onkeydown

    @property
    def onkeypress_(self):
        return self._artop_onkeypress

    @property
    def onkeyup_(self):
        return self._artop_onkeyup

    @property
    def onmousedown_(self):
        return self._artop_onmousedown

    @property
    def onmousemove_(self):
        return self._artop_onmousemove

    @property
    def onmouseout_(self):
        return self._artop_onmouseout

    @property
    def onmouseover_(self):
        return self._artop_onmouseover

    @property
    def onmouseup_(self):
        return self._artop_onmouseup

    @property
    def style_(self):
        return self._artop_style

    @property
    def title_(self):
        return self._artop_title

    @property
    def ref_lGraphic_(self):
        return self._artop_lGraphic

    @property
    def lGraphic_(self):
        if self._artop_lGraphic is not None:
            if hasattr(self._artop_lGraphic, "uuid"):
                return self._artop_lGraphic.uuid
        return

    @property
    def areas_Area(self):
        return self._artop_area
