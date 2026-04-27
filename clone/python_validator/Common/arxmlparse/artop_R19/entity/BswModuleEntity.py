# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleEntity.py
from .ExecutableEntity import ExecutableEntity

class BswModuleEntity(ExecutableEntity):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .ModeDeclarationGroupPrototypeRefConditional import ModeDeclarationGroupPrototypeRefConditional
        from .BswInternalTriggeringPointRefConditional import BswInternalTriggeringPointRefConditional
        from .BswModuleCallPoint import BswModuleCallPoint
        from .BswModuleEntryRefConditional import BswModuleEntryRefConditional
        from .BswVariableAccess import BswVariableAccess
        from .BswModuleEntry import BswModuleEntry
        from .TriggerRefConditional import TriggerRefConditional
        from .BswSchedulerNamePrefix import BswSchedulerNamePrefix
        from .VariationPoint import VariationPoint
        self._artop_bswInternalBehavior = None
        self._artop_accessedModeGroup = []
        self._artop_activationPoint = []
        self._artop_callPoint = []
        self._artop_calledEntry = []
        self._artop_dataReceivePoint = []
        self._artop_dataSendPoint = []
        self._artop_implementedEntryRef = None
        self._artop_issuedTrigger = []
        self._artop_managedModeGroup = []
        self._artop_schedulerNamePrefixRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswInternalBehavior': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_accessedModeGroup': '"MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"', 
         '_artop_activationPoint': '"BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL"', 
         '_artop_callPoint': '"BSW-MODULE-CALL-POINT"', 
         '_artop_calledEntry': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_dataReceivePoint': '"BSW-VARIABLE-ACCESS"', 
         '_artop_dataSendPoint': '"BSW-VARIABLE-ACCESS"', 
         '_artop_implementedEntryRef': '"BSW-MODULE-ENTRY"', 
         '_artop_issuedTrigger': '"TRIGGER-REF-CONDITIONAL"', 
         '_artop_managedModeGroup': '"MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"', 
         '_artop_schedulerNamePrefixRef': '"BSW-SCHEDULER-NAME-PREFIX"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_bswInternalBehavior_(self):
        return self._artop_bswInternalBehavior

    @property
    def bswInternalBehavior_(self):
        if self._artop_bswInternalBehavior is not None:
            if hasattr(self._artop_bswInternalBehavior, "uuid"):
                return self._artop_bswInternalBehavior.uuid
        return

    @property
    def accessedModeGroups_ModeDeclarationGroupPrototypeRefConditional(self):
        return self._artop_accessedModeGroup

    @property
    def activationPoints_BswInternalTriggeringPointRefConditional(self):
        return self._artop_activationPoint

    @property
    def callPoints_BswModuleCallPoint(self):
        return self._artop_callPoint

    @property
    def calledEntries_BswModuleEntryRefConditional(self):
        return self._artop_calledEntry

    @property
    def dataReceivePoints_BswVariableAccess(self):
        return self._artop_dataReceivePoint

    @property
    def dataSendPoints_BswVariableAccess(self):
        return self._artop_dataSendPoint

    @property
    def ref_implementedEntry_(self):
        return self._artop_implementedEntryRef

    @property
    def implementedEntry_(self):
        if self._artop_implementedEntryRef is not None:
            if hasattr(self._artop_implementedEntryRef, "uuid"):
                return self._artop_implementedEntryRef.uuid
        return

    @property
    def issuedTriggers_TriggerRefConditional(self):
        return self._artop_issuedTrigger

    @property
    def managedModeGroups_ModeDeclarationGroupPrototypeRefConditional(self):
        return self._artop_managedModeGroup

    @property
    def ref_schedulerNamePrefix_(self):
        return self._artop_schedulerNamePrefixRef

    @property
    def schedulerNamePrefix_(self):
        if self._artop_schedulerNamePrefixRef is not None:
            if hasattr(self._artop_schedulerNamePrefixRef, "uuid"):
                return self._artop_schedulerNamePrefixRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
