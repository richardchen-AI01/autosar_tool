# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipServiceInterfaceDeployment.py
from .ServiceInterfaceDeployment import ServiceInterfaceDeployment

class SomeipServiceInterfaceDeployment(ServiceInterfaceDeployment):

    def __init__(self):
        super().__init__()
        from .SomeipEventGroup import SomeipEventGroup
        from .SomeipServiceVersion import SomeipServiceVersion
        self._artop_serviceInterfaceId = None
        self._artop_eventGroup = []
        self._artop_serviceInterfaceVersion = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_eventGroup':"SOMEIP-EVENT-GROUP", 
         '_artop_serviceInterfaceVersion':"SOMEIP-SERVICE-VERSION"})

    @property
    def serviceInterfaceId_(self):
        return self._artop_serviceInterfaceId

    @property
    def eventGroups_SomeipEventGroup(self):
        return self._artop_eventGroup

    @property
    def ref_serviceInterfaceVersion_(self):
        return self._artop_serviceInterfaceVersion

    @property
    def serviceInterfaceVersion_(self):
        if self._artop_serviceInterfaceVersion is not None:
            if hasattr(self._artop_serviceInterfaceVersion, "uuid"):
                return self._artop_serviceInterfaceVersion.uuid
        return
