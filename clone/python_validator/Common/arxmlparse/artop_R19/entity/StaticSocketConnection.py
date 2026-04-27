# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\StaticSocketConnection.py
from .Identifiable import Identifiable

class StaticSocketConnection(Identifiable):

    def __init__(self):
        super().__init__()
        from .SocketAddress import SocketAddress
        from .SoConIPduIdentifierRefConditional import SoConIPduIdentifierRefConditional
        from .SocketAddressRefConditional import SocketAddressRefConditional
        from .VariationPoint import VariationPoint
        self._artop_tcpRole = None
        self._artop_socketAddress = None
        self._artop_iPduIdentifier = []
        self._artop_remoteAddress = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_socketAddress': '"SOCKET-ADDRESS"', 
         '_artop_iPduIdentifier': '"SO-CON-I-PDU-IDENTIFIER-REF-CONDITIONAL"', 
         '_artop_remoteAddress': '"SOCKET-ADDRESS-REF-CONDITIONAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def tcpRole_(self):
        return self._artop_tcpRole

    @property
    def ref_socketAddress_(self):
        return self._artop_socketAddress

    @property
    def socketAddress_(self):
        if self._artop_socketAddress is not None:
            if hasattr(self._artop_socketAddress, "uuid"):
                return self._artop_socketAddress.uuid
        return

    @property
    def iPduIdentifiers_SoConIPduIdentifierRefConditional(self):
        return self._artop_iPduIdentifier

    @property
    def remoteAddress_SocketAddressRefConditional(self):
        return self._artop_remoteAddress

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
