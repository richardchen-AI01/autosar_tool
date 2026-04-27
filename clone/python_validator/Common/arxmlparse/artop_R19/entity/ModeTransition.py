# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeTransition.py
from .AtpStructureElement import AtpStructureElement

class ModeTransition(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroup import ModeDeclarationGroup
        from .ModeDeclaration import ModeDeclaration
        self._artop_modeDeclarationGroup = None
        self._artop_enteredModeRef = None
        self._artop_exitedModeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_modeDeclarationGroup':"MODE-DECLARATION-GROUP", 
         '_artop_enteredModeRef':"MODE-DECLARATION", 
         '_artop_exitedModeRef':"MODE-DECLARATION"})

    @property
    def ref_modeDeclarationGroup_(self):
        return self._artop_modeDeclarationGroup

    @property
    def modeDeclarationGroup_(self):
        if self._artop_modeDeclarationGroup is not None:
            if hasattr(self._artop_modeDeclarationGroup, "uuid"):
                return self._artop_modeDeclarationGroup.uuid
        return

    @property
    def ref_enteredMode_(self):
        return self._artop_enteredModeRef

    @property
    def enteredMode_(self):
        if self._artop_enteredModeRef is not None:
            if hasattr(self._artop_enteredModeRef, "uuid"):
                return self._artop_enteredModeRef.uuid
        return

    @property
    def ref_exitedMode_(self):
        return self._artop_exitedModeRef

    @property
    def exitedMode_(self):
        if self._artop_exitedModeRef is not None:
            if hasattr(self._artop_exitedModeRef, "uuid"):
                return self._artop_exitedModeRef.uuid
        return
