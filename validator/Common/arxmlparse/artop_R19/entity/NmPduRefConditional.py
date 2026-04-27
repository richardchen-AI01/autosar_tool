# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmPduRefConditional.py
from .ARObject import ARObject

class NmPduRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ISignalIPduGroup import ISignalIPduGroup
        from .NmPdu import NmPdu
        from .VariationPoint import VariationPoint
        self._artop_iSignalIPduGroup = None
        self._artop_nmPduRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iSignalIPduGroup':"I-SIGNAL-I-PDU-GROUP", 
         '_artop_nmPduRef':"NM-PDU", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_iSignalIPduGroup_(self):
        return self._artop_iSignalIPduGroup

    @property
    def iSignalIPduGroup_(self):
        if self._artop_iSignalIPduGroup is not None:
            if hasattr(self._artop_iSignalIPduGroup, "uuid"):
                return self._artop_iSignalIPduGroup.uuid
        return

    @property
    def ref_nmPdu_(self):
        return self._artop_nmPduRef

    @property
    def nmPdu_(self):
        if self._artop_nmPduRef is not None:
            if hasattr(self._artop_nmPduRef, "uuid"):
                return self._artop_nmPduRef.uuid
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
