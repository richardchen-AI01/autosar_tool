# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeSwitchReceiverComSpec.py
from .RPortComSpec import RPortComSpec

class ModeSwitchReceiverComSpec(RPortComSpec):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        self._artop_enhancedModeApi = None
        self._artop_supportsAsynchronousModeSwitch = None
        self._artop_modeGroupRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeGroupRef": "MODE-DECLARATION-GROUP-PROTOTYPE"})

    @property
    def enhancedModeApi_(self):
        if self._artop_enhancedModeApi:
            if self._artop_enhancedModeApi == "true":
                return True
            return False
        else:
            return self._artop_enhancedModeApi

    @property
    def supportsAsynchronousModeSwitch_(self):
        if self._artop_supportsAsynchronousModeSwitch:
            if self._artop_supportsAsynchronousModeSwitch == "true":
                return True
            return False
        else:
            return self._artop_supportsAsynchronousModeSwitch

    @property
    def ref_modeGroup_(self):
        return self._artop_modeGroupRef

    @property
    def modeGroup_(self):
        if self._artop_modeGroupRef is not None:
            if hasattr(self._artop_modeGroupRef, "uuid"):
                return self._artop_modeGroupRef.uuid
        return
