# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwSystemconstantValueSet.py
from .ARElement import ARElement

class SwSystemconstantValueSet(ARElement):

    def __init__(self):
        super().__init__()
        from .SwSystemconstValue import SwSystemconstValue
        self._artop_swSystemconstantValue = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swSystemconstantValue": "SW-SYSTEMCONST-VALUE"})

    @property
    def swSystemconstantValues_SwSystemconstValue(self):
        return self._artop_swSystemconstantValue
