# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ECUMapping.py
from .Identifiable import Identifiable

class ECUMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .CommunicationControllerMapping import CommunicationControllerMapping
        from .EcuInstance import EcuInstance
        from .HwElement import HwElement
        from .HwPortMapping import HwPortMapping
        from .VariationPoint import VariationPoint
        self._artop_systemMapping = None
        self._artop_commControllerMapping = []
        self._artop_ecuInstanceRef = None
        self._artop_ecuRef = None
        self._artop_hwPortMapping = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_commControllerMapping': '"COMMUNICATION-CONTROLLER-MAPPING"', 
         '_artop_ecuInstanceRef': '"ECU-INSTANCE"', 
         '_artop_ecuRef': '"HW-ELEMENT"', 
         '_artop_hwPortMapping': '"HW-PORT-MAPPING"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def commControllerMappings_CommunicationControllerMapping(self):
        return self._artop_commControllerMapping

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
        return

    @property
    def ref_ecu_(self):
        return self._artop_ecuRef

    @property
    def ecu_(self):
        if self._artop_ecuRef is not None:
            if hasattr(self._artop_ecuRef, "uuid"):
                return self._artop_ecuRef.uuid
        return

    @property
    def hwPortMappings_HwPortMapping(self):
        return self._artop_hwPortMapping

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
