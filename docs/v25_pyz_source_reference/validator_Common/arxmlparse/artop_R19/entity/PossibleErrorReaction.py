# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PossibleErrorReaction.py
from .Identifiable import Identifiable

class PossibleErrorReaction(Identifiable):

    def __init__(self):
        super().__init__()
        from .TransientFault import TransientFault
        self._artop_reactionCode = None
        self._artop_transientFault = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_transientFault": "TRANSIENT-FAULT"})

    @property
    def reactionCode_(self):
        return self._artop_reactionCode

    @property
    def ref_transientFault_(self):
        return self._artop_transientFault

    @property
    def transientFault_(self):
        if self._artop_transientFault is not None:
            if hasattr(self._artop_transientFault, "uuid"):
                return self._artop_transientFault.uuid
        return
