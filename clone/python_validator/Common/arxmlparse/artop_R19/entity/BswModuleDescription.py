# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleDescription.py
from .AtpStructureElement import AtpStructureElement
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class BswModuleDescription(ARElement, AtpBlueprint, AtpBlueprintable, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .BswModuleEntryRefConditional import BswModuleEntryRefConditional
        from .SwComponentDocumentation import SwComponentDocumentation
        from .BswModuleDependency import BswModuleDependency
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .Trigger import Trigger
        from .BswModuleClientServerEntry import BswModuleClientServerEntry
        from .VariableDataPrototype import VariableDataPrototype
        from .BswInternalBehavior import BswInternalBehavior
        self._artop_moduleId = None
        self._artop_expectedEntry = []
        self._artop_implementedEntry = []
        self._artop_bswModuleDocumentation = []
        self._artop_providedEntry = []
        self._artop_outgoingCallback = []
        self._artop_bswModuleDependency = []
        self._artop_providedModeGroup = []
        self._artop_requiredModeGroup = []
        self._artop_releasedTrigger = []
        self._artop_requiredTrigger = []
        self._artop_providedClientServerEntry = []
        self._artop_requiredClientServerEntry = []
        self._artop_providedData = []
        self._artop_requiredData = []
        self._artop_internalBehavior = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_expectedEntry': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_implementedEntry': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_bswModuleDocumentation': '"SW-COMPONENT-DOCUMENTATION"', 
         '_artop_providedEntry': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_outgoingCallback': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_bswModuleDependency': '"BSW-MODULE-DEPENDENCY"', 
         '_artop_providedModeGroup': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_requiredModeGroup': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_releasedTrigger': '"TRIGGER"', 
         '_artop_requiredTrigger': '"TRIGGER"', 
         '_artop_providedClientServerEntry': '"BSW-MODULE-CLIENT-SERVER-ENTRY"', 
         '_artop_requiredClientServerEntry': '"BSW-MODULE-CLIENT-SERVER-ENTRY"', 
         '_artop_providedData': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_requiredData': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_internalBehavior': '"BSW-INTERNAL-BEHAVIOR"'})

    @property
    def moduleId_(self):
        return self._artop_moduleId

    @property
    def expectedEntries_BswModuleEntryRefConditional(self):
        return self._artop_expectedEntry

    @property
    def implementedEntries_BswModuleEntryRefConditional(self):
        return self._artop_implementedEntry

    @property
    def bswModuleDocumentations_SwComponentDocumentation(self):
        return self._artop_bswModuleDocumentation

    @property
    def providedEntries_BswModuleEntryRefConditional(self):
        return self._artop_providedEntry

    @property
    def outgoingCallbacks_BswModuleEntryRefConditional(self):
        return self._artop_outgoingCallback

    @property
    def bswModuleDependencies_BswModuleDependency(self):
        return self._artop_bswModuleDependency

    @property
    def providedModeGroups_ModeDeclarationGroupPrototype(self):
        return self._artop_providedModeGroup

    @property
    def requiredModeGroups_ModeDeclarationGroupPrototype(self):
        return self._artop_requiredModeGroup

    @property
    def releasedTriggers_Trigger(self):
        return self._artop_releasedTrigger

    @property
    def requiredTriggers_Trigger(self):
        return self._artop_requiredTrigger

    @property
    def providedClientServerEntries_BswModuleClientServerEntry(self):
        return self._artop_providedClientServerEntry

    @property
    def requiredClientServerEntries_BswModuleClientServerEntry(self):
        return self._artop_requiredClientServerEntry

    @property
    def providedDatas_VariableDataPrototype(self):
        return self._artop_providedData

    @property
    def requiredDatas_VariableDataPrototype(self):
        return self._artop_requiredData

    @property
    def internalBehaviors_BswInternalBehavior(self):
        return self._artop_internalBehavior
