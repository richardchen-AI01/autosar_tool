# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IncludedModeDeclarationGroupSet.py
from .ARObject import ARObject

class IncludedModeDeclarationGroupSet(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcInternalBehavior import SwcInternalBehavior
        from .ModeDeclarationGroup import ModeDeclarationGroup
        self._artop_prefix = None
        self._artop_swcInternalBehavior = None
        self._artop_modeDeclarationGroupRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swcInternalBehavior':"SWC-INTERNAL-BEHAVIOR", 
         '_artop_modeDeclarationGroupRef':"MODE-DECLARATION-GROUP"})

    @property
    def prefix_(self):
        return self._artop_prefix

    @property
    def ref_swcInternalBehavior_(self):
        return self._artop_swcInternalBehavior

    @property
    def swcInternalBehavior_(self):
        if self._artop_swcInternalBehavior is not None:
            if hasattr(self._artop_swcInternalBehavior, "uuid"):
                return self._artop_swcInternalBehavior.uuid
        return

    @property
    def ref_modeDeclarationGroups_(self):
        return self._artop_modeDeclarationGroupRef

    @property
    def modeDeclarationGroups_(self):
        return self._artop_modeDeclarationGroupRef
