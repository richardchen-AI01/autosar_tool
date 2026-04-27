# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeSwitchInterface.py
from .PortInterface import PortInterface

class ModeSwitchInterface(PortInterface):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        self._artop_modeGroup = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeGroup": "MODE-DECLARATION-GROUP-PROTOTYPE"})

    @property
    def ref_modeGroup_(self):
        return self._artop_modeGroup

    @property
    def modeGroup_(self):
        if self._artop_modeGroup is not None:
            if hasattr(self._artop_modeGroup, "uuid"):
                return self._artop_modeGroup.uuid
        return
