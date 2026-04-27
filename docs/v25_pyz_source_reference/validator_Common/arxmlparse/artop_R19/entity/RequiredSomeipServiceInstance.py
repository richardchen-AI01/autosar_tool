# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RequiredSomeipServiceInstance.py
from .RequiredApServiceInstance import RequiredApServiceInstance

class RequiredSomeipServiceInstance(RequiredApServiceInstance):

    def __init__(self):
        super().__init__()
        from .SomeipServiceVersion import SomeipServiceVersion
        from .TagWithOptionalValue import TagWithOptionalValue
        from .SomeipMethodProps import SomeipMethodProps
        from .SomeipRequiredEventGroup import SomeipRequiredEventGroup
        from .SomeipSdClientServiceInstanceConfig import SomeipSdClientServiceInstanceConfig
        self._artop_requiredMinorVersion = None
        self._artop_requiredServiceInstanceId = None
        self._artop_versionDrivenFindBehavior = None
        self._artop_blacklistedVersion = []
        self._artop_capabilityRecord = []
        self._artop_methodRequestProps = []
        self._artop_requiredEventGroup = []
        self._artop_sdClientConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_blacklistedVersion': '"SOMEIP-SERVICE-VERSION"', 
         '_artop_capabilityRecord': '"TAG-WITH-OPTIONAL-VALUE"', 
         '_artop_methodRequestProps': '"SOMEIP-METHOD-PROPS"', 
         '_artop_requiredEventGroup': '"SOMEIP-REQUIRED-EVENT-GROUP"', 
         '_artop_sdClientConfigRef': '"SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG"'})

    @property
    def requiredMinorVersion_(self):
        return self._artop_requiredMinorVersion

    @property
    def requiredServiceInstanceId_(self):
        return self._artop_requiredServiceInstanceId

    @property
    def versionDrivenFindBehavior_(self):
        return self._artop_versionDrivenFindBehavior

    @property
    def blacklistedVersions_SomeipServiceVersion(self):
        return self._artop_blacklistedVersion

    @property
    def capabilityRecords_TagWithOptionalValue(self):
        return self._artop_capabilityRecord

    @property
    def methodRequestProps_SomeipMethodProps(self):
        return self._artop_methodRequestProps

    @property
    def requiredEventGroups_SomeipRequiredEventGroup(self):
        return self._artop_requiredEventGroup

    @property
    def ref_sdClientConfig_(self):
        return self._artop_sdClientConfigRef

    @property
    def sdClientConfig_(self):
        if self._artop_sdClientConfigRef is not None:
            if hasattr(self._artop_sdClientConfigRef, "uuid"):
                return self._artop_sdClientConfigRef.uuid
        return
