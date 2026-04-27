# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventBswModeDeclaration.py
from .TDEventBsw import TDEventBsw

class TDEventBswModeDeclaration(TDEventBsw):

    def __init__(self):
        super().__init__()
        from .ModeDeclaration import ModeDeclaration
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        self._artop_tdEventBswModeDeclarationType = None
        self._artop_entryModeDeclarationRef = None
        self._artop_exitModeDeclarationRef = None
        self._artop_modeDeclarationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_entryModeDeclarationRef':"MODE-DECLARATION", 
         '_artop_exitModeDeclarationRef':"MODE-DECLARATION", 
         '_artop_modeDeclarationRef':"MODE-DECLARATION-GROUP-PROTOTYPE"})

    @property
    def tdEventBswModeDeclarationType_(self):
        return self._artop_tdEventBswModeDeclarationType

    @property
    def ref_entryModeDeclaration_(self):
        return self._artop_entryModeDeclarationRef

    @property
    def entryModeDeclaration_(self):
        if self._artop_entryModeDeclarationRef is not None:
            if hasattr(self._artop_entryModeDeclarationRef, "uuid"):
                return self._artop_entryModeDeclarationRef.uuid
        return

    @property
    def ref_exitModeDeclaration_(self):
        return self._artop_exitModeDeclarationRef

    @property
    def exitModeDeclaration_(self):
        if self._artop_exitModeDeclarationRef is not None:
            if hasattr(self._artop_exitModeDeclarationRef, "uuid"):
                return self._artop_exitModeDeclarationRef.uuid
        return

    @property
    def ref_modeDeclaration_(self):
        return self._artop_modeDeclarationRef

    @property
    def modeDeclaration_(self):
        if self._artop_modeDeclarationRef is not None:
            if hasattr(self._artop_modeDeclarationRef, "uuid"):
                return self._artop_modeDeclarationRef.uuid
        return
