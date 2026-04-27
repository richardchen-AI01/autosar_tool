# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HealthChannelExternalStatus.py
from .HealthChannel import HealthChannel

class HealthChannelExternalStatus(HealthChannel):

    def __init__(self):
        super().__init__()
        from .Process import Process
        from .PhmHealthChannelStatusInExecutableInstanceRef import PhmHealthChannelStatusInExecutableInstanceRef
        self._artop_modeCondition = None
        self._artop_processRef = None
        self._artop_statusIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_processRef':"PROCESS", 
         '_artop_statusIref':"PHM-HEALTH-CHANNEL-STATUS-IN-EXECUTABLE-INSTANCE-REF-IREF"})

    @property
    def modeCondition_(self):
        return self._artop_modeCondition

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
    def ref_status_(self):
        return self._artop_statusIref

    @property
    def status_(self):
        if self._artop_statusIref is not None:
            if hasattr(self._artop_statusIref, "uuid"):
                return self._artop_statusIref.uuid
        return
