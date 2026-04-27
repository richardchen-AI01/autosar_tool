# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceMapping.py
from .Identifiable import Identifiable

class ServiceInterfaceMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .ServiceInterfaceMappingSet import ServiceInterfaceMappingSet
        from .ServiceInterface import ServiceInterface
        self._artop_serviceInterfaceMappingSet = None
        self._artop_compositeServiceInterfaceRef = None
        self._artop_sourceServiceInterfaceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_serviceInterfaceMappingSet':"SERVICE-INTERFACE-MAPPING-SET", 
         '_artop_compositeServiceInterfaceRef':"SERVICE-INTERFACE", 
         '_artop_sourceServiceInterfaceRef':"SERVICE-INTERFACE"})

    @property
    def ref_serviceInterfaceMappingSet_(self):
        return self._artop_serviceInterfaceMappingSet

    @property
    def serviceInterfaceMappingSet_(self):
        if self._artop_serviceInterfaceMappingSet is not None:
            if hasattr(self._artop_serviceInterfaceMappingSet, "uuid"):
                return self._artop_serviceInterfaceMappingSet.uuid
        return

    @property
    def ref_compositeServiceInterface_(self):
        return self._artop_compositeServiceInterfaceRef

    @property
    def compositeServiceInterface_(self):
        if self._artop_compositeServiceInterfaceRef is not None:
            if hasattr(self._artop_compositeServiceInterfaceRef, "uuid"):
                return self._artop_compositeServiceInterfaceRef.uuid
        return

    @property
    def ref_sourceServiceInterfaces_(self):
        return self._artop_sourceServiceInterfaceRef

    @property
    def sourceServiceInterfaces_(self):
        return self._artop_sourceServiceInterfaceRef
