# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalToIPduMapping.py
from .Identifiable import Identifiable

class ISignalToIPduMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ISignalGroup import ISignalGroup
        from .ISignal import ISignal
        from .VariationPoint import VariationPoint
        self._artop_packingByteOrder = None
        self._artop_startPosition = None
        self._artop_transferProperty = None
        self._artop_updateIndicationBitPosition = None
        self._artop_iSignalGroupRef = None
        self._artop_iSignalRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iSignalGroupRef':"I-SIGNAL-GROUP", 
         '_artop_iSignalRef':"I-SIGNAL", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def packingByteOrder_(self):
        return self._artop_packingByteOrder

    @property
    def startPosition_(self):
        if self._artop_startPosition:
            return int(self._artop_startPosition)
        return self._artop_startPosition

    @property
    def transferProperty_(self):
        return self._artop_transferProperty

    @property
    def updateIndicationBitPosition_(self):
        if self._artop_updateIndicationBitPosition:
            return int(self._artop_updateIndicationBitPosition)
        return self._artop_updateIndicationBitPosition

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
