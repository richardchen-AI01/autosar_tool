# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeMaster.py
from .Identifiable import Identifiable

class GlobalTimeMaster(Identifiable):

    def __init__(self):
        super().__init__()
        from .CommunicationConnector import CommunicationConnector
        from .VariationPoint import VariationPoint
        self._artop_immediateResumeTime = None
        self._artop_isSystemWideGlobalTimeMaster = None
        self._artop_syncPeriod = None
        self._artop_communicationConnectorRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_communicationConnectorRef':"COMMUNICATION-CONNECTOR", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def immediateResumeTime_(self):
        return self._artop_immediateResumeTime

    @property
    def isSystemWideGlobalTimeMaster_(self):
        if self._artop_isSystemWideGlobalTimeMaster:
            if self._artop_isSystemWideGlobalTimeMaster == "true":
                return True
            return False
        else:
            return self._artop_isSystemWideGlobalTimeMaster

    @property
    def syncPeriod_(self):
        return self._artop_syncPeriod

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
