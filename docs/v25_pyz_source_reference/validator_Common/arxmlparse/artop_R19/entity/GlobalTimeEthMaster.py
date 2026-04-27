# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\GlobalTimeEthMaster.py
from .GlobalTimeMaster import GlobalTimeMaster

class GlobalTimeEthMaster(GlobalTimeMaster):

    def __init__(self):
        super().__init__()
        from .EthTSynSubTlvConfig import EthTSynSubTlvConfig
        self._artop_crcSecured = None
        self._artop_subTlvConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_subTlvConfig": "ETH-T-SYN-SUB-TLV-CONFIG"})

    @property
    def crcSecured_(self):
        return self._artop_crcSecured

    @property
    def ref_subTlvConfig_(self):
        return self._artop_subTlvConfig

    @property
    def subTlvConfig_(self):
        if self._artop_subTlvConfig is not None:
            if hasattr(self._artop_subTlvConfig, "uuid"):
                return self._artop_subTlvConfig.uuid
        return
