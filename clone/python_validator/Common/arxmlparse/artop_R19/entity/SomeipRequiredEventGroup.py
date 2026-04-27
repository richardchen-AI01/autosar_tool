# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipRequiredEventGroup.py
from .Referrable import Referrable

class SomeipRequiredEventGroup(Referrable):

    def __init__(self):
        super().__init__()
        from .RequiredSomeipServiceInstance import RequiredSomeipServiceInstance
        from .SomeipEventGroup import SomeipEventGroup
        from .SomeipSdClientEventGroupTimingConfig import SomeipSdClientEventGroupTimingConfig
        self._artop_requiredSomeipServiceInstance = None
        self._artop_eventGroupRef = None
        self._artop_sdClientEventGroupTimingConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_requiredSomeipServiceInstance':"REQUIRED-SOMEIP-SERVICE-INSTANCE", 
         '_artop_eventGroupRef':"SOMEIP-EVENT-GROUP", 
         '_artop_sdClientEventGroupTimingConfigRef':"SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"})

    @property
    def ref_requiredSomeipServiceInstance_(self):
        return self._artop_requiredSomeipServiceInstance

    @property
    def requiredSomeipServiceInstance_(self):
        if self._artop_requiredSomeipServiceInstance is not None:
            if hasattr(self._artop_requiredSomeipServiceInstance, "uuid"):
                return self._artop_requiredSomeipServiceInstance.uuid
        return

    @property
    def ref_eventGroup_(self):
        return self._artop_eventGroupRef

    @property
    def eventGroup_(self):
        if self._artop_eventGroupRef is not None:
            if hasattr(self._artop_eventGroupRef, "uuid"):
                return self._artop_eventGroupRef.uuid
        return

    @property
    def ref_sdClientEventGroupTimingConfig_(self):
        return self._artop_sdClientEventGroupTimingConfigRef

    @property
    def sdClientEventGroupTimingConfig_(self):
        if self._artop_sdClientEventGroupTimingConfigRef is not None:
            if hasattr(self._artop_sdClientEventGroupTimingConfigRef, "uuid"):
                return self._artop_sdClientEventGroupTimingConfigRef.uuid
        return
