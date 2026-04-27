# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipEventGroup.py
from .Identifiable import Identifiable

class SomeipEventGroup(Identifiable):

    def __init__(self):
        super().__init__()
        from .SomeipServiceInterfaceDeployment import SomeipServiceInterfaceDeployment
        from .SomeipEventDeployment import SomeipEventDeployment
        self._artop_eventGroupId = None
        self._artop_someipServiceInterfaceDeployment = None
        self._artop_eventRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_someipServiceInterfaceDeployment':"SOMEIP-SERVICE-INTERFACE-DEPLOYMENT", 
         '_artop_eventRef':"SOMEIP-EVENT-DEPLOYMENT"})

    @property
    def eventGroupId_(self):
        return self._artop_eventGroupId

    @property
    def ref_someipServiceInterfaceDeployment_(self):
        return self._artop_someipServiceInterfaceDeployment

    @property
    def someipServiceInterfaceDeployment_(self):
        if self._artop_someipServiceInterfaceDeployment is not None:
            if hasattr(self._artop_someipServiceInterfaceDeployment, "uuid"):
                return self._artop_someipServiceInterfaceDeployment.uuid
        return

    @property
    def ref_events_(self):
        return self._artop_eventRef

    @property
    def events_(self):
        return self._artop_eventRef
