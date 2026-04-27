# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthTSynCrcFlags.py
from .ARObject import ARObject

class EthTSynCrcFlags(ARObject):

    def __init__(self):
        super().__init__()
        from .EthGlobalTimeDomainProps import EthGlobalTimeDomainProps
        self._artop_crcCorrectionField = None
        self._artop_crcDomainNumber = None
        self._artop_crcMessageLength = None
        self._artop_crcPreciseOriginTimestamp = None
        self._artop_crcSequenceId = None
        self._artop_crcSourcePortIdentity = None
        self._artop_ethGlobalTimeDomainProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ethGlobalTimeDomainProps": "ETH-GLOBAL-TIME-DOMAIN-PROPS"})

    @property
    def crcCorrectionField_(self):
        if self._artop_crcCorrectionField:
            if self._artop_crcCorrectionField == "true":
                return True
            return False
        else:
            return self._artop_crcCorrectionField

    @property
    def crcDomainNumber_(self):
        if self._artop_crcDomainNumber:
            if self._artop_crcDomainNumber == "true":
                return True
            return False
        else:
            return self._artop_crcDomainNumber

    @property
    def crcMessageLength_(self):
        if self._artop_crcMessageLength:
            if self._artop_crcMessageLength == "true":
                return True
            return False
        else:
            return self._artop_crcMessageLength

    @property
    def crcPreciseOriginTimestamp_(self):
        if self._artop_crcPreciseOriginTimestamp:
            if self._artop_crcPreciseOriginTimestamp == "true":
                return True
            return False
        else:
            return self._artop_crcPreciseOriginTimestamp

    @property
    def crcSequenceId_(self):
        if self._artop_crcSequenceId:
            if self._artop_crcSequenceId == "true":
                return True
            return False
        else:
            return self._artop_crcSequenceId

    @property
    def crcSourcePortIdentity_(self):
        if self._artop_crcSourcePortIdentity:
            if self._artop_crcSourcePortIdentity == "true":
                return True
            return False
        else:
            return self._artop_crcSourcePortIdentity

    @property
    def ref_ethGlobalTimeDomainProps_(self):
        return self._artop_ethGlobalTimeDomainProps

    @property
    def ethGlobalTimeDomainProps_(self):
        if self._artop_ethGlobalTimeDomainProps is not None:
            if hasattr(self._artop_ethGlobalTimeDomainProps, "uuid"):
                return self._artop_ethGlobalTimeDomainProps.uuid
        return
