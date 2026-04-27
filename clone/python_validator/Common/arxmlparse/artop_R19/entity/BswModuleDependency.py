# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleDependency.py
from .Identifiable import Identifiable

class BswModuleDependency(Identifiable):

    def __init__(self):
        super().__init__()
        from .BswModuleDescription import BswModuleDescription
        from .BswModuleDescriptionRefConditional import BswModuleDescriptionRefConditional
        from .BswModuleEntryRefConditional import BswModuleEntryRefConditional
        from .ServiceNeeds import ServiceNeeds
        from .VariationPoint import VariationPoint
        self._artop_targetModuleId = None
        self._artop_bswModuleDescription = None
        self._artop_targetModuleRef = []
        self._artop_requiredEntry = []
        self._artop_expectedCallback = []
        self._artop_serviceItem = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswModuleDescription': '"BSW-MODULE-DESCRIPTION"', 
         '_artop_targetModuleRef': '"BSW-MODULE-DESCRIPTION-REF-CONDITIONAL"', 
         '_artop_requiredEntry': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_expectedCallback': '"BSW-MODULE-ENTRY-REF-CONDITIONAL"', 
         '_artop_serviceItem': '"SERVICE-NEEDS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def targetModuleId_(self):
        return self._artop_targetModuleId

    @property
    def ref_bswModuleDescription_(self):
        return self._artop_bswModuleDescription

    @property
    def bswModuleDescription_(self):
        if self._artop_bswModuleDescription is not None:
            if hasattr(self._artop_bswModuleDescription, "uuid"):
                return self._artop_bswModuleDescription.uuid
        return

    @property
    def targetModuleRefs_BswModuleDescriptionRefConditional(self):
        return self._artop_targetModuleRef

    @property
    def requiredEntries_BswModuleEntryRefConditional(self):
        return self._artop_requiredEntry

    @property
    def expectedCallbacks_BswModuleEntryRefConditional(self):
        return self._artop_expectedCallback

    @property
    def serviceItems_ServiceNeeds(self):
        return self._artop_serviceItem

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
