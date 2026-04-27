# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IPduPort.py
from .CommConnectorPort import CommConnectorPort

class IPduPort(CommConnectorPort):

    def __init__(self):
        super().__init__()
        self._artop_iPduSignalProcessing = None
        self._artop_keyId = None
        self._artop_rxSecurityVerification = None
        self._artop_timestampRxAcceptanceWindow = None
        self._artop_useAuthDataFreshness = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def iPduSignalProcessing_(self):
        return self._artop_iPduSignalProcessing

    @property
    def keyId_(self):
        return self._artop_keyId

    @property
    def rxSecurityVerification_(self):
        if self._artop_rxSecurityVerification:
            if self._artop_rxSecurityVerification == "true":
                return True
            return False
        else:
            return self._artop_rxSecurityVerification

    @property
    def timestampRxAcceptanceWindow_(self):
        return self._artop_timestampRxAcceptanceWindow

    @property
    def useAuthDataFreshness_(self):
        if self._artop_useAuthDataFreshness:
            if self._artop_useAuthDataFreshness == "true":
                return True
            return False
        else:
            return self._artop_useAuthDataFreshness
