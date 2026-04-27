# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SpecElementScope.py
from .SpecElementReference import SpecElementReference

class SpecElementScope(SpecElementReference):

    def __init__(self):
        super().__init__()
        self._artop_inScope = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def inScope_(self):
        if self._artop_inScope:
            if self._artop_inScope == "true":
                return True
            return False
        else:
            return self._artop_inScope
