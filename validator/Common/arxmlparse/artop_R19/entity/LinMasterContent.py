# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinMasterContent.py
from .LinCommunicationControllerContent import LinCommunicationControllerContent

class LinMasterContent(LinCommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .LinSlaveConfig import LinSlaveConfig
        self._artop_timeBase = None
        self._artop_timeBaseJitter = None
        self._artop_linSlave = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_linSlave": "LIN-SLAVE-CONFIG"})

    @property
    def timeBase_(self):
        return self._artop_timeBase

    @property
    def timeBaseJitter_(self):
        return self._artop_timeBaseJitter

    @property
    def linSlaves_LinSlaveConfig(self):
        return self._artop_linSlave
