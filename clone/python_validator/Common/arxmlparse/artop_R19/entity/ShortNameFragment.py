# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ShortNameFragment.py
from .ARObject import ARObject

class ShortNameFragment(ARObject):

    def __init__(self):
        super().__init__()
        from .Referrable import Referrable
        self._artop_role = None
        self._artop_fragment = None
        self._artop_referrable = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_referrable": "REFERRABLE"})

    @property
    def role_(self):
        return self._artop_role

    @property
    def fragment_(self):
        return self._artop_fragment

    @property
    def ref_referrable_(self):
        return self._artop_referrable

    @property
    def referrable_(self):
        if self._artop_referrable is not None:
            if hasattr(self._artop_referrable, "uuid"):
                return self._artop_referrable.uuid
        return
