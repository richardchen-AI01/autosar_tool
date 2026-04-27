# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwAddrMethod.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class SwAddrMethod(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        self._artop_memoryAllocationKeywordPolicy = None
        self._artop_option = None
        self._artop_sectionInitializationPolicy = None
        self._artop_sectionType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def memoryAllocationKeywordPolicy_(self):
        return self._artop_memoryAllocationKeywordPolicy

    @property
    def option_(self):
        return self._artop_option

    @property
    def sectionInitializationPolicy_(self):
        return self._artop_sectionInitializationPolicy

    @property
    def sectionType_(self):
        return self._artop_sectionType
