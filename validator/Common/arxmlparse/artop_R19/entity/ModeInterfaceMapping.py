# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeInterfaceMapping.py
from .PortInterfaceMapping import PortInterfaceMapping

class ModeInterfaceMapping(PortInterfaceMapping):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroupPrototypeMapping import ModeDeclarationGroupPrototypeMapping
        self._artop_modeMapping = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeMapping": "MODE-DECLARATION-GROUP-PROTOTYPE-MAPPING"})

    @property
    def ref_modeMapping_(self):
        return self._artop_modeMapping

    @property
    def modeMapping_(self):
        if self._artop_modeMapping is not None:
            if hasattr(self._artop_modeMapping, "uuid"):
                return self._artop_modeMapping.uuid
        return
