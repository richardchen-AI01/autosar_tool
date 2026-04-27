# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Pdu.py
from .FibexElement import FibexElement

class Pdu(FibexElement):

    def __init__(self):
        super().__init__()
        self._artop_hasDynamicLength = None
        self._artop_length = None
        self._artop_metaDataLength = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def hasDynamicLength_(self):
        if self._artop_hasDynamicLength:
            if self._artop_hasDynamicLength == "true":
                return True
            return False
        else:
            return self._artop_hasDynamicLength

    @property
    def length_(self):
        if self._artop_length:
            return int(self._artop_length)
        return self._artop_length

    @property
    def metaDataLength_(self):
        return self._artop_metaDataLength
