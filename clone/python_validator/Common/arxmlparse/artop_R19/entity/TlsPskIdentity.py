# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlsPskIdentity.py
from .ARObject import ARObject

class TlsPskIdentity(ARObject):

    def __init__(self):
        super().__init__()
        from .TlsCryptoCipherSuite import TlsCryptoCipherSuite
        from .CryptoServiceKey import CryptoServiceKey
        self._artop_pskIdentity = None
        self._artop_pskIdentityHint = None
        self._artop_tlsCryptoCipherSuite = None
        self._artop_preSharedKeyRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tlsCryptoCipherSuite':"TLS-CRYPTO-CIPHER-SUITE", 
         '_artop_preSharedKeyRef':"CRYPTO-SERVICE-KEY"})

    @property
    def pskIdentity_(self):
        return self._artop_pskIdentity

    @property
    def pskIdentityHint_(self):
        return self._artop_pskIdentityHint

    @property
    def ref_tlsCryptoCipherSuite_(self):
        return self._artop_tlsCryptoCipherSuite

    @property
    def tlsCryptoCipherSuite_(self):
        if self._artop_tlsCryptoCipherSuite is not None:
            if hasattr(self._artop_tlsCryptoCipherSuite, "uuid"):
                return self._artop_tlsCryptoCipherSuite.uuid
        return

    @property
    def ref_preSharedKey_(self):
        return self._artop_preSharedKeyRef

    @property
    def preSharedKey_(self):
        if self._artop_preSharedKeyRef is not None:
            if hasattr(self._artop_preSharedKeyRef, "uuid"):
                return self._artop_preSharedKeyRef.uuid
        return
