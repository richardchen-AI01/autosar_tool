# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyPortPrototypeToKeyValueDatabaseMapping.py
from .UploadablePackageElement import UploadablePackageElement

class PersistencyPortPrototypeToKeyValueDatabaseMapping(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .PersistencyKeyValueDatabase import PersistencyKeyValueDatabase
        from .PortPrototypeInExecutableInstanceRef import PortPrototypeInExecutableInstanceRef
        from .Process import Process
        self._artop_keyValueStorageRef = None
        self._artop_portPrototypeIref = None
        self._artop_processRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_keyValueStorageRef':"PERSISTENCY-KEY-VALUE-DATABASE", 
         '_artop_portPrototypeIref':"PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_processRef':"PROCESS"})

    @property
    def ref_keyValueStorage_(self):
        return self._artop_keyValueStorageRef

    @property
    def keyValueStorage_(self):
        if self._artop_keyValueStorageRef is not None:
            if hasattr(self._artop_keyValueStorageRef, "uuid"):
                return self._artop_keyValueStorageRef.uuid
        return

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototypeIref

    @property
    def portPrototype_(self):
        if self._artop_portPrototypeIref is not None:
            if hasattr(self._artop_portPrototypeIref, "uuid"):
                return self._artop_portPrototypeIref.uuid
        return

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return
