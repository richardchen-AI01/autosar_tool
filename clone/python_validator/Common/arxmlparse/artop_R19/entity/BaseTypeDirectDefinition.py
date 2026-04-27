# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BaseTypeDirectDefinition.py
from .BaseTypeDefinition import BaseTypeDefinition

class BaseTypeDirectDefinition(BaseTypeDefinition):

    def __init__(self):
        super().__init__()
        self._artop_baseTypeSize = None
        self._artop_maxBaseTypeSize = None
        self._artop_baseTypeEncoding = None
        self._artop_memAlignment = None
        self._artop_byteOrder = None
        self._artop_nativeDeclaration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def baseTypeSize_(self):
        return self._artop_baseTypeSize

    @property
    def maxBaseTypeSize_(self):
        return self._artop_maxBaseTypeSize

    @property
    def baseTypeEncoding_(self):
        return self._artop_baseTypeEncoding

    @property
    def memAlignment_(self):
        return self._artop_memAlignment

    @property
    def byteOrder_(self):
        return self._artop_byteOrder

    @property
    def nativeDeclaration_(self):
        return self._artop_nativeDeclaration
