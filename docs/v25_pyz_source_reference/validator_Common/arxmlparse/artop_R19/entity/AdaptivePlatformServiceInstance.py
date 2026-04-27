# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AdaptivePlatformServiceInstance.py
from .UploadablePackageElement import UploadablePackageElement

class AdaptivePlatformServiceInstance(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .End2EndEventProtectionProps import End2EndEventProtectionProps
        from .End2EndMethodProtectionProps import End2EndMethodProtectionProps
        from .ServiceInterfaceElementSecureComConfig import ServiceInterfaceElementSecureComConfig
        from .ServiceInterfaceDeployment import ServiceInterfaceDeployment
        self._artop_e2EEventProtectionProps = []
        self._artop_e2EMethodProtectionProps = []
        self._artop_secureComConfig = []
        self._artop_serviceInterfaceDeploymentRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_e2EEventProtectionProps': '"END-2-END-EVENT-PROTECTION-PROPS"', 
         '_artop_e2EMethodProtectionProps': '"END-2-END-METHOD-PROTECTION-PROPS"', 
         '_artop_secureComConfig': '"SERVICE-INTERFACE-ELEMENT-SECURE-COM-CONFIG"', 
         '_artop_serviceInterfaceDeploymentRef': '"SERVICE-INTERFACE-DEPLOYMENT"'})

    @property
    def e2eEventProtectionProps_End2EndEventProtectionProps(self):
        return self._artop_e2EEventProtectionProps

    @property
    def e2eMethodProtectionProps_End2EndMethodProtectionProps(self):
        return self._artop_e2EMethodProtectionProps

    @property
    def secureComConfigs_ServiceInterfaceElementSecureComConfig(self):
        return self._artop_secureComConfig

    @property
    def ref_serviceInterfaceDeployment_(self):
        return self._artop_serviceInterfaceDeploymentRef

    @property
    def serviceInterfaceDeployment_(self):
        if self._artop_serviceInterfaceDeploymentRef is not None:
            if hasattr(self._artop_serviceInterfaceDeploymentRef, "uuid"):
                return self._artop_serviceInterfaceDeploymentRef.uuid
        return
