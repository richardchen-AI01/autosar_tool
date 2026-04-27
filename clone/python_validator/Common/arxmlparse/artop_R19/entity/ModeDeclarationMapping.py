# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeDeclarationMapping.py
from .AtpStructureElement import AtpStructureElement

class ModeDeclarationMapping(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationMappingSet import ModeDeclarationMappingSet
        from .ModeDeclaration import ModeDeclaration
        self._artop_modeDeclarationMappingSet = None
        self._artop_firstModeRef = []
        self._artop_secondModeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_modeDeclarationMappingSet':"MODE-DECLARATION-MAPPING-SET", 
         '_artop_firstModeRef':"MODE-DECLARATION", 
         '_artop_secondModeRef':"MODE-DECLARATION"})

    @property
    def ref_modeDeclarationMappingSet_(self):
        return self._artop_modeDeclarationMappingSet

    @property
    def modeDeclarationMappingSet_(self):
        if self._artop_modeDeclarationMappingSet is not None:
            if hasattr(self._artop_modeDeclarationMappingSet, "uuid"):
                return self._artop_modeDeclarationMappingSet.uuid
        return

    @property
    def ref_firstModes_(self):
        return self._artop_firstModeRef

    @property
    def firstModes_(self):
        return self._artop_firstModeRef

    @property
    def ref_secondMode_(self):
        return self._artop_secondModeRef

    @property
    def secondMode_(self):
        if self._artop_secondModeRef is not None:
            if hasattr(self._artop_secondModeRef, "uuid"):
                return self._artop_secondModeRef.uuid
        return
