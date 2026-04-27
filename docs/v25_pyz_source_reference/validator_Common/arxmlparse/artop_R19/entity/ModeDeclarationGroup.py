# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeDeclarationGroup.py
from .AtpType import AtpType
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class ModeDeclarationGroup(ARElement, AtpBlueprint, AtpBlueprintable, AtpType):

    def __init__(self):
        super().__init__()
        from .ModeDeclaration import ModeDeclaration
        from .ModeErrorBehavior import ModeErrorBehavior
        from .ModeTransition import ModeTransition
        self._artop_onTransitionValue = None
        self._artop_initialModeRef = None
        self._artop_modeDeclaration = []
        self._artop_modeManagerErrorBehavior = None
        self._artop_modeTransition = []
        self._artop_modeUserErrorBehavior = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_initialModeRef': '"MODE-DECLARATION"', 
         '_artop_modeDeclaration': '"MODE-DECLARATION"', 
         '_artop_modeManagerErrorBehavior': '"MODE-ERROR-BEHAVIOR"', 
         '_artop_modeTransition': '"MODE-TRANSITION"', 
         '_artop_modeUserErrorBehavior': '"MODE-ERROR-BEHAVIOR"'})

    @property
    def onTransitionValue_(self):
        return self._artop_onTransitionValue

    @property
    def ref_initialMode_(self):
        return self._artop_initialModeRef

    @property
    def initialMode_(self):
        if self._artop_initialModeRef is not None:
            if hasattr(self._artop_initialModeRef, "uuid"):
                return self._artop_initialModeRef.uuid
        return

    @property
    def modeDeclarations_ModeDeclaration(self):
        return self._artop_modeDeclaration

    @property
    def ref_modeManagerErrorBehavior_(self):
        return self._artop_modeManagerErrorBehavior

    @property
    def modeManagerErrorBehavior_(self):
        if self._artop_modeManagerErrorBehavior is not None:
            if hasattr(self._artop_modeManagerErrorBehavior, "uuid"):
                return self._artop_modeManagerErrorBehavior.uuid
        return

    @property
    def modeTransitions_ModeTransition(self):
        return self._artop_modeTransition

    @property
    def ref_modeUserErrorBehavior_(self):
        return self._artop_modeUserErrorBehavior

    @property
    def modeUserErrorBehavior_(self):
        if self._artop_modeUserErrorBehavior is not None:
            if hasattr(self._artop_modeUserErrorBehavior, "uuid"):
                return self._artop_modeUserErrorBehavior.uuid
        return
