# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TriggerToSignalMapping.py
from .DataMapping import DataMapping

class TriggerToSignalMapping(DataMapping):

    def __init__(self):
        super().__init__()
        from .TriggerInSystemInstanceRef import TriggerInSystemInstanceRef
        from .SystemSignal import SystemSignal
        self._artop_triggerIref = None
        self._artop_systemSignalRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_triggerIref':"TRIGGER-IN-SYSTEM-INSTANCE-REF-IREF", 
         '_artop_systemSignalRef':"SYSTEM-SIGNAL"})

    @property
    def ref_trigger_(self):
        return self._artop_triggerIref

    @property
    def trigger_(self):
        if self._artop_triggerIref is not None:
            if hasattr(self._artop_triggerIref, "uuid"):
                return self._artop_triggerIref.uuid
        return

    @property
    def ref_systemSignal_(self):
        return self._artop_systemSignalRef

    @property
    def systemSignal_(self):
        if self._artop_systemSignalRef is not None:
            if hasattr(self._artop_systemSignalRef, "uuid"):
                return self._artop_systemSignalRef.uuid
        return
