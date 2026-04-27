# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerInterfaceMapping.py
from .PortInterfaceMapping import PortInterfaceMapping

class ClientServerInterfaceMapping(PortInterfaceMapping):

    def __init__(self):
        super().__init__()
        from .ClientServerApplicationErrorMapping import ClientServerApplicationErrorMapping
        from .ClientServerOperationMapping import ClientServerOperationMapping
        self._artop_errorMapping = []
        self._artop_operationMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_errorMapping':"CLIENT-SERVER-APPLICATION-ERROR-MAPPING", 
         '_artop_operationMapping':"CLIENT-SERVER-OPERATION-MAPPING"})

    @property
    def errorMappings_ClientServerApplicationErrorMapping(self):
        return self._artop_errorMapping

    @property
    def operationMappings_ClientServerOperationMapping(self):
        return self._artop_operationMapping
