# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdClientEventGroupTimingConfig.py
from .ARElement import ARElement

class SomeipSdClientEventGroupTimingConfig(ARElement):

    def __init__(self):
        super().__init__()
        from .RequestResponseDelay import RequestResponseDelay
        self._artop_subscribeEventgroupRetryDelay = None
        self._artop_subscribeEventgroupRetryMax = None
        self._artop_timeToLive = None
        self._artop_requestResponseDelay = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_requestResponseDelay": "REQUEST-RESPONSE-DELAY"})

    @property
    def subscribeEventgroupRetryDelay_(self):
        return self._artop_subscribeEventgroupRetryDelay

    @property
    def subscribeEventgroupRetryMax_(self):
        return self._artop_subscribeEventgroupRetryMax

    @property
    def timeToLive_(self):
        return self._artop_timeToLive

    @property
    def ref_requestResponseDelay_(self):
        return self._artop_requestResponseDelay

    @property
    def requestResponseDelay_(self):
        if self._artop_requestResponseDelay is not None:
            if hasattr(self._artop_requestResponseDelay, "uuid"):
                return self._artop_requestResponseDelay.uuid
        return
