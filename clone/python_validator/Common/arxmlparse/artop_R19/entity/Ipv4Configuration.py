# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Ipv4Configuration.py
from .NetworkEndpointAddress import NetworkEndpointAddress

class Ipv4Configuration(NetworkEndpointAddress):

    def __init__(self):
        super().__init__()
        self._artop_assignmentPriority = None
        self._artop_defaultGateway = None
        self._artop_dnsServerAddress = None
        self._artop_ipAddressKeepBehavior = None
        self._artop_ipv4Address = None
        self._artop_ipv4AddressSource = None
        self._artop_networkMask = None
        self._artop_ttl = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def assignmentPriority_(self):
        return self._artop_assignmentPriority

    @property
    def defaultGateway_(self):
        return self._artop_defaultGateway

    @property
    def dnsServerAddress_(self):
        return self._artop_dnsServerAddress

    @property
    def ipAddressKeepBehavior_(self):
        return self._artop_ipAddressKeepBehavior

    @property
    def ipv4Address_(self):
        return self._artop_ipv4Address

    @property
    def ipv4AddressSource_(self):
        return self._artop_ipv4AddressSource

    @property
    def networkMask_(self):
        return self._artop_networkMask

    @property
    def ttl_(self):
        return self._artop_ttl
