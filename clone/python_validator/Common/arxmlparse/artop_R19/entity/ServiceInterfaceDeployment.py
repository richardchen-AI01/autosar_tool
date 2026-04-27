# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceDeployment.py
from .UploadablePackageElement import UploadablePackageElement

class ServiceInterfaceDeployment(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .ServiceEventDeployment import ServiceEventDeployment
        from .ServiceFieldDeployment import ServiceFieldDeployment
        from .ServiceMethodDeployment import ServiceMethodDeployment
        from .ServiceInterface import ServiceInterface
        self._artop_eventDeployment = []
        self._artop_fieldDeployment = []
        self._artop_methodDeployment = []
        self._artop_serviceInterfaceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_eventDeployment': '"SERVICE-EVENT-DEPLOYMENT"', 
         '_artop_fieldDeployment': '"SERVICE-FIELD-DEPLOYMENT"', 
         '_artop_methodDeployment': '"SERVICE-METHOD-DEPLOYMENT"', 
         '_artop_serviceInterfaceRef': '"SERVICE-INTERFACE"'})

    @property
    def eventDeployments_ServiceEventDeployment(self):
        return self._artop_eventDeployment

    @property
    def fieldDeployments_ServiceFieldDeployment(self):
        return self._artop_fieldDeployment

    @property
    def methodDeployments_ServiceMethodDeployment(self):
        return self._artop_methodDeployment

    @property
    def ref_serviceInterface_(self):
        return self._artop_serviceInterfaceRef

    @property
    def serviceInterface_(self):
        if self._artop_serviceInterfaceRef is not None:
            if hasattr(self._artop_serviceInterfaceRef, "uuid"):
                return self._artop_serviceInterfaceRef.uuid
        return
