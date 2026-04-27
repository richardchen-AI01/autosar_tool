# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinSlaveConfigIdent.py
from .Referrable import Referrable

class LinSlaveConfigIdent(Referrable):

    def __init__(self):
        super().__init__()
        from .LinSlaveConfig import LinSlaveConfig
        self._artop_linSlaveConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_linSlaveConfig": "LIN-SLAVE-CONFIG"})

    @property
    def ref_linSlaveConfig_(self):
        return self._artop_linSlaveConfig

    @property
    def linSlaveConfig_(self):
        if self._artop_linSlaveConfig is not None:
            if hasattr(self._artop_linSlaveConfig, "uuid"):
                return self._artop_linSlaveConfig.uuid
        return
