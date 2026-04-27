# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecureCommunicationProps.py
from .ARObject import ARObject

class SecureCommunicationProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SecuredIPdu import SecuredIPdu
        self._artop_authAlgorithm = None
        self._artop_authDataFreshnessLength = None
        self._artop_authDataFreshnessStartPosition = None
        self._artop_authInfoTxLength = None
        self._artop_authenticationBuildAttempts = None
        self._artop_authenticationRetries = None
        self._artop_dataId = None
        self._artop_freshnessCounterSyncAttempts = None
        self._artop_freshnessTimestampTimePeriodFactor = None
        self._artop_freshnessValueId = None
        self._artop_freshnessValueLength = None
        self._artop_freshnessValueTxLength = None
        self._artop_messageLinkLength = None
        self._artop_messageLinkPosition = None
        self._artop_secondaryFreshnessValueId = None
        self._artop_securedAreaLength = None
        self._artop_securedAreaOffset = None
        self._artop_useFreshnessTimestamp = None
        self._artop_securedIPdu = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_securedIPdu": "SECURED-I-PDU"})

    @property
    def authAlgorithm_(self):
        return self._artop_authAlgorithm

    @property
    def authDataFreshnessLength_(self):
        return self._artop_authDataFreshnessLength

    @property
    def authDataFreshnessStartPosition_(self):
        return self._artop_authDataFreshnessStartPosition

    @property
    def authInfoTxLength_(self):
        return self._artop_authInfoTxLength

    @property
    def authenticationBuildAttempts_(self):
        return self._artop_authenticationBuildAttempts

    @property
    def authenticationRetries_(self):
        return self._artop_authenticationRetries

    @property
    def dataId_(self):
        return self._artop_dataId

    @property
    def freshnessCounterSyncAttempts_(self):
        return self._artop_freshnessCounterSyncAttempts

    @property
    def freshnessTimestampTimePeriodFactor_(self):
        return self._artop_freshnessTimestampTimePeriodFactor

    @property
    def freshnessValueId_(self):
        return self._artop_freshnessValueId

    @property
    def freshnessValueLength_(self):
        return self._artop_freshnessValueLength

    @property
    def freshnessValueTxLength_(self):
        return self._artop_freshnessValueTxLength

    @property
    def messageLinkLength_(self):
        return self._artop_messageLinkLength

    @property
    def messageLinkPosition_(self):
        return self._artop_messageLinkPosition

    @property
    def secondaryFreshnessValueId_(self):
        return self._artop_secondaryFreshnessValueId

    @property
    def securedAreaLength_(self):
        return self._artop_securedAreaLength

    @property
    def securedAreaOffset_(self):
        return self._artop_securedAreaOffset

    @property
    def useFreshnessTimestamp_(self):
        if self._artop_useFreshnessTimestamp:
            if self._artop_useFreshnessTimestamp == "true":
                return True
            return False
        else:
            return self._artop_useFreshnessTimestamp

    @property
    def ref_securedIPdu_(self):
        return self._artop_securedIPdu

    @property
    def securedIPdu_(self):
        if self._artop_securedIPdu is not None:
            if hasattr(self._artop_securedIPdu, "uuid"):
                return self._artop_securedIPdu.uuid
        return
