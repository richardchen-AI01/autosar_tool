# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfaceMappingSet.py
from .ARElement import ARElement

class ServiceInterfaceMappingSet(ARElement):

    def __init__(self):
        super().__init__()
        from .ServiceInterfaceElementMapping import ServiceInterfaceElementMapping
        from .ServiceInterfaceMapping import ServiceInterfaceMapping
        self._artop_elementMapping = []
        self._artop_interfaceMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_elementMapping':"SERVICE-INTERFACE-ELEMENT-MAPPING", 
         '_artop_interfaceMapping':"SERVICE-INTERFACE-MAPPING"})

    @property
    def elementMappings_ServiceInterfaceElementMapping(self):
        return self._artop_elementMapping

    @property
    def interfaceMappings_ServiceInterfaceMapping(self):
        return self._artop_interfaceMapping
