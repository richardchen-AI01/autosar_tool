# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterfacePedigree.py
from .ARElement import ARElement

class ServiceInterfacePedigree(ARElement):

    def __init__(self):
        super().__init__()
        from .ServiceInterface import ServiceInterface
        self._artop_serviceInterfaceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_serviceInterfaceRef": "SERVICE-INTERFACE"})

    @property
    def ref_serviceInterfaces_(self):
        return self._artop_serviceInterfaceRef

    @property
    def serviceInterfaces_(self):
        return self._artop_serviceInterfaceRef
