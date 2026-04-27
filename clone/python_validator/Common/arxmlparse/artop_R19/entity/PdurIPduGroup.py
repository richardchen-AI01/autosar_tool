# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PdurIPduGroup.py
from .FibexElement import FibexElement

class PdurIPduGroup(FibexElement):

    def __init__(self):
        super().__init__()
        from .PduTriggeringRefConditional import PduTriggeringRefConditional
        self._artop_communicationMode = None
        self._artop_iPdu = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_iPdu": "PDU-TRIGGERING-REF-CONDITIONAL"})

    @property
    def communicationMode_(self):
        return self._artop_communicationMode

    @property
    def iPdus_PduTriggeringRefConditional(self):
        return self._artop_iPdu
