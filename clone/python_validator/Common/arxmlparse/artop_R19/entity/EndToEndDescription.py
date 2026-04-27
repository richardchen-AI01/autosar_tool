# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndDescription.py
from .ARObject import ARObject

class EndToEndDescription(ARObject):

    def __init__(self):
        super().__init__()
        from .EndToEndProtection import EndToEndProtection
        self._artop_category = None
        self._artop_dataId = None
        self._artop_dataIdMode = None
        self._artop_dataLength = None
        self._artop_maxDeltaCounterInit = None
        self._artop_crcOffset = None
        self._artop_counterOffset = None
        self._artop_maxNoNewOrRepeatedData = None
        self._artop_syncCounterInit = None
        self._artop_dataIdNibbleOffset = None
        self._artop_endToEndProtection = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_endToEndProtection": "END-TO-END-PROTECTION"})

    @property
    def category_(self):
        return self._artop_category

    @property
    def dataId_(self):
        return self._artop_dataId

    @property
    def dataIdMode_(self):
        return self._artop_dataIdMode

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def maxDeltaCounterInit_(self):
        return self._artop_maxDeltaCounterInit

    @property
    def crcOffset_(self):
        return self._artop_crcOffset

    @property
    def counterOffset_(self):
        return self._artop_counterOffset

    @property
    def maxNoNewOrRepeatedData_(self):
        return self._artop_maxNoNewOrRepeatedData

    @property
    def syncCounterInit_(self):
        return self._artop_syncCounterInit

    @property
    def dataIdNibbleOffset_(self):
        return self._artop_dataIdNibbleOffset

    @property
    def ref_endToEndProtection_(self):
        return self._artop_endToEndProtection

    @property
    def endToEndProtection_(self):
        if self._artop_endToEndProtection is not None:
            if hasattr(self._artop_endToEndProtection, "uuid"):
                return self._artop_endToEndProtection.uuid
        return
