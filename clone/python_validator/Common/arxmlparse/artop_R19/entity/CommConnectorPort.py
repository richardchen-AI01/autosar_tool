# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CommConnectorPort.py
from .Identifiable import Identifiable

class CommConnectorPort(Identifiable):

    def __init__(self):
        super().__init__()
        from .CommunicationConnector import CommunicationConnector
        from .VariationPoint import VariationPoint
        self._artop_communicationDirection = None
        self._artop_communicationConnector = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_communicationConnector':"COMMUNICATION-CONNECTOR", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def communicationDirection_(self):
        return self._artop_communicationDirection

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnector

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnector is not None:
            if hasattr(self._artop_communicationConnector, "uuid"):
                return self._artop_communicationConnector.uuid
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
