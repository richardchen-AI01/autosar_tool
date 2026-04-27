# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeErrorBehavior.py
from .ARObject import ARObject

class ModeErrorBehavior(ARObject):

    def __init__(self):
        super().__init__()
        from .ModeDeclaration import ModeDeclaration
        self._artop_errorReactionPolicy = None
        self._artop_defaultModeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_defaultModeRef": "MODE-DECLARATION"})

    @property
    def errorReactionPolicy_(self):
        return self._artop_errorReactionPolicy

    @property
    def ref_defaultMode_(self):
        return self._artop_defaultModeRef

    @property
    def defaultMode_(self):
        if self._artop_defaultModeRef is not None:
            if hasattr(self._artop_defaultModeRef, "uuid"):
                return self._artop_defaultModeRef.uuid
        return
