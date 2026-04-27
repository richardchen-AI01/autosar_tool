# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CommunicationControllerMapping.py
from .ARObject import ARObject

class CommunicationControllerMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ECUMapping import ECUMapping
        from .CommunicationController import CommunicationController
        from .HwElement import HwElement
        self._artop_ecuMapping = None
        self._artop_communicationControllerRef = None
        self._artop_hwCommunicationControllerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecuMapping':"ECU-MAPPING", 
         '_artop_communicationControllerRef':"COMMUNICATION-CONTROLLER", 
         '_artop_hwCommunicationControllerRef':"HW-ELEMENT"})

    @property
    def ref_eCUMapping_(self):
        return self._artop_ecuMapping

    @property
    def eCUMapping_(self):
        if self._artop_ecuMapping is not None:
            if hasattr(self._artop_ecuMapping, "uuid"):
                return self._artop_ecuMapping.uuid
        return

    @property
    def ref_communicationController_(self):
        return self._artop_communicationControllerRef

    @property
    def communicationController_(self):
        if self._artop_communicationControllerRef is not None:
            if hasattr(self._artop_communicationControllerRef, "uuid"):
                return self._artop_communicationControllerRef.uuid
        return

    @property
    def ref_hwCommunicationController_(self):
        return self._artop_hwCommunicationControllerRef

    @property
    def hwCommunicationController_(self):
        if self._artop_hwCommunicationControllerRef is not None:
            if hasattr(self._artop_hwCommunicationControllerRef, "uuid"):
                return self._artop_hwCommunicationControllerRef.uuid
        return
