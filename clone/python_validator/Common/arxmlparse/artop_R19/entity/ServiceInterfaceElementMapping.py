# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceElementMapping.py
from .Identifiable import Identifiable

class ServiceInterfaceElementMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ServiceInterfaceMappingSet import ServiceInterfaceMappingSet
        self._artop_serviceInterfaceMappingSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_serviceInterfaceMappingSet": "SERVICE-INTERFACE-MAPPING-SET"})

    @property
    def ref_serviceInterfaceMappingSet_(self):
        return self._artop_serviceInterfaceMappingSet

    @property
    def serviceInterfaceMappingSet_(self):
        if self._artop_serviceInterfaceMappingSet is not None:
            if hasattr(self._artop_serviceInterfaceMappingSet, "uuid"):
                return self._artop_serviceInterfaceMappingSet.uuid
        return
