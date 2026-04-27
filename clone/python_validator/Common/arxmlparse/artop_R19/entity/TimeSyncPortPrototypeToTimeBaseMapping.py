# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeSyncPortPrototypeToTimeBaseMapping.py
from .UploadablePackageElement import UploadablePackageElement

class TimeSyncPortPrototypeToTimeBaseMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .Process import Process
        from .TimeBaseResource import TimeBaseResource
        from .RPortPrototypeInExecutableInstanceRef import RPortPrototypeInExecutableInstanceRef
        self._artop_processRef = None
        self._artop_timeBaseResourceRef = None
        self._artop_timeSyncPortPrototypeIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_processRef':"PROCESS", 
         '_artop_timeBaseResourceRef':"TIME-BASE-RESOURCE", 
         '_artop_timeSyncPortPrototypeIref':"R-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF"})

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
    def ref_timeBaseResource_(self):
        return self._artop_timeBaseResourceRef

    @property
    def timeBaseResource_(self):
        if self._artop_timeBaseResourceRef is not None:
            if hasattr(self._artop_timeBaseResourceRef, "uuid"):
                return self._artop_timeBaseResourceRef.uuid
        return

    @property
    def ref_timeSyncPortPrototype_(self):
        return self._artop_timeSyncPortPrototypeIref

    @property
    def timeSyncPortPrototype_(self):
        if self._artop_timeSyncPortPrototypeIref is not None:
            if hasattr(self._artop_timeSyncPortPrototypeIref, "uuid"):
                return self._artop_timeSyncPortPrototypeIref.uuid
        return
