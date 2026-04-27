# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwPortMapping.py
from .ARObject import ARObject

class HwPortMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ECUMapping import ECUMapping
        from .CommunicationConnector import CommunicationConnector
        from .HwPinGroup import HwPinGroup
        self._artop_ecuMapping = None
        self._artop_communicationConnectorRef = None
        self._artop_hwCommunicationPortRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecuMapping':"ECU-MAPPING", 
         '_artop_communicationConnectorRef':"COMMUNICATION-CONNECTOR", 
         '_artop_hwCommunicationPortRef':"HW-PIN-GROUP"})

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
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
        return

    @property
    def ref_hwCommunicationPort_(self):
        return self._artop_hwCommunicationPortRef

    @property
    def hwCommunicationPort_(self):
        if self._artop_hwCommunicationPortRef is not None:
            if hasattr(self._artop_hwCommunicationPortRef, "uuid"):
                return self._artop_hwCommunicationPortRef.uuid
        return
