# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipServiceDiscovery.py
from .ServiceDiscoveryConfiguration import ServiceDiscoveryConfiguration

class SomeipServiceDiscovery(ServiceDiscoveryConfiguration):

    def __init__(self):
        super().__init__()
        from .NetworkEndpoint import NetworkEndpoint
        from .SecureComProps import SecureComProps
        self._artop_someipServiceDiscoveryPort = None
        self._artop_multicastSdIpAddressRef = None
        self._artop_multicastSecureComPropsRef = None
        self._artop_unicastSecureComPropsRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_multicastSdIpAddressRef':"NETWORK-ENDPOINT", 
         '_artop_multicastSecureComPropsRef':"SECURE-COM-PROPS", 
         '_artop_unicastSecureComPropsRef':"SECURE-COM-PROPS"})

    @property
    def someipServiceDiscoveryPort_(self):
        return self._artop_someipServiceDiscoveryPort

    @property
    def ref_multicastSdIpAddress_(self):
        return self._artop_multicastSdIpAddressRef

    @property
    def multicastSdIpAddress_(self):
        if self._artop_multicastSdIpAddressRef is not None:
            if hasattr(self._artop_multicastSdIpAddressRef, "uuid"):
                return self._artop_multicastSdIpAddressRef.uuid
        return

    @property
    def ref_multicastSecureComProps_(self):
        return self._artop_multicastSecureComPropsRef

    @property
    def multicastSecureComProps_(self):
        if self._artop_multicastSecureComPropsRef is not None:
            if hasattr(self._artop_multicastSecureComPropsRef, "uuid"):
                return self._artop_multicastSecureComPropsRef.uuid
        return

    @property
    def ref_unicastSecureComProps_(self):
        return self._artop_unicastSecureComPropsRef

    @property
    def unicastSecureComProps_(self):
        return self._artop_unicastSecureComPropsRef
