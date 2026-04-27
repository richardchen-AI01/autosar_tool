# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CryptoServiceCertificate.py
from .ARElement import ARElement

class CryptoServiceCertificate(ARElement):

    def __init__(self):
        super().__init__()
        self._artop_algorithmFamily = None
        self._artop_format = None
        self._artop_maximumLength = None
        self._artop_nextHigherCertificateRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_nextHigherCertificateRef": "CRYPTO-SERVICE-CERTIFICATE"})

    @property
    def algorithmFamily_(self):
        return self._artop_algorithmFamily

    @property
    def format_(self):
        return self._artop_format

    @property
    def maximumLength_(self):
        return self._artop_maximumLength

    @property
    def ref_nextHigherCertificate_(self):
        return self._artop_nextHigherCertificateRef

    @property
    def nextHigherCertificate_(self):
        if self._artop_nextHigherCertificateRef is not None:
            if hasattr(self._artop_nextHigherCertificateRef, "uuid"):
                return self._artop_nextHigherCertificateRef.uuid
        return
