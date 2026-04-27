# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DltConfig.py
from .ARObject import ARObject

class DltConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .EcuInstance import EcuInstance
        from .DltLogChannel import DltLogChannel
        self._artop_dltEcuId = None
        self._artop_sessionIdSupport = None
        self._artop_timestampSupport = None
        self._artop_ecuInstance = None
        self._artop_dltLogChannel = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecuInstance':"ECU-INSTANCE", 
         '_artop_dltLogChannel':"DLT-LOG-CHANNEL"})

    @property
    def dltEcuId_(self):
        return self._artop_dltEcuId

    @property
    def sessionIdSupport_(self):
        if self._artop_sessionIdSupport:
            if self._artop_sessionIdSupport == "true":
                return True
            return False
        else:
            return self._artop_sessionIdSupport

    @property
    def timestampSupport_(self):
        if self._artop_timestampSupport:
            if self._artop_timestampSupport == "true":
                return True
            return False
        else:
            return self._artop_timestampSupport

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
    def dltLogChannels_DltLogChannel(self):
        return self._artop_dltLogChannel
