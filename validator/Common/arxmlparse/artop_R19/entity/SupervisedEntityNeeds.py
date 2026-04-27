# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SupervisedEntityNeeds.py
from .ServiceNeeds import ServiceNeeds

class SupervisedEntityNeeds(ServiceNeeds):

    def __init__(self):
        super().__init__()
        from .SupervisedEntityCheckpointNeedsRefConditional import SupervisedEntityCheckpointNeedsRefConditional
        self._artop_activateAtStart = None
        self._artop_enableDeactivation = None
        self._artop_expectedAliveCycle = None
        self._artop_maxAliveCycle = None
        self._artop_minAliveCycle = None
        self._artop_toleratedFailedCycles = None
        self._artop_checkpoints = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_checkpoints": "SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL"})

    @property
    def activateAtStart_(self):
        if self._artop_activateAtStart:
            if self._artop_activateAtStart == "true":
                return True
            return False
        else:
            return self._artop_activateAtStart

    @property
    def enableDeactivation_(self):
        if self._artop_enableDeactivation:
            if self._artop_enableDeactivation == "true":
                return True
            return False
        else:
            return self._artop_enableDeactivation

    @property
    def expectedAliveCycle_(self):
        return self._artop_expectedAliveCycle

    @property
    def maxAliveCycle_(self):
        return self._artop_maxAliveCycle

    @property
    def minAliveCycle_(self):
        return self._artop_minAliveCycle

    @property
    def toleratedFailedCycles_(self):
        return self._artop_toleratedFailedCycles

    @property
    def checkpoints_SupervisedEntityCheckpointNeedsRefConditional(self):
        return self._artop_checkpoints
