# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnvSwcModeElement.py
from .DiagnosticEnvModeElement import DiagnosticEnvModeElement

class DiagnosticEnvSwcModeElement(DiagnosticEnvModeElement):

    def __init__(self):
        super().__init__()
        from .PModeInSystemInstanceRef import PModeInSystemInstanceRef
        self._artop_modeIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeIref": "P-MODE-IN-SYSTEM-INSTANCE-REF-IREF"})

    @property
    def ref_mode_(self):
        return self._artop_modeIref

    @property
    def mode_(self):
        if self._artop_modeIref is not None:
            if hasattr(self._artop_modeIref, "uuid"):
                return self._artop_modeIref.uuid
        return
