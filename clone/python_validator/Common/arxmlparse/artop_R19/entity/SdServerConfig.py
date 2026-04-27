# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdServerConfig.py
from .ARObject import ARObject

class SdServerConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .TagWithOptionalValue import TagWithOptionalValue
        from .InitialSdDelayConfig import InitialSdDelayConfig
        from .RequestResponseDelay import RequestResponseDelay
        self._artop_offerCyclicDelay = None
        self._artop_serverServiceMajorVersion = None
        self._artop_serverServiceMinorVersion = None
        self._artop_ttl = None
        self._artop_capabilityRecord = []
        self._artop_initialOfferBehavior = None
        self._artop_requestResponseDelay = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_capabilityRecord':"TAG-WITH-OPTIONAL-VALUE", 
         '_artop_initialOfferBehavior':"INITIAL-SD-DELAY-CONFIG", 
         '_artop_requestResponseDelay':"REQUEST-RESPONSE-DELAY"})

    @property
    def offerCyclicDelay_(self):
        return self._artop_offerCyclicDelay

    @property
    def serverServiceMajorVersion_(self):
        return self._artop_serverServiceMajorVersion

    @property
    def serverServiceMinorVersion_(self):
        return self._artop_serverServiceMinorVersion

    @property
    def ttl_(self):
        return self._artop_ttl

    @property
    def capabilityRecords_TagWithOptionalValue(self):
        return self._artop_capabilityRecord

    @property
    def ref_initialOfferBehavior_(self):
        return self._artop_initialOfferBehavior

    @property
    def initialOfferBehavior_(self):
        if self._artop_initialOfferBehavior is not None:
            if hasattr(self._artop_initialOfferBehavior, "uuid"):
                return self._artop_initialOfferBehavior.uuid
        return

    @property
    def ref_requestResponseDelay_(self):
        return self._artop_requestResponseDelay

    @property
    def requestResponseDelay_(self):
        if self._artop_requestResponseDelay is not None:
            if hasattr(self._artop_requestResponseDelay, "uuid"):
                return self._artop_requestResponseDelay.uuid
        return
