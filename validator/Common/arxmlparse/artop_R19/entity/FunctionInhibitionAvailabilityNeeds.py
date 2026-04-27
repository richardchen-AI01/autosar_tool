# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FunctionInhibitionAvailabilityNeeds.py
from .ServiceNeeds import ServiceNeeds

class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):

    def __init__(self):
        super().__init__()
        from .FunctionInhibitionNeeds import FunctionInhibitionNeeds
        self._artop_controlledFidRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_controlledFidRef": "FUNCTION-INHIBITION-NEEDS"})

    @property
    def ref_controlledFid_(self):
        return self._artop_controlledFidRef

    @property
    def controlledFid_(self):
        if self._artop_controlledFidRef is not None:
            if hasattr(self._artop_controlledFidRef, "uuid"):
                return self._artop_controlledFidRef.uuid
        return
