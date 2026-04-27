# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalTriggering.py
from .Identifiable import Identifiable

class ISignalTriggering(Identifiable):

    def __init__(self):
        super().__init__()
        from .PhysicalChannel import PhysicalChannel
        from .ISignalGroup import ISignalGroup
        from .ISignalPort import ISignalPort
        from .ISignal import ISignal
        from .VariationPoint import VariationPoint
        self._artop_physicalChannel = None
        self._artop_iSignalGroupRef = None
        self._artop_iSignalPortRef = []
        self._artop_iSignalRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_physicalChannel': '"PHYSICAL-CHANNEL"', 
         '_artop_iSignalGroupRef': '"I-SIGNAL-GROUP"', 
         '_artop_iSignalPortRef': '"I-SIGNAL-PORT"', 
         '_artop_iSignalRef': '"I-SIGNAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_physicalChannel_(self):
        return self._artop_physicalChannel

    @property
    def physicalChannel_(self):
        if self._artop_physicalChannel is not None:
            if hasattr(self._artop_physicalChannel, "uuid"):
                return self._artop_physicalChannel.uuid
        return

    @property
    def ref_iSignalGroup_(self):
        return self._artop_iSignalGroupRef

    @property
    def iSignalGroup_(self):
        if self._artop_iSignalGroupRef is not None:
            if hasattr(self._artop_iSignalGroupRef, "uuid"):
                return self._artop_iSignalGroupRef.uuid
        return

    @property
    def ref_iSignalPorts_(self):
        return self._artop_iSignalPortRef

    @property
    def iSignalPorts_(self):
        return self._artop_iSignalPortRef

    @property
    def ref_iSignal_(self):
        return self._artop_iSignalRef

    @property
    def iSignal_(self):
        if self._artop_iSignalRef is not None:
            if hasattr(self._artop_iSignalRef, "uuid"):
                return self._artop_iSignalRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
