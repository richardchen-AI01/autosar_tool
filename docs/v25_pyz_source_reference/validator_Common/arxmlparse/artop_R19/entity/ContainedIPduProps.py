# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ContainedIPduProps.py
from .ARObject import ARObject

class ContainedIPduProps(ARObject):

    def __init__(self):
        super().__init__()
        from .IPdu import IPdu
        self._artop_collectionSemantics = None
        self._artop_headerIdLongHeader = None
        self._artop_headerIdShortHeader = None
        self._artop_offset = None
        self._artop_priority = None
        self._artop_timeout = None
        self._artop_trigger = None
        self._artop_updateIndicationBitPosition = None
        self._artop_iPdu = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_iPdu": "I-PDU"})

    @property
    def collectionSemantics_(self):
        return self._artop_collectionSemantics

    @property
    def headerIdLongHeader_(self):
        return self._artop_headerIdLongHeader

    @property
    def headerIdShortHeader_(self):
        return self._artop_headerIdShortHeader

    @property
    def offset_(self):
        return self._artop_offset

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def timeout_(self):
        return self._artop_timeout

    @property
    def trigger_(self):
        return self._artop_trigger

    @property
    def updateIndicationBitPosition_(self):
        return self._artop_updateIndicationBitPosition

    @property
    def ref_iPdu_(self):
        return self._artop_iPdu

    @property
    def iPdu_(self):
        if self._artop_iPdu is not None:
            if hasattr(self._artop_iPdu, "uuid"):
                return self._artop_iPdu.uuid
        return
