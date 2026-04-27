# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CryptoModuleInstantiation.py
from .NonOsModuleInstantiation import NonOsModuleInstantiation

class CryptoModuleInstantiation(NonOsModuleInstantiation):

    def __init__(self):
        super().__init__()
        from .CryptoKeySlot import CryptoKeySlot
        from .SecureComConfigToCryptoKeySlotMapping import SecureComConfigToCryptoKeySlotMapping
        self._artop_keySlot = []
        self._artop_secureComConfigToKeySlotMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_keySlot':"CRYPTO-KEY-SLOT", 
         '_artop_secureComConfigToKeySlotMapping':"SECURE-COM-CONFIG-TO-CRYPTO-KEY-SLOT-MAPPING"})

    @property
    def keySlots_CryptoKeySlot(self):
        return self._artop_keySlot

    @property
    def secureComConfigToKeySlotMappings_SecureComConfigToCryptoKeySlotMapping(self):
        return self._artop_secureComConfigToKeySlotMapping
