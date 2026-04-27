# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPduTiming.py
from .Describable import Describable

class IPduTiming(Describable):

    def __init__(self):
        super().__init__()
        from .ISignalIPdu import ISignalIPdu
        from .TransmissionModeDeclaration import TransmissionModeDeclaration
        from .VariationPoint import VariationPoint
        self._artop_minimumDelay = None
        self._artop_iSignalIPdu = None
        self._artop_transmissionModeDeclaration = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iSignalIPdu':"I-SIGNAL-I-PDU", 
         '_artop_transmissionModeDeclaration':"TRANSMISSION-MODE-DECLARATION", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def minimumDelay_(self):
        return self._artop_minimumDelay

    @property
    def ref_iSignalIPdu_(self):
        return self._artop_iSignalIPdu

    @property
    def iSignalIPdu_(self):
        if self._artop_iSignalIPdu is not None:
            if hasattr(self._artop_iSignalIPdu, "uuid"):
                return self._artop_iSignalIPdu.uuid
        return

    @property
    def ref_transmissionModeDeclaration_(self):
        return self._artop_transmissionModeDeclaration

    @property
    def transmissionModeDeclaration_(self):
        if self._artop_transmissionModeDeclaration is not None:
            if hasattr(self._artop_transmissionModeDeclaration, "uuid"):
                return self._artop_transmissionModeDeclaration.uuid
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
