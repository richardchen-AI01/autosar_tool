# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProcessDesign.py
from .ARElement import ARElement

class ProcessDesign(ARElement):

    def __init__(self):
        super().__init__()
        from .DeterministicClientResourceNeeds import DeterministicClientResourceNeeds
        from .Executable import Executable
        self._artop_deterministicClientResourceNeeds = []
        self._artop_executableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_deterministicClientResourceNeeds':"DETERMINISTIC-CLIENT-RESOURCE-NEEDS", 
         '_artop_executableRef':"EXECUTABLE"})

    @property
    def deterministicClientResourceNeeds_DeterministicClientResourceNeeds(self):
        return self._artop_deterministicClientResourceNeeds

    @property
    def ref_executable_(self):
        return self._artop_executableRef

    @property
    def executable_(self):
        if self._artop_executableRef is not None:
            if hasattr(self._artop_executableRef, "uuid"):
                return self._artop_executableRef.uuid
        return
