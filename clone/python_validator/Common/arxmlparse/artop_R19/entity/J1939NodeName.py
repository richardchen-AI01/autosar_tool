# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939NodeName.py
from .ARObject import ARObject

class J1939NodeName(ARObject):

    def __init__(self):
        super().__init__()
        from .J1939NmNode import J1939NmNode
        self._artop_arbitraryAddressCapable = None
        self._artop_ecuInstance = None
        self._artop_function = None
        self._artop_functionInstance = None
        self._artop_identitiyNumber = None
        self._artop_industryGroup = None
        self._artop_manufacturerCode = None
        self._artop_vehicleSystem = None
        self._artop_vehicleSystemInstance = None
        self._artop_j1939NmNode = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_j1939NmNode": "J-1939-NM-NODE"})

    @property
    def arbitraryAddressCapable_(self):
        if self._artop_arbitraryAddressCapable:
            if self._artop_arbitraryAddressCapable == "true":
                return True
            return False
        else:
            return self._artop_arbitraryAddressCapable

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstance:
            return int(self._artop_ecuInstance)
        return self._artop_ecuInstance

    @property
    def function_(self):
        if self._artop_function:
            return int(self._artop_function)
        return self._artop_function

    @property
    def functionInstance_(self):
        if self._artop_functionInstance:
            return int(self._artop_functionInstance)
        return self._artop_functionInstance

    @property
    def identitiyNumber_(self):
        if self._artop_identitiyNumber:
            return int(self._artop_identitiyNumber)
        return self._artop_identitiyNumber

    @property
    def industryGroup_(self):
        if self._artop_industryGroup:
            return int(self._artop_industryGroup)
        return self._artop_industryGroup

    @property
    def manufacturerCode_(self):
        if self._artop_manufacturerCode:
            return int(self._artop_manufacturerCode)
        return self._artop_manufacturerCode

    @property
    def vehicleSystem_(self):
        if self._artop_vehicleSystem:
            return int(self._artop_vehicleSystem)
        return self._artop_vehicleSystem

    @property
    def vehicleSystemInstance_(self):
        if self._artop_vehicleSystemInstance:
            return int(self._artop_vehicleSystemInstance)
        return self._artop_vehicleSystemInstance

    @property
    def ref_j1939NmNode_(self):
        return self._artop_j1939NmNode

    @property
    def j1939NmNode_(self):
        if self._artop_j1939NmNode is not None:
            if hasattr(self._artop_j1939NmNode, "uuid"):
                return self._artop_j1939NmNode.uuid
        return
