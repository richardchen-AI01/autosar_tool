# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RModeInAtomicSwcInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class RModeInAtomicSwcInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AtomicSwComponentType import AtomicSwComponentType
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeDeclaration import ModeDeclaration
        self._artop_atomicSwComponentType = None
        self._artop_contextPortRef = None
        self._artop_contextModeDeclarationGroupPrototypeRef = None
        self._artop_targetModeDeclarationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"', 
         '_artop_contextPortRef': '"ABSTRACT-REQUIRED-PORT-PROTOTYPE"', 
         '_artop_contextModeDeclarationGroupPrototypeRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_targetModeDeclarationRef': '"MODE-DECLARATION"'})

    @property
    def ref_base_(self):
        return self._artop_atomicSwComponentType

    @property
    def base_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return

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
