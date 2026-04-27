# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\End2EndEventProtectionProps.py
from .Identifiable import Identifiable

class End2EndEventProtectionProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        from .E2EProfileConfiguration import E2EProfileConfiguration
        from .ServiceEventDeployment import ServiceEventDeployment
        self._artop_dataId = None
        self._artop_dataLength = None
        self._artop_dataUpdatePeriod = None
        self._artop_maxDataLength = None
        self._artop_minDataLength = None
        self._artop_adaptivePlatformServiceInstance = None
        self._artop_e2EProfileConfigurationRef = None
        self._artop_eventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_adaptivePlatformServiceInstance':"ADAPTIVE-PLATFORM-SERVICE-INSTANCE", 
         '_artop_e2EProfileConfigurationRef':"E-2-E-PROFILE-CONFIGURATION", 
         '_artop_eventRef':"SERVICE-EVENT-DEPLOYMENT"})

    @property
    def dataId_(self):
        return self._artop_dataId

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def dataUpdatePeriod_(self):
        return self._artop_dataUpdatePeriod

    @property
    def maxDataLength_(self):
        return self._artop_maxDataLength

    @property
    def minDataLength_(self):
        return self._artop_minDataLength

    @property
    def ref_adaptivePlatformServiceInstance_(self):
        return self._artop_adaptivePlatformServiceInstance

    @property
    def adaptivePlatformServiceInstance_(self):
        if self._artop_adaptivePlatformServiceInstance is not None:
            if hasattr(self._artop_adaptivePlatformServiceInstance, "uuid"):
                return self._artop_adaptivePlatformServiceInstance.uuid
        return

    @property
    def ref_e2eProfileConfiguration_(self):
        return self._artop_e2EProfileConfigurationRef

    @property
    def e2eProfileConfiguration_(self):
        if self._artop_e2EProfileConfigurationRef is not None:
            if hasattr(self._artop_e2EProfileConfigurationRef, "uuid"):
                return self._artop_e2EProfileConfigurationRef.uuid
        return

    @property
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return
