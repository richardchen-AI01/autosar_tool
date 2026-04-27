# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlsCryptoCipherSuite.py
from .Identifiable import Identifiable

class TlsCryptoCipherSuite(Identifiable):

    def __init__(self):
        super().__init__()
        from .CryptoServicePrimitive import CryptoServicePrimitive
        from .CryptoServiceCertificate import CryptoServiceCertificate
        from .CryptoServiceKey import CryptoServiceKey
        from .TlsPskIdentity import TlsPskIdentity
        self._artop_priority = None
        self._artop_version = None
        self._artop_authenticationRef = None
        self._artop_certificateRef = None
        self._artop_encryptionRef = None
        self._artop_keyExchangeRef = []
        self._artop_preSharedKeyRef = None
        self._artop_pskIdentity = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_authenticationRef': '"CRYPTO-SERVICE-PRIMITIVE"', 
         '_artop_certificateRef': '"CRYPTO-SERVICE-CERTIFICATE"', 
         '_artop_encryptionRef': '"CRYPTO-SERVICE-PRIMITIVE"', 
         '_artop_keyExchangeRef': '"CRYPTO-SERVICE-PRIMITIVE"', 
         '_artop_preSharedKeyRef': '"CRYPTO-SERVICE-KEY"', 
         '_artop_pskIdentity': '"TLS-PSK-IDENTITY"'})

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def version_(self):
        return self._artop_version

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
    def ref_certificate_(self):
        return self._artop_certificateRef

    @property
    def certificate_(self):
        if self._artop_certificateRef is not None:
            if hasattr(self._artop_certificateRef, "uuid"):
                return self._artop_certificateRef.uuid
        return

    @property
    def ref_encryption_(self):
        return self._artop_encryptionRef

    @property
    def encryption_(self):
        if self._artop_encryptionRef is not None:
            if hasattr(self._artop_encryptionRef, "uuid"):
                return self._artop_encryptionRef.uuid
        return

    @property
    def ref_keyExchanges_(self):
        return self._artop_keyExchangeRef

    @property
    def keyExchanges_(self):
        return self._artop_keyExchangeRef

    @property
    def ref_preSharedKey_(self):
        return self._artop_preSharedKeyRef

    @property
    def preSharedKey_(self):
        if self._artop_preSharedKeyRef is not None:
            if hasattr(self._artop_preSharedKeyRef, "uuid"):
                return self._artop_preSharedKeyRef.uuid
        return

    @property
    def ref_pskIdentity_(self):
        return self._artop_pskIdentity

    @property
    def pskIdentity_(self):
        if self._artop_pskIdentity is not None:
            if hasattr(self._artop_pskIdentity, "uuid"):
                return self._artop_pskIdentity.uuid
        return
