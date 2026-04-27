# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerInterfaceToBswModuleEntryBlueprintMapping.py
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement, AtpBlueprint):

    def __init__(self):
        super().__init__()
        from .ClientServerInterface import ClientServerInterface
        from .ClientServerOperationBlueprintMapping import ClientServerOperationBlueprintMapping
        from .PortDefinedArgumentBlueprint import PortDefinedArgumentBlueprint
        self._artop_clientServerInterfaceRef = None
        self._artop_operationMapping = []
        self._artop_portDefinedArgumentBlueprint = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_clientServerInterfaceRef':"CLIENT-SERVER-INTERFACE", 
         '_artop_operationMapping':"CLIENT-SERVER-OPERATION-BLUEPRINT-MAPPING", 
         '_artop_portDefinedArgumentBlueprint':"PORT-DEFINED-ARGUMENT-BLUEPRINT"})

    @property
    def ref_clientServerInterface_(self):
        return self._artop_clientServerInterfaceRef

    @property
    def clientServerInterface_(self):
        if self._artop_clientServerInterfaceRef is not None:
            if hasattr(self._artop_clientServerInterfaceRef, "uuid"):
                return self._artop_clientServerInterfaceRef.uuid
        return

    @property
    def operationMappings_ClientServerOperationBlueprintMapping(self):
        return self._artop_operationMapping

    @property
    def portDefinedArgumentBlueprints_PortDefinedArgumentBlueprint(self):
        return self._artop_portDefinedArgumentBlueprint
