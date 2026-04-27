# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmCoordinator.py
from .ARObject import ARObject

class NmCoordinator(ARObject):

    def __init__(self):
        super().__init__()
        from .NmEcu import NmEcu
        from .NmNode import NmNode
        self._artop_index = None
        self._artop_nmActiveCoordinator = None
        self._artop_nmCoordSyncSupport = None
        self._artop_nmGlobalCoordinatorTime = None
        self._artop_nmShutdownDelayTimer = None
        self._artop_nmEcu = None
        self._artop_nmNodeRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nmEcu':"NM-ECU", 
         '_artop_nmNodeRef':"NM-NODE"})

    @property
    def index_(self):
        if self._artop_index:
            return int(self._artop_index)
        return self._artop_index

    @property
    def nmActiveCoordinator_(self):
        if self._artop_nmActiveCoordinator:
            if self._artop_nmActiveCoordinator == "true":
                return True
            return False
        else:
            return self._artop_nmActiveCoordinator

    @property
    def nmCoordSyncSupport_(self):
        if self._artop_nmCoordSyncSupport:
            if self._artop_nmCoordSyncSupport == "true":
                return True
            return False
        else:
            return self._artop_nmCoordSyncSupport

    @property
    def nmGlobalCoordinatorTime_(self):
        return self._artop_nmGlobalCoordinatorTime

    @property
    def nmShutdownDelayTimer_(self):
        return self._artop_nmShutdownDelayTimer

    @property
    def ref_nmEcu_(self):
        return self._artop_nmEcu

    @property
    def nmEcu_(self):
        if self._artop_nmEcu is not None:
            if hasattr(self._artop_nmEcu, "uuid"):
                return self._artop_nmEcu.uuid
        return

    @property
    def ref_nmNodes_(self):
        return self._artop_nmNodeRef

    @property
    def nmNodes_(self):
        return self._artop_nmNodeRef
