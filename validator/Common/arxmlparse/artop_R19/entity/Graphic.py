# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Graphic.py
from .EngineeringObject import EngineeringObject

class Graphic(EngineeringObject):

    def __init__(self):
        super().__init__()
        from .LGraphic import LGraphic
        self._artop_editHeight = None
        self._artop_editWidth = None
        self._artop_editfit = None
        self._artop_editscale = None
        self._artop_filename = None
        self._artop_fit = None
        self._artop_generator = None
        self._artop_height = None
        self._artop_htmlFit = None
        self._artop_htmlHeight = None
        self._artop_htmlScale = None
        self._artop_htmlWidth = None
        self._artop_notation = None
        self._artop_scale = None
        self._artop_width = None
        self._artop_lGraphic = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_lGraphic": "L-GRAPHIC"})

    @property
    def editHeight_(self):
        return self._artop_editHeight

    @property
    def editWidth_(self):
        return self._artop_editWidth

    @property
    def editfit_(self):
        return self._artop_editfit

    @property
    def editscale_(self):
        return self._artop_editscale

    @property
    def filename_(self):
        return self._artop_filename

    @property
    def fit_(self):
        return self._artop_fit

    @property
    def generator_(self):
        return self._artop_generator

    @property
    def height_(self):
        return self._artop_height

    @property
    def htmlFit_(self):
        return self._artop_htmlFit

    @property
    def htmlHeight_(self):
        return self._artop_htmlHeight

    @property
    def htmlScale_(self):
        return self._artop_htmlScale

    @property
    def htmlWidth_(self):
        return self._artop_htmlWidth

    @property
    def notation_(self):
        return self._artop_notation

    @property
    def scale_(self):
        return self._artop_scale

    @property
    def width_(self):
        return self._artop_width

    @property
    def ref_lGraphic_(self):
        return self._artop_lGraphic

    @property
    def lGraphic_(self):
        if self._artop_lGraphic is not None:
            if hasattr(self._artop_lGraphic, "uuid"):
                return self._artop_lGraphic.uuid
        return
