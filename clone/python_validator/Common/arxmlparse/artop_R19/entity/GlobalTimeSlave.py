# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeSlave.py
from .Identifiable import Identifiable

class GlobalTimeSlave(Identifiable):

    def __init__(self):
        super().__init__()
        from .GlobalTimeDomain import GlobalTimeDomain
        from .CommunicationConnector import CommunicationConnector
        from .VariationPoint import VariationPoint
        self._artop_followUpTimeoutValue = None
        self._artop_timeLeapFutureThreshold = None
        self._artop_timeLeapHealingCounter = None
        self._artop_timeLeapPastThreshold = None
        self._artop_globalTimeDomain = None
        self._artop_communicationConnectorRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_globalTimeDomain':"GLOBAL-TIME-DOMAIN", 
         '_artop_communicationConnectorRef':"COMMUNICATION-CONNECTOR", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def followUpTimeoutValue_(self):
        return self._artop_followUpTimeoutValue

    @property
    def timeLeapFutureThreshold_(self):
        return self._artop_timeLeapFutureThreshold

    @property
    def timeLeapHealingCounter_(self):
        return self._artop_timeLeapHealingCounter

    @property
    def timeLeapPastThreshold_(self):
        return self._artop_timeLeapPastThreshold

    @property
    def ref_globalTimeDomain_(self):
        return self._artop_globalTimeDomain

    @property
    def globalTimeDomain_(self):
        if self._artop_globalTimeDomain is not None:
            if hasattr(self._artop_globalTimeDomain, "uuid"):
                return self._artop_globalTimeDomain.uuid
        return

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
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
