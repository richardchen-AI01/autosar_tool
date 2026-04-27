# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpInstantiation.py
from .NonOsModuleInstantiation import NonOsModuleInstantiation

class DoIpInstantiation(NonOsModuleInstantiation):

    def __init__(self):
        super().__init__()
        from .DoIpNetworkConfiguration import DoIpNetworkConfiguration
        from .DoIpRequestConfiguration import DoIpRequestConfiguration
        self._artop_eid = None
        self._artop_entityStatusMaxByteFieldUse = None
        self._artop_gid = None
        self._artop_gidInvalidityPattern = None
        self._artop_logicalAddress = None
        self._artop_maxRequestBytes = None
        self._artop_vinInvalidityPattern = None
        self._artop_networkInterface = []
        self._artop_requestConfiguration = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkInterface':"DO-IP-NETWORK-CONFIGURATION", 
         '_artop_requestConfiguration':"DO-IP-REQUEST-CONFIGURATION"})

    @property
    def eid_(self):
        return self._artop_eid

    @property
    def entityStatusMaxByteFieldUse_(self):
        if self._artop_entityStatusMaxByteFieldUse:
            if self._artop_entityStatusMaxByteFieldUse == "true":
                return True
            return False
        else:
            return self._artop_entityStatusMaxByteFieldUse

    @property
    def gid_(self):
        return self._artop_gid

    @property
    def gidInvalidityPattern_(self):
        return self._artop_gidInvalidityPattern

    @property
    def logicalAddress_(self):
        return self._artop_logicalAddress

    @property
    def maxRequestBytes_(self):
        return self._artop_maxRequestBytes

    @property
    def vinInvalidityPattern_(self):
        return self._artop_vinInvalidityPattern

    @property
    def networkInterfaces_DoIpNetworkConfiguration(self):
        return self._artop_networkInterface

    @property
    def requestConfigurations_DoIpRequestConfiguration(self):
        return self._artop_requestConfiguration
