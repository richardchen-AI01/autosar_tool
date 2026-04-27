# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoConIPduIdentifierRefConditional.py
from .ARObject import ARObject

class SoConIPduIdentifierRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .StaticSocketConnection import StaticSocketConnection
        from .SoConIPduIdentifier import SoConIPduIdentifier
        from .VariationPoint import VariationPoint
        self._artop_staticSocketConnection = None
        self._artop_soConIPduIdentifierRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_staticSocketConnection':"STATIC-SOCKET-CONNECTION", 
         '_artop_soConIPduIdentifierRef':"SO-CON-I-PDU-IDENTIFIER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_staticSocketConnection_(self):
        return self._artop_staticSocketConnection

    @property
    def staticSocketConnection_(self):
        if self._artop_staticSocketConnection is not None:
            if hasattr(self._artop_staticSocketConnection, "uuid"):
                return self._artop_staticSocketConnection.uuid
        return

    @property
    def ref_soConIPduIdentifier_(self):
        return self._artop_soConIPduIdentifierRef

    @property
    def soConIPduIdentifier_(self):
        if self._artop_soConIPduIdentifierRef is not None:
            if hasattr(self._artop_soConIPduIdentifierRef, "uuid"):
                return self._artop_soConIPduIdentifierRef.uuid
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
