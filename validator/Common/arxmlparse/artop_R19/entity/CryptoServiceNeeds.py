# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CryptoServiceNeeds.py
from .ServiceNeeds import ServiceNeeds

class CryptoServiceNeeds(ServiceNeeds):

    def __init__(self):
        super().__init__()
        self._artop_algorithmFamily = None
        self._artop_algorithmMode = None
        self._artop_cryptoKeyDescription = None
        self._artop_maximumKeyLength = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def algorithmFamily_(self):
        return self._artop_algorithmFamily

    @property
    def algorithmMode_(self):
        return self._artop_algorithmMode

    @property
    def cryptoKeyDescription_(self):
        return self._artop_cryptoKeyDescription

    @property
    def maximumKeyLength_(self):
        return self._artop_maximumKeyLength
