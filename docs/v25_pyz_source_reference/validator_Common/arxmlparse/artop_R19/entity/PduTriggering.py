# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PduTriggering.py
from .Identifiable import Identifiable

class PduTriggering(Identifiable):

    def __init__(self):
        super().__init__()
        from .PhysicalChannel import PhysicalChannel
        from .IPduPort import IPduPort
        from .Pdu import Pdu
        from .ISignalTriggeringRefConditional import ISignalTriggeringRefConditional
        from .SecOcCryptoServiceMapping import SecOcCryptoServiceMapping
        from .TriggerIPduSendCondition import TriggerIPduSendCondition
        from .VariationPoint import VariationPoint
        self._artop_physicalChannel = None
        self._artop_iPduPortRef = []
        self._artop_iPduRef = None
        self._artop_iSignalTriggering = []
        self._artop_secOcCryptoMappingRef = None
        self._artop_triggerIPduSendCondition = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_physicalChannel': '"PHYSICAL-CHANNEL"', 
         '_artop_iPduPortRef': '"I-PDU-PORT"', 
         '_artop_iPduRef': '"PDU"', 
         '_artop_iSignalTriggering': '"I-SIGNAL-TRIGGERING-REF-CONDITIONAL"', 
         '_artop_secOcCryptoMappingRef': '"SEC-OC-CRYPTO-SERVICE-MAPPING"', 
         '_artop_triggerIPduSendCondition': '"TRIGGER-I-PDU-SEND-CONDITION"', 
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
    def ref_iPduPorts_(self):
        return self._artop_iPduPortRef

    @property
    def iPduPorts_(self):
        return self._artop_iPduPortRef

    @property
    def ref_iPdu_(self):
        return self._artop_iPduRef

    @property
    def iPdu_(self):
        if self._artop_iPduRef is not None:
            if hasattr(self._artop_iPduRef, "uuid"):
                return self._artop_iPduRef.uuid
        return

    @property
    def iSignalTriggerings_ISignalTriggeringRefConditional(self):
        return self._artop_iSignalTriggering

    @property
    def ref_secOcCryptoMapping_(self):
        return self._artop_secOcCryptoMappingRef

    @property
    def secOcCryptoMapping_(self):
        if self._artop_secOcCryptoMappingRef is not None:
            if hasattr(self._artop_secOcCryptoMappingRef, "uuid"):
                return self._artop_secOcCryptoMappingRef.uuid
        return

    @property
    def triggerIPduSendConditions_TriggerIPduSendCondition(self):
        return self._artop_triggerIPduSendCondition

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
