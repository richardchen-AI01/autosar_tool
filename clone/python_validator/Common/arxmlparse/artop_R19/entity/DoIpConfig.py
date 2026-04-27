# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpConfig.py
from .ARObject import ARObject

class DoIpConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .EcuInstance import EcuInstance
        from .DoIpInterface import DoIpInterface
        from .DoIpLogicAddress import DoIpLogicAddress
        self._artop_ecuInstance = None
        self._artop_doipInterface = []
        self._artop_logicAddress = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecuInstance':"ECU-INSTANCE", 
         '_artop_doipInterface':"DO-IP-INTERFACE", 
         '_artop_logicAddress':"DO-IP-LOGIC-ADDRESS"})

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstance

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstance is not None:
            if hasattr(self._artop_ecuInstance, "uuid"):
                return self._artop_ecuInstance.uuid
        return

    @property
    def doipInterfaces_DoIpInterface(self):
        return self._artop_doipInterface

    @property
    def ref_logicAddress_(self):
        return self._artop_logicAddress

    @property
    def logicAddress_(self):
        if self._artop_logicAddress is not None:
            if hasattr(self._artop_logicAddress, "uuid"):
                return self._artop_logicAddress.uuid
        return
