# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Area.py
from .ARObject import ARObject

class Area(ARObject):

    def __init__(self):
        super().__init__()
        from .Map import Map
        self._artop_accesskey = None
        self._artop_alt = None
        self._artop_class_ = None
        self._artop_coords = None
        self._artop_href = None
        self._artop_nohref = None
        self._artop_onblur = None
        self._artop_onclick = None
        self._artop_ondblclick = None
        self._artop_onfocus = None
        self._artop_onkeydown = None
        self._artop_onkeypress = None
        self._artop_onkeyup = None
        self._artop_onmousedown = None
        self._artop_onmousemove = None
        self._artop_onmouseout = None
        self._artop_onmouseover = None
        self._artop_onmouseup = None
        self._artop_shape = None
        self._artop_style = None
        self._artop_tabindex = None
        self._artop_title = None
        self._artop_map = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_map": "MAP"})

    @property
    def accesskey_(self):
        return self._artop_accesskey

    @property
    def alt_(self):
        return self._artop_alt

    @property
    def class__(self):
        return self._artop_class_

    @property
    def coords_(self):
        return self._artop_coords

    @property
    def href_(self):
        return self._artop_href

    @property
    def nohref_(self):
        return self._artop_nohref

    @property
    def onblur_(self):
        return self._artop_onblur

    @property
    def onclick_(self):
        return self._artop_onclick

    @property
    def ondblclick_(self):
        return self._artop_ondblclick

    @property
    def onfocus_(self):
        return self._artop_onfocus

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
    def shape_(self):
        return self._artop_shape

    @property
    def style_(self):
        return self._artop_style

    @property
    def tabindex_(self):
        return self._artop_tabindex

    @property
    def title_(self):
        return self._artop_title

    @property
    def ref_map_(self):
        return self._artop_map

    @property
    def map_(self):
        if self._artop_map is not None:
            if hasattr(self._artop_map, "uuid"):
                return self._artop_map.uuid
        return
