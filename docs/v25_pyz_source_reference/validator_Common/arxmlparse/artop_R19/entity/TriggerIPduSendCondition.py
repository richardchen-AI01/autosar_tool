# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TriggerIPduSendCondition.py
from .ARObject import ARObject

class TriggerIPduSendCondition(ARObject):

    def __init__(self):
        super().__init__()
        from .PduTriggering import PduTriggering
        from .ModeDeclaration import ModeDeclaration
        self._artop_pduTriggering = None
        self._artop_modeDeclarationRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_pduTriggering':"PDU-TRIGGERING", 
         '_artop_modeDeclarationRef':"MODE-DECLARATION"})

    @property
    def ref_pduTriggering_(self):
        return self._artop_pduTriggering

    @property
    def pduTriggering_(self):
        if self._artop_pduTriggering is not None:
            if hasattr(self._artop_pduTriggering, "uuid"):
                return self._artop_pduTriggering.uuid
        return

    @property
    def ref_modeDeclarations_(self):
        return self._artop_modeDeclarationRef

    @property
    def modeDeclarations_(self):
        return self._artop_modeDeclarationRef
