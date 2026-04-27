# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthTSynSubTlvConfig.py
from .ARObject import ARObject

class EthTSynSubTlvConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .GlobalTimeEthMaster import GlobalTimeEthMaster
        self._artop_ofsSubTlv = None
        self._artop_statusSubTlv = None
        self._artop_timeSubTlv = None
        self._artop_userDataSubTlv = None
        self._artop_globalTimeEthMaster = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_globalTimeEthMaster": "GLOBAL-TIME-ETH-MASTER"})

    @property
    def ofsSubTlv_(self):
        if self._artop_ofsSubTlv:
            if self._artop_ofsSubTlv == "true":
                return True
            return False
        else:
            return self._artop_ofsSubTlv

    @property
    def statusSubTlv_(self):
        if self._artop_statusSubTlv:
            if self._artop_statusSubTlv == "true":
                return True
            return False
        else:
            return self._artop_statusSubTlv

    @property
    def timeSubTlv_(self):
        if self._artop_timeSubTlv:
            if self._artop_timeSubTlv == "true":
                return True
            return False
        else:
            return self._artop_timeSubTlv

    @property
    def userDataSubTlv_(self):
        if self._artop_userDataSubTlv:
            if self._artop_userDataSubTlv == "true":
                return True
            return False
        else:
            return self._artop_userDataSubTlv

    @property
    def ref_globalTimeEthMaster_(self):
        return self._artop_globalTimeEthMaster

    @property
    def globalTimeEthMaster_(self):
        if self._artop_globalTimeEthMaster is not None:
            if hasattr(self._artop_globalTimeEthMaster, "uuid"):
                return self._artop_globalTimeEthMaster.uuid
        return
