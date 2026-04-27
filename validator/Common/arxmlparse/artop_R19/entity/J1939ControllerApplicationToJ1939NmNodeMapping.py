# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939ControllerApplicationToJ1939NmNodeMapping.py
from .ARObject import ARObject

class J1939ControllerApplicationToJ1939NmNodeMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .J1939ControllerApplication import J1939ControllerApplication
        from .J1939NmNode import J1939NmNode
        self._artop_systemMapping = None
        self._artop_j1939ControllerApplicationRef = None
        self._artop_j1939NmNodeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_systemMapping':"SYSTEM-MAPPING", 
         '_artop_j1939ControllerApplicationRef':"J-1939-CONTROLLER-APPLICATION", 
         '_artop_j1939NmNodeRef':"J-1939-NM-NODE"})

    @property
    def ref_systemMapping_(self):
        return self._artop_systemMapping

    @property
    def systemMapping_(self):
        if self._artop_systemMapping is not None:
            if hasattr(self._artop_systemMapping, "uuid"):
                return self._artop_systemMapping.uuid
        return

    @property
    def ref_j1939ControllerApplication_(self):
        return self._artop_j1939ControllerApplicationRef

    @property
    def j1939ControllerApplication_(self):
        if self._artop_j1939ControllerApplicationRef is not None:
            if hasattr(self._artop_j1939ControllerApplicationRef, "uuid"):
                return self._artop_j1939ControllerApplicationRef.uuid
        return

    @property
    def ref_j1939NmNode_(self):
        return self._artop_j1939NmNodeRef

    @property
    def j1939NmNode_(self):
        if self._artop_j1939NmNodeRef is not None:
            if hasattr(self._artop_j1939NmNodeRef, "uuid"):
                return self._artop_j1939NmNodeRef.uuid
        return
