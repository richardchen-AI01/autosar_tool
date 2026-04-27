# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PrmCharNumericalValue.py
from .ARObject import ARObject

class PrmCharNumericalValue(ARObject):

    def __init__(self):
        super().__init__()
        from .PrmCharNumericalContents import PrmCharNumericalContents
        self._artop_prmCharNumericalContents = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_prmCharNumericalContents": "PRM-CHAR-NUMERICAL-CONTENTS"})

    @property
    def ref_prmCharNumericalContents_(self):
        return self._artop_prmCharNumericalContents

    @property
    def prmCharNumericalContents_(self):
        if self._artop_prmCharNumericalContents is not None:
            if hasattr(self._artop_prmCharNumericalContents, "uuid"):
                return self._artop_prmCharNumericalContents.uuid
        return
