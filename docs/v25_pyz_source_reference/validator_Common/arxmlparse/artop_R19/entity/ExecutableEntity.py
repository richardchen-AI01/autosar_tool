# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExecutableEntity.py
from .Identifiable import Identifiable

class ExecutableEntity(Identifiable):

    def __init__(self):
        super().__init__()
        from .ExecutableEntityActivationReason import ExecutableEntityActivationReason
        from .ExclusiveArea import ExclusiveArea
        from .ExclusiveAreaNestingOrder import ExclusiveAreaNestingOrder
        from .SwAddrMethod import SwAddrMethod
        self._artop_minimumStartInterval = None
        self._artop_reentrancyLevel = None
        self._artop_activationReason = []
        self._artop_canEnterExclusiveAreaRef = []
        self._artop_exclusiveAreaNestingOrderRef = []
        self._artop_runsInsideExclusiveAreaRef = []
        self._artop_swAddrMethodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_activationReason': '"EXECUTABLE-ENTITY-ACTIVATION-REASON"', 
         '_artop_canEnterExclusiveAreaRef': '"EXCLUSIVE-AREA"', 
         '_artop_exclusiveAreaNestingOrderRef': '"EXCLUSIVE-AREA-NESTING-ORDER"', 
         '_artop_runsInsideExclusiveAreaRef': '"EXCLUSIVE-AREA"', 
         '_artop_swAddrMethodRef': '"SW-ADDR-METHOD"'})

    @property
    def minimumStartInterval_(self):
        return self._artop_minimumStartInterval

    @property
    def reentrancyLevel_(self):
        return self._artop_reentrancyLevel

    @property
    def activationReasons_ExecutableEntityActivationReason(self):
        return self._artop_activationReason

    @property
    def ref_canEnterExclusiveAreas_(self):
        return self._artop_canEnterExclusiveAreaRef

    @property
    def canEnterExclusiveAreas_(self):
        return self._artop_canEnterExclusiveAreaRef

    @property
    def ref_exclusiveAreaNestingOrders_(self):
        return self._artop_exclusiveAreaNestingOrderRef

    @property
    def exclusiveAreaNestingOrders_(self):
        return self._artop_exclusiveAreaNestingOrderRef

    @property
    def ref_runsInsideExclusiveAreas_(self):
        return self._artop_runsInsideExclusiveAreaRef

    @property
    def runsInsideExclusiveAreas_(self):
        return self._artop_runsInsideExclusiveAreaRef

    @property
    def ref_swAddrMethod_(self):
        return self._artop_swAddrMethodRef

    @property
    def swAddrMethod_(self):
        if self._artop_swAddrMethodRef is not None:
            if hasattr(self._artop_swAddrMethodRef, "uuid"):
                return self._artop_swAddrMethodRef.uuid
        return
