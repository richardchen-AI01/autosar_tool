# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SenderComSpec.py
from .PPortComSpec import PPortComSpec

class SenderComSpec(PPortComSpec):

    def __init__(self):
        super().__init__()
        from .CompositeNetworkRepresentation import CompositeNetworkRepresentation
        from .AutosarDataPrototype import AutosarDataPrototype
        from .SwDataDefProps import SwDataDefProps
        from .TransmissionAcknowledgementRequest import TransmissionAcknowledgementRequest
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        self._artop_dataUpdatePeriod = None
        self._artop_handleOutOfRange = None
        self._artop_senderCapability = None
        self._artop_compositeNetworkRepresentation = []
        self._artop_dataElementRef = None
        self._artop_networkRepresentation = None
        self._artop_transmissionAcknowledge = None
        self._artop_usesEndToEndProtection = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_compositeNetworkRepresentation': '"COMPOSITE-NETWORK-REPRESENTATION"', 
         '_artop_dataElementRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_networkRepresentation': '"SW-DATA-DEF-PROPS"', 
         '_artop_transmissionAcknowledge': '"TRANSMISSION-ACKNOWLEDGEMENT-REQUEST"', 
         '_artop_usesEndToEndProtection': '"BOOLEAN-VALUE-VARIATION-POINT"'})

    @property
    def dataUpdatePeriod_(self):
        return self._artop_dataUpdatePeriod

    @property
    def handleOutOfRange_(self):
        return self._artop_handleOutOfRange

    @property
    def senderCapability_(self):
        return self._artop_senderCapability

    @property
    def compositeNetworkRepresentations_CompositeNetworkRepresentation(self):
        return self._artop_compositeNetworkRepresentation

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return

    @property
    def ref_networkRepresentation_(self):
        return self._artop_networkRepresentation

    @property
    def networkRepresentation_(self):
        if self._artop_networkRepresentation is not None:
            if hasattr(self._artop_networkRepresentation, "uuid"):
                return self._artop_networkRepresentation.uuid
        return

    @property
    def ref_transmissionAcknowledge_(self):
        return self._artop_transmissionAcknowledge

    @property
    def transmissionAcknowledge_(self):
        if self._artop_transmissionAcknowledge is not None:
            if hasattr(self._artop_transmissionAcknowledge, "uuid"):
                return self._artop_transmissionAcknowledge.uuid
        return

    @property
    def ref_usesEndToEndProtection_(self):
        return self._artop_usesEndToEndProtection

    @property
    def usesEndToEndProtection_(self):
        if self._artop_usesEndToEndProtection is not None:
            if hasattr(self._artop_usesEndToEndProtection, "uuid"):
                return self._artop_usesEndToEndProtection.uuid
        return
