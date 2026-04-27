# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecOcCryptoServiceMapping.py
from .CryptoServiceMapping import CryptoServiceMapping

class SecOcCryptoServiceMapping(CryptoServiceMapping):

    def __init__(self):
        super().__init__()
        from .CryptoServicePrimitive import CryptoServicePrimitive
        from .CryptoServiceKey import CryptoServiceKey
        from .CryptoServiceQueue import CryptoServiceQueue
        self._artop_authenticationRef = None
        self._artop_cryptoServiceKeyRef = None
        self._artop_cryptoServiceQueueRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_authenticationRef':"CRYPTO-SERVICE-PRIMITIVE", 
         '_artop_cryptoServiceKeyRef':"CRYPTO-SERVICE-KEY", 
         '_artop_cryptoServiceQueueRef':"CRYPTO-SERVICE-QUEUE"})

    @property
    def ref_authentication_(self):
        return self._artop_authenticationRef

    @property
    def authentication_(self):
        if self._artop_authenticationRef is not None:
            if hasattr(self._artop_authenticationRef, "uuid"):
                return self._artop_authenticationRef.uuid
        return

    @property
    def ref_cryptoServiceKey_(self):
        return self._artop_cryptoServiceKeyRef

    @property
    def cryptoServiceKey_(self):
        if self._artop_cryptoServiceKeyRef is not None:
            if hasattr(self._artop_cryptoServiceKeyRef, "uuid"):
                return self._artop_cryptoServiceKeyRef.uuid
        return

    @property
    def ref_cryptoServiceQueue_(self):
        return self._artop_cryptoServiceQueueRef

    @property
    def cryptoServiceQueue_(self):
        if self._artop_cryptoServiceQueueRef is not None:
            if hasattr(self._artop_cryptoServiceQueueRef, "uuid"):
                return self._artop_cryptoServiceQueueRef.uuid
        return
