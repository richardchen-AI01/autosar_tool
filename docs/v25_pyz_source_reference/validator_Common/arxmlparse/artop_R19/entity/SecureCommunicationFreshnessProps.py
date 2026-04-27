# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecureCommunicationFreshnessProps.py
from .Identifiable import Identifiable

class SecureCommunicationFreshnessProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SecureCommunicationPropsSet import SecureCommunicationPropsSet
        self._artop_freshnessCounterSyncAttempts = None
        self._artop_freshnessTimestampTimePeriodFactor = None
        self._artop_freshnessValueLength = None
        self._artop_freshnessValueTxLength = None
        self._artop_useFreshnessTimestamp = None
        self._artop_secureCommunicationPropsSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_secureCommunicationPropsSet": "SECURE-COMMUNICATION-PROPS-SET"})

    @property
    def freshnessCounterSyncAttempts_(self):
        return self._artop_freshnessCounterSyncAttempts

    @property
    def freshnessTimestampTimePeriodFactor_(self):
        return self._artop_freshnessTimestampTimePeriodFactor

    @property
    def freshnessValueLength_(self):
        return self._artop_freshnessValueLength

    @property
    def freshnessValueTxLength_(self):
        return self._artop_freshnessValueTxLength

    @property
    def useFreshnessTimestamp_(self):
        if self._artop_useFreshnessTimestamp:
            if self._artop_useFreshnessTimestamp == "true":
                return True
            return False
        else:
            return self._artop_useFreshnessTimestamp

    @property
    def ref_secureCommunicationPropsSet_(self):
        return self._artop_secureCommunicationPropsSet

    @property
    def secureCommunicationPropsSet_(self):
        if self._artop_secureCommunicationPropsSet is not None:
            if hasattr(self._artop_secureCommunicationPropsSet, "uuid"):
                return self._artop_secureCommunicationPropsSet.uuid
        return
