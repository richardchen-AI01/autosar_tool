# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DeterministicClientResource.py
from .ARObject import ARObject

class DeterministicClientResource(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_numberOfInstructions = None
        self._artop_sequentialInstructionsBegin = None
        self._artop_sequentialInstructionsEnd = None
        self._artop_speedup = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def numberOfInstructions_(self):
        return self._artop_numberOfInstructions

    @property
    def sequentialInstructionsBegin_(self):
        return self._artop_sequentialInstructionsBegin

    @property
    def sequentialInstructionsEnd_(self):
        return self._artop_sequentialInstructionsEnd

    @property
    def speedup_(self):
        if self._artop_speedup:
            return float(self._artop_speedup)
        return self._artop_speedup
