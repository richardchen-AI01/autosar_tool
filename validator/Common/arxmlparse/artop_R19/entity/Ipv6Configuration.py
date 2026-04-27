# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Ipv6Configuration.py
from .NetworkEndpointAddress import NetworkEndpointAddress

class Ipv6Configuration(NetworkEndpointAddress):

    def __init__(self):
        super().__init__()
        self._artop_assignmentPriority = None
        self._artop_defaultRouter = None
        self._artop_dnsServerAddress = None
        self._artop_enableAnycast = None
        self._artop_hopCount = None
        self._artop_ipAddressKeepBehavior = None
        self._artop_ipAddressPrefixLength = None
        self._artop_ipv6Address = None
        self._artop_ipv6AddressSource = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def assignmentPriority_(self):
        return self._artop_assignmentPriority

    @property
    def defaultRouter_(self):
        return self._artop_defaultRouter

    @property
    def dnsServerAddress_(self):
        return self._artop_dnsServerAddress

    @property
    def enableAnycast_(self):
        if self._artop_enableAnycast:
            if self._artop_enableAnycast == "true":
                return True
            return False
        else:
            return self._artop_enableAnycast

    @property
    def hopCount_(self):
        return self._artop_hopCount

    @property
    def ipAddressKeepBehavior_(self):
        return self._artop_ipAddressKeepBehavior

    @property
    def ipAddressPrefixLength_(self):
        return self._artop_ipAddressPrefixLength

    @property
    def ipv6Address_(self):
        return self._artop_ipv6Address

    @property
    def ipv6AddressSource_(self):
        return self._artop_ipv6AddressSource
