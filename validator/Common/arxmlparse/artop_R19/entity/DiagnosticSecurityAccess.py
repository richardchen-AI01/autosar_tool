# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticSecurityAccess.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticSecurityAccess(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticSecurityAccessClass import DiagnosticSecurityAccessClass
        from .DiagnosticSecurityLevel import DiagnosticSecurityLevel
        self._artop_requestSeedId = None
        self._artop_securityAccessClassRef = None
        self._artop_securityLevelRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_securityAccessClassRef':"DIAGNOSTIC-SECURITY-ACCESS-CLASS", 
         '_artop_securityLevelRef':"DIAGNOSTIC-SECURITY-LEVEL"})

    @property
    def requestSeedId_(self):
        return self._artop_requestSeedId

    @property
    def ref_securityAccessClass_(self):
        return self._artop_securityAccessClassRef

    @property
    def securityAccessClass_(self):
        if self._artop_securityAccessClassRef is not None:
            if hasattr(self._artop_securityAccessClassRef, "uuid"):
                return self._artop_securityAccessClassRef.uuid
        return

    @property
    def ref_securityLevel_(self):
        return self._artop_securityLevelRef

    @property
    def securityLevel_(self):
        if self._artop_securityLevelRef is not None:
            if hasattr(self._artop_securityLevelRef, "uuid"):
                return self._artop_securityLevelRef.uuid
        return
