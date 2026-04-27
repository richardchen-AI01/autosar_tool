# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CryptoKeySlot.py
from .Identifiable import Identifiable

class CryptoKeySlot(Identifiable):

    def __init__(self):
        super().__init__()
        from .CryptoModuleInstantiation import CryptoModuleInstantiation
        self._artop_algorithmFamily = None
        self._artop_length = None
        self._artop_cryptoModuleInstantiation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_cryptoModuleInstantiation": "CRYPTO-MODULE-INSTANTIATION"})

    @property
    def algorithmFamily_(self):
        return self._artop_algorithmFamily

    @property
    def length_(self):
        return self._artop_length

    @property
    def ref_cryptoModuleInstantiation_(self):
        return self._artop_cryptoModuleInstantiation

    @property
    def cryptoModuleInstantiation_(self):
        if self._artop_cryptoModuleInstantiation is not None:
            if hasattr(self._artop_cryptoModuleInstantiation, "uuid"):
                return self._artop_cryptoModuleInstantiation.uuid
        return
