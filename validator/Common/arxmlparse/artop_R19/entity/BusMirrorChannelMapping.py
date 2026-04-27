# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BusMirrorChannelMapping.py
from .FibexElement import FibexElement

class BusMirrorChannelMapping(FibexElement):

    def __init__(self):
        super().__init__()
        from .BusMirrorChannel import BusMirrorChannel
        from .PduTriggeringRefConditional import PduTriggeringRefConditional
        self._artop_sourceChannel = None
        self._artop_targetChannel = None
        self._artop_targetPduTriggering = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sourceChannel':"BUS-MIRROR-CHANNEL", 
         '_artop_targetChannel':"BUS-MIRROR-CHANNEL", 
         '_artop_targetPduTriggering':"PDU-TRIGGERING-REF-CONDITIONAL"})

    @property
    def ref_sourceChannel_(self):
        return self._artop_sourceChannel

    @property
    def sourceChannel_(self):
        if self._artop_sourceChannel is not None:
            if hasattr(self._artop_sourceChannel, "uuid"):
                return self._artop_sourceChannel.uuid
        return

    @property
    def ref_targetChannel_(self):
        return self._artop_targetChannel

    @property
    def targetChannel_(self):
        if self._artop_targetChannel is not None:
            if hasattr(self._artop_targetChannel, "uuid"):
                return self._artop_targetChannel.uuid
        return

    @property
    def targetPduTriggerings_PduTriggeringRefConditional(self):
        return self._artop_targetPduTriggering
