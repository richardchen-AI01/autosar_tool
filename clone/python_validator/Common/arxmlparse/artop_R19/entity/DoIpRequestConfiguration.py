# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpRequestConfiguration.py
from .ARObject import ARObject

class DoIpRequestConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .DoIpInstantiation import DoIpInstantiation
        self._artop_endAddress = None
        self._artop_requestType = None
        self._artop_startAddress = None
        self._artop_doIpInstantiation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_doIpInstantiation": "DO-IP-INSTANTIATION"})

    @property
    def endAddress_(self):
        return self._artop_endAddress

    @property
    def requestType_(self):
        return self._artop_requestType

    @property
    def startAddress_(self):
        return self._artop_startAddress

    @property
    def ref_doIpInstantiation_(self):
        return self._artop_doIpInstantiation

    @property
    def doIpInstantiation_(self):
        if self._artop_doIpInstantiation is not None:
            if hasattr(self._artop_doIpInstantiation, "uuid"):
                return self._artop_doIpInstantiation.uuid
        return
