# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceElementSecureComConfig.py
from .Identifiable import Identifiable

class ServiceInterfaceElementSecureComConfig(Identifiable):

    def __init__(self):
        super().__init__()
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        from .ServiceEventDeployment import ServiceEventDeployment
        from .ServiceFieldDeployment import ServiceFieldDeployment
        from .ServiceMethodDeployment import ServiceMethodDeployment
        self._artop_dataId = None
        self._artop_freshnessValueId = None
        self._artop_adaptivePlatformServiceInstance = None
        self._artop_eventRef = None
        self._artop_fieldNotifierRef = None
        self._artop_getterCallRef = None
        self._artop_getterReturnRef = None
        self._artop_methodCallRef = None
        self._artop_methodReturnRef = None
        self._artop_setterCallRef = None
        self._artop_setterReturnRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_adaptivePlatformServiceInstance': '"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"', 
         '_artop_eventRef': '"SERVICE-EVENT-DEPLOYMENT"', 
         '_artop_fieldNotifierRef': '"SERVICE-FIELD-DEPLOYMENT"', 
         '_artop_getterCallRef': '"SERVICE-FIELD-DEPLOYMENT"', 
         '_artop_getterReturnRef': '"SERVICE-FIELD-DEPLOYMENT"', 
         '_artop_methodCallRef': '"SERVICE-METHOD-DEPLOYMENT"', 
         '_artop_methodReturnRef': '"SERVICE-METHOD-DEPLOYMENT"', 
         '_artop_setterCallRef': '"SERVICE-FIELD-DEPLOYMENT"', 
         '_artop_setterReturnRef': '"SERVICE-FIELD-DEPLOYMENT"'})

    @property
    def dataId_(self):
        return self._artop_dataId

    @property
    def freshnessValueId_(self):
        return self._artop_freshnessValueId

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
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return

    @property
    def ref_fieldNotifier_(self):
        return self._artop_fieldNotifierRef

    @property
    def fieldNotifier_(self):
        if self._artop_fieldNotifierRef is not None:
            if hasattr(self._artop_fieldNotifierRef, "uuid"):
                return self._artop_fieldNotifierRef.uuid
        return

    @property
    def ref_getterCall_(self):
        return self._artop_getterCallRef

    @property
    def getterCall_(self):
        if self._artop_getterCallRef is not None:
            if hasattr(self._artop_getterCallRef, "uuid"):
                return self._artop_getterCallRef.uuid
        return

    @property
    def ref_getterReturn_(self):
        return self._artop_getterReturnRef

    @property
    def getterReturn_(self):
        if self._artop_getterReturnRef is not None:
            if hasattr(self._artop_getterReturnRef, "uuid"):
                return self._artop_getterReturnRef.uuid
        return

    @property
    def ref_methodCall_(self):
        return self._artop_methodCallRef

    @property
    def methodCall_(self):
        if self._artop_methodCallRef is not None:
            if hasattr(self._artop_methodCallRef, "uuid"):
                return self._artop_methodCallRef.uuid
        return

    @property
    def ref_methodReturn_(self):
        return self._artop_methodReturnRef

    @property
    def methodReturn_(self):
        if self._artop_methodReturnRef is not None:
            if hasattr(self._artop_methodReturnRef, "uuid"):
                return self._artop_methodReturnRef.uuid
        return

    @property
    def ref_setterCall_(self):
        return self._artop_setterCallRef

    @property
    def setterCall_(self):
        if self._artop_setterCallRef is not None:
            if hasattr(self._artop_setterCallRef, "uuid"):
                return self._artop_setterCallRef.uuid
        return

    @property
    def ref_setterReturn_(self):
        return self._artop_setterReturnRef

    @property
    def setterReturn_(self):
        if self._artop_setterReturnRef is not None:
            if hasattr(self._artop_setterReturnRef, "uuid"):
                return self._artop_setterReturnRef.uuid
        return
