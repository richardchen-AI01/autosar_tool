# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApSomeipTransformationProps.py
from .TransformationProps import TransformationProps

class ApSomeipTransformationProps(TransformationProps):

    def __init__(self):
        super().__init__()
        self._artop_alignment = None
        self._artop_byteOrder = None
        self._artop_implementsLegacyStringSerialization = None
        self._artop_isDynamicLengthFieldSize = None
        self._artop_sessionHandling = None
        self._artop_sizeOfArrayLengthField = None
        self._artop_sizeOfStringLengthField = None
        self._artop_sizeOfStructLengthField = None
        self._artop_sizeOfUnionLengthField = None
        self._artop_sizeOfUnionTypeSelectorField = None
        self._artop_stringEncoding = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def alignment_(self):
        return self._artop_alignment

    @property
    def byteOrder_(self):
        return self._artop_byteOrder

    @property
    def implementsLegacyStringSerialization_(self):
        if self._artop_implementsLegacyStringSerialization:
            if self._artop_implementsLegacyStringSerialization == "true":
                return True
            return False
        else:
            return self._artop_implementsLegacyStringSerialization

    @property
    def isDynamicLengthFieldSize_(self):
        if self._artop_isDynamicLengthFieldSize:
            if self._artop_isDynamicLengthFieldSize == "true":
                return True
            return False
        else:
            return self._artop_isDynamicLengthFieldSize

    @property
    def sessionHandling_(self):
        return self._artop_sessionHandling

    @property
    def sizeOfArrayLengthField_(self):
        return self._artop_sizeOfArrayLengthField

    @property
    def sizeOfStringLengthField_(self):
        return self._artop_sizeOfStringLengthField

    @property
    def sizeOfStructLengthField_(self):
        return self._artop_sizeOfStructLengthField

    @property
    def sizeOfUnionLengthField_(self):
        return self._artop_sizeOfUnionLengthField

    @property
    def sizeOfUnionTypeSelectorField_(self):
        return self._artop_sizeOfUnionTypeSelectorField

    @property
    def stringEncoding_(self):
        return self._artop_stringEncoding
