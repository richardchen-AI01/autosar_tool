# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RecoveryViaApplicationActionToClientServerOperationMapping.py
from .UploadablePackageElement import UploadablePackageElement

class RecoveryViaApplicationActionToClientServerOperationMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .Process import Process
        from .ProvidedMethodInExecutableInstanceRef import ProvidedMethodInExecutableInstanceRef
        from .RecoveryViaApplicationAction import RecoveryViaApplicationAction
        self._artop_processRef = None
        self._artop_recoveryActionIref = None
        self._artop_recoveryViaApplicationActionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_processRef':"PROCESS", 
         '_artop_recoveryActionIref':"PROVIDED-METHOD-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_recoveryViaApplicationActionRef':"RECOVERY-VIA-APPLICATION-ACTION"})

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return

    @property
    def ref_recoveryAction_(self):
        return self._artop_recoveryActionIref

    @property
    def recoveryAction_(self):
        if self._artop_recoveryActionIref is not None:
            if hasattr(self._artop_recoveryActionIref, "uuid"):
                return self._artop_recoveryActionIref.uuid
        return

    @property
    def ref_recoveryViaApplicationAction_(self):
        return self._artop_recoveryViaApplicationActionRef

    @property
    def recoveryViaApplicationAction_(self):
        if self._artop_recoveryViaApplicationActionRef is not None:
            if hasattr(self._artop_recoveryViaApplicationActionRef, "uuid"):
                return self._artop_recoveryViaApplicationActionRef.uuid
        return
