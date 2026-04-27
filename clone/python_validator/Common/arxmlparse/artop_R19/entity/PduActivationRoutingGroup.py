# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PduActivationRoutingGroup.py
from .Referrable import Referrable

class PduActivationRoutingGroup(Referrable):

    def __init__(self):
        super().__init__()
        from .SoConIPduIdentifier import SoConIPduIdentifier
        from .VariationPoint import VariationPoint
        self._artop_eventGroupControlType = None
        self._artop_iPduIdentifierTcpRef = []
        self._artop_iPduIdentifierUdpRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_iPduIdentifierTcpRef':"SO-CON-I-PDU-IDENTIFIER", 
         '_artop_iPduIdentifierUdpRef':"SO-CON-I-PDU-IDENTIFIER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def eventGroupControlType_(self):
        return self._artop_eventGroupControlType

    @property
    def ref_iPduIdentifierTcps_(self):
        return self._artop_iPduIdentifierTcpRef

    @property
    def iPduIdentifierTcps_(self):
        return self._artop_iPduIdentifierTcpRef

    @property
    def ref_iPduIdentifierUdps_(self):
        return self._artop_iPduIdentifierUdpRef

    @property
    def iPduIdentifierUdps_(self):
        return self._artop_iPduIdentifierUdpRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
