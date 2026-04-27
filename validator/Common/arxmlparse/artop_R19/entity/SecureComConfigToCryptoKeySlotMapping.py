# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecureComConfigToCryptoKeySlotMapping.py
from .ARObject import ARObject

class SecureComConfigToCryptoKeySlotMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .CryptoModuleInstantiation import CryptoModuleInstantiation
        from .CryptoKeySlot import CryptoKeySlot
        from .ServiceInterfaceElementSecureComConfig import ServiceInterfaceElementSecureComConfig
        self._artop_cryptoModuleInstantiation = None
        self._artop_cryptoKeySlotRef = None
        self._artop_secureComConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_cryptoModuleInstantiation':"CRYPTO-MODULE-INSTANTIATION", 
         '_artop_cryptoKeySlotRef':"CRYPTO-KEY-SLOT", 
         '_artop_secureComConfigRef':"SERVICE-INTERFACE-ELEMENT-SECURE-COM-CONFIG"})

    @property
    def ref_cryptoModuleInstantiation_(self):
        return self._artop_cryptoModuleInstantiation

    @property
    def cryptoModuleInstantiation_(self):
        if self._artop_cryptoModuleInstantiation is not None:
            if hasattr(self._artop_cryptoModuleInstantiation, "uuid"):
                return self._artop_cryptoModuleInstantiation.uuid
        return

    @property
    def ref_cryptoKeySlot_(self):
        return self._artop_cryptoKeySlotRef

    @property
    def cryptoKeySlot_(self):
        if self._artop_cryptoKeySlotRef is not None:
            if hasattr(self._artop_cryptoKeySlotRef, "uuid"):
                return self._artop_cryptoKeySlotRef.uuid
        return

    @property
    def ref_secureComConfig_(self):
        return self._artop_secureComConfigRef

    @property
    def secureComConfig_(self):
        if self._artop_secureComConfigRef is not None:
            if hasattr(self._artop_secureComConfigRef, "uuid"):
                return self._artop_secureComConfigRef.uuid
        return
