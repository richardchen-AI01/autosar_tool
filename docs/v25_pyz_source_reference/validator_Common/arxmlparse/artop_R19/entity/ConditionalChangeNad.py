# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConditionalChangeNad.py
from .LinConfigurationEntry import LinConfigurationEntry

class ConditionalChangeNad(LinConfigurationEntry):

    def __init__(self):
        super().__init__()
        self._artop_byte = None
        self._artop_id = None
        self._artop_invert = None
        self._artop_mask = None
        self._artop_newNad = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def byte_(self):
        if self._artop_byte:
            return int(self._artop_byte)
        return self._artop_byte

    @property
    def id_(self):
        return self._artop_id

    @property
    def invert_(self):
        if self._artop_invert:
            return int(self._artop_invert)
        return self._artop_invert

    @property
    def mask_(self):
        if self._artop_mask:
            return int(self._artop_mask)
        return self._artop_mask

    @property
    def newNad_(self):
        if self._artop_newNad:
            return int(self._artop_newNad)
        return self._artop_newNad
