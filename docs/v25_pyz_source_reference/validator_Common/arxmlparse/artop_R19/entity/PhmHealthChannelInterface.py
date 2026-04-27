# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmHealthChannelInterface.py
from .PlatformHealthManagementInterface import PlatformHealthManagementInterface

class PhmHealthChannelInterface(PlatformHealthManagementInterface):

    def __init__(self):
        super().__init__()
        from .PhmHealthChannelStatus import PhmHealthChannelStatus
        self._artop_status = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_status": "PHM-HEALTH-CHANNEL-STATUS"})

    @property
    def status_PhmHealthChannelStatus(self):
        return self._artop_status
