# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CryptoServiceKey.py
from .ARElement import ARElement

class CryptoServiceKey(ARElement):

    def __init__(self):
        super().__init__()
        from .ValueSpecification import ValueSpecification
        self._artop_algorithmFamily = None
        self._artop_keyGeneration = None
        self._artop_keyStorageType = None
        self._artop_length = None
        self._artop_developmentValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_developmentValue": "VALUE-SPECIFICATION"})

    @property
    def algorithmFamily_(self):
        return self._artop_algorithmFamily

    @property
    def keyGeneration_(self):
        return self._artop_keyGeneration

    @property
    def keyStorageType_(self):
        return self._artop_keyStorageType

    @property
    def length_(self):
        return self._artop_length

    @property
    def ref_developmentValue_(self):
        return self._artop_developmentValue

    @property
    def developmentValue_(self):
        if self._artop_developmentValue is not None:
            if hasattr(self._artop_developmentValue, "uuid"):
                return self._artop_developmentValue.uuid
        return
