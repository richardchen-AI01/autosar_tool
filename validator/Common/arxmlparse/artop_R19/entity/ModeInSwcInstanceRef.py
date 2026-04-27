# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeInSwcInstanceRef.py
from .ModeInSwcBswInstanceRef import ModeInSwcBswInstanceRef
from .AtpInstanceRef import AtpInstanceRef

class ModeInSwcInstanceRef(AtpInstanceRef, ModeInSwcBswInstanceRef):

    def __init__(self):
        super().__init__()
        from .SwComponentType import SwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        from .PortPrototype import PortPrototype
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeDeclaration import ModeDeclaration
        self._artop_swComponentType = None
        self._artop_contextComponentRef = []
        self._artop_contextPortRef = None
        self._artop_contextModeDeclarationGroupPrototypeRef = None
        self._artop_targetModeDeclarationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swComponentType': '"SW-COMPONENT-TYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPortRef': '"PORT-PROTOTYPE"', 
         '_artop_contextModeDeclarationGroupPrototypeRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_targetModeDeclarationRef': '"MODE-DECLARATION"'})

    @property
    def ref_base_(self):
        return self._artop_swComponentType

    @property
    def base_(self):
        if self._artop_swComponentType is not None:
            if hasattr(self._artop_swComponentType, "uuid"):
                return self._artop_swComponentType.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def ref_contextPort_(self):
        return self._artop_contextPortRef

    @property
    def contextPort_(self):
        if self._artop_contextPortRef is not None:
            if hasattr(self._artop_contextPortRef, "uuid"):
                return self._artop_contextPortRef.uuid
        return

    @property
    def ref_contextModeDeclarationGroupPrototype_(self):
        return self._artop_contextModeDeclarationGroupPrototypeRef

    @property
    def contextModeDeclarationGroupPrototype_(self):
        if self._artop_contextModeDeclarationGroupPrototypeRef is not None:
            if hasattr(self._artop_contextModeDeclarationGroupPrototypeRef, "uuid"):
                return self._artop_contextModeDeclarationGroupPrototypeRef.uuid
        return

    @property
    def ref_targetModeDeclaration_(self):
        return self._artop_targetModeDeclarationRef

    @property
    def targetModeDeclaration_(self):
        if self._artop_targetModeDeclarationRef is not None:
            if hasattr(self._artop_targetModeDeclarationRef, "uuid"):
                return self._artop_targetModeDeclarationRef.uuid
        return
