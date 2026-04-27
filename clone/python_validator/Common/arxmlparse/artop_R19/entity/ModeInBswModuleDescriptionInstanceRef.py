# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeInBswModuleDescriptionInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ModeInBswModuleDescriptionInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .BswModuleDescription import BswModuleDescription
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeDeclaration import ModeDeclaration
        self._artop_bswModuleDescription = None
        self._artop_contextModeDeclarationGroupRef = None
        self._artop_targetModeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bswModuleDescription':"BSW-MODULE-DESCRIPTION", 
         '_artop_contextModeDeclarationGroupRef':"MODE-DECLARATION-GROUP-PROTOTYPE", 
         '_artop_targetModeRef':"MODE-DECLARATION"})

    @property
    def ref_base_(self):
        return self._artop_bswModuleDescription

    @property
    def base_(self):
        if self._artop_bswModuleDescription is not None:
            if hasattr(self._artop_bswModuleDescription, "uuid"):
                return self._artop_bswModuleDescription.uuid
        return

    @property
    def ref_contextModeDeclarationGroup_(self):
        return self._artop_contextModeDeclarationGroupRef

    @property
    def contextModeDeclarationGroup_(self):
        if self._artop_contextModeDeclarationGroupRef is not None:
            if hasattr(self._artop_contextModeDeclarationGroupRef, "uuid"):
                return self._artop_contextModeDeclarationGroupRef.uuid
        return

    @property
    def ref_targetMode_(self):
        return self._artop_targetModeRef

    @property
    def targetMode_(self):
        if self._artop_targetModeRef is not None:
            if hasattr(self._artop_targetModeRef, "uuid"):
                return self._artop_targetModeRef.uuid
        return
