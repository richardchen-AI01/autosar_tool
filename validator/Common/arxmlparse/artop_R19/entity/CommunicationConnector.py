# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CommunicationConnector.py
from .Identifiable import Identifiable

class CommunicationConnector(Identifiable):

    def __init__(self):
        super().__init__()
        from .CommunicationController import CommunicationController
        from .CommConnectorPort import CommConnectorPort
        from .VariationPoint import VariationPoint
        self._artop_createEcuWakeupSource = None
        self._artop_pncGatewayType = None
        self._artop_commControllerRef = None
        self._artop_ecuCommPortInstance = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_commControllerRef':"COMMUNICATION-CONTROLLER", 
         '_artop_ecuCommPortInstance':"COMM-CONNECTOR-PORT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def createEcuWakeupSource_(self):
        if self._artop_createEcuWakeupSource:
            if self._artop_createEcuWakeupSource == "true":
                return True
            return False
        else:
            return self._artop_createEcuWakeupSource

    @property
    def pncGatewayType_(self):
        return self._artop_pncGatewayType

    @property
    def ref_commController_(self):
        return self._artop_commControllerRef

    @property
    def commController_(self):
        if self._artop_commControllerRef is not None:
            if hasattr(self._artop_commControllerRef, "uuid"):
                return self._artop_commControllerRef.uuid
        return

    @property
    def ecuCommPortInstances_CommConnectorPort(self):
        return self._artop_ecuCommPortInstance

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
