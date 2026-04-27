# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeSwitchSenderComSpec.py
from .PPortComSpec import PPortComSpec

class ModeSwitchSenderComSpec(PPortComSpec):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeSwitchedAckRequest import ModeSwitchedAckRequest
        self._artop_enhancedModeApi = None
        self._artop_queueLength = None
        self._artop_modeGroupRef = None
        self._artop_modeSwitchedAck = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_modeGroupRef':"MODE-DECLARATION-GROUP-PROTOTYPE", 
         '_artop_modeSwitchedAck':"MODE-SWITCHED-ACK-REQUEST"})

    @property
    def enhancedModeApi_(self):
        if self._artop_enhancedModeApi:
            if self._artop_enhancedModeApi == "true":
                return True
            return False
        else:
            return self._artop_enhancedModeApi

    @property
    def queueLength_(self):
        return self._artop_queueLength

    @property
    def ref_modeGroup_(self):
        return self._artop_modeGroupRef

    @property
    def modeGroup_(self):
        if self._artop_modeGroupRef is not None:
            if hasattr(self._artop_modeGroupRef, "uuid"):
                return self._artop_modeGroupRef.uuid
        return

    @property
    def ref_modeSwitchedAck_(self):
        return self._artop_modeSwitchedAck

    @property
    def modeSwitchedAck_(self):
        if self._artop_modeSwitchedAck is not None:
            if hasattr(self._artop_modeSwitchedAck, "uuid"):
                return self._artop_modeSwitchedAck.uuid
        return
