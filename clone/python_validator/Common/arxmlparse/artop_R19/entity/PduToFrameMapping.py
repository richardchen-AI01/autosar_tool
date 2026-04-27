# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PduToFrameMapping.py
from .Identifiable import Identifiable

class PduToFrameMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .Frame import Frame
        from .Pdu import Pdu
        from .VariationPoint import VariationPoint
        self._artop_packingByteOrder = None
        self._artop_startPosition = None
        self._artop_updateIndicationBitPosition = None
        self._artop_frame = None
        self._artop_pduRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_frame':"FRAME", 
         '_artop_pduRef':"PDU", 
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
    def updateIndicationBitPosition_(self):
        if self._artop_updateIndicationBitPosition:
            return int(self._artop_updateIndicationBitPosition)
        return self._artop_updateIndicationBitPosition

    @property
    def ref_frame_(self):
        return self._artop_frame

    @property
    def frame_(self):
        if self._artop_frame is not None:
            if hasattr(self._artop_frame, "uuid"):
                return self._artop_frame.uuid
        return

    @property
    def ref_pdu_(self):
        return self._artop_pduRef

    @property
    def pdu_(self):
        if self._artop_pduRef is not None:
            if hasattr(self._artop_pduRef, "uuid"):
                return self._artop_pduRef.uuid
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
