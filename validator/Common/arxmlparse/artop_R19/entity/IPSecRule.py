# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPSecRule.py
from .Identifiable import Identifiable

class IPSecRule(Identifiable):

    def __init__(self):
        super().__init__()
        from .IPSecConfig import IPSecConfig
        from .NetworkEndpoint import NetworkEndpoint
        self._artop_direction = None
        self._artop_headerType = None
        self._artop_ikeAuthenticationMethod = None
        self._artop_ipProtocol = None
        self._artop_localPortRangeEnd = None
        self._artop_localPortRangeStart = None
        self._artop_mode = None
        self._artop_policy = None
        self._artop_priority = None
        self._artop_remotePortRangeEnd = None
        self._artop_remotePortRangeStart = None
        self._artop_ipSecConfig = None
        self._artop_remoteIpAddressRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ipSecConfig':"IP-SEC-CONFIG", 
         '_artop_remoteIpAddressRef':"NETWORK-ENDPOINT"})

    @property
    def direction_(self):
        return self._artop_direction

    @property
    def headerType_(self):
        return self._artop_headerType

    @property
    def ikeAuthenticationMethod_(self):
        return self._artop_ikeAuthenticationMethod

    @property
    def ipProtocol_(self):
        return self._artop_ipProtocol

    @property
    def localPortRangeEnd_(self):
        return self._artop_localPortRangeEnd

    @property
    def localPortRangeStart_(self):
        return self._artop_localPortRangeStart

    @property
    def mode_(self):
        return self._artop_mode

    @property
    def policy_(self):
        return self._artop_policy

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def remotePortRangeEnd_(self):
        return self._artop_remotePortRangeEnd

    @property
    def remotePortRangeStart_(self):
        return self._artop_remotePortRangeStart

    @property
    def ref_iPSecConfig_(self):
        return self._artop_ipSecConfig

    @property
    def iPSecConfig_(self):
        if self._artop_ipSecConfig is not None:
            if hasattr(self._artop_ipSecConfig, "uuid"):
                return self._artop_ipSecConfig.uuid
        return

    @property
    def ref_remoteIpAddress_(self):
        return self._artop_remoteIpAddressRef

    @property
    def remoteIpAddress_(self):
        return self._artop_remoteIpAddressRef
