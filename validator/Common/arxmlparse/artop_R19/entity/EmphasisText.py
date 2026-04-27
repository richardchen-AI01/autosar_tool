# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EmphasisText.py
from .ARObject import ARObject

class EmphasisText(ARObject):

    def __init__(self):
        super().__init__()
        from .Tt import Tt
        self._artop_color = None
        self._artop_font = None
        self._artop_sub = None
        self._artop_sup = None
        self._artop_type = None
        self._artop_mixed = None
        self._artop_tt = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tt": "TT"})

    @property
    def color_(self):
        return self._artop_color

    @property
    def font_(self):
        return self._artop_font

    @property
    def sub_(self):
        return self._artop_sub

    @property
    def sup_(self):
        return self._artop_sup

    @property
    def type_(self):
        return self._artop_type

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def tts_Tt(self):
        return self._artop_tt
