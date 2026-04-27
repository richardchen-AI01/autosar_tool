# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ValueGroup.py
from .ARObject import ARObject

class ValueGroup(ARObject):

    def __init__(self):
        super().__init__()
        from .SwValues import SwValues
        from .MultilanguageLongName import MultilanguageLongName
        self._artop_swValues = None
        self._artop_label = None
        self._artop_vgContents = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swValues':"SW-VALUES", 
         '_artop_label':"MULTILANGUAGE-LONG-NAME", 
         '_artop_vgContents':"SW-VALUES"})

    @property
    def ref_swValues_(self):
        return self._artop_swValues

    @property
    def swValues_(self):
        if self._artop_swValues is not None:
            if hasattr(self._artop_swValues, "uuid"):
                return self._artop_swValues.uuid
        return

    @property
    def ref_label_(self):
        return self._artop_label

    @property
    def label_(self):
        if self._artop_label is not None:
            if hasattr(self._artop_label, "uuid"):
                return self._artop_label.uuid
        return

    @property
    def ref_vgContents_(self):
        return self._artop_vgContents

    @property
    def vgContents_(self):
        if self._artop_vgContents is not None:
            if hasattr(self._artop_vgContents, "uuid"):
                return self._artop_vgContents.uuid
        return
