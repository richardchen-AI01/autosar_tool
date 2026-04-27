# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinMaster.py
from .LinCommunicationController import LinCommunicationController

class LinMaster(LinCommunicationController):

    def __init__(self):
        super().__init__()
        from .LinMasterConditional import LinMasterConditional
        self._artop_linMasterVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_linMasterVariant": "LIN-MASTER-CONDITIONAL"})

    @property
    def LinMasterVariants_LinMasterConditional(self):
        return self._artop_linMasterVariant
