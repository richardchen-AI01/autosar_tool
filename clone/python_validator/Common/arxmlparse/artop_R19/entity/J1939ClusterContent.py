# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939ClusterContent.py
from .AbstractCanClusterContent import AbstractCanClusterContent

class J1939ClusterContent(AbstractCanClusterContent):

    def __init__(self):
        super().__init__()
        self._artop_networkId = None
        self._artop_request2Support = None
        self._artop_usesAddressArbitration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def networkId_(self):
        return self._artop_networkId

    @property
    def request2Support_(self):
        if self._artop_request2Support:
            if self._artop_request2Support == "true":
                return True
            return False
        else:
            return self._artop_request2Support

    @property
    def usesAddressArbitration_(self):
        if self._artop_usesAddressArbitration:
            if self._artop_usesAddressArbitration == "true":
                return True
            return False
        else:
            return self._artop_usesAddressArbitration
