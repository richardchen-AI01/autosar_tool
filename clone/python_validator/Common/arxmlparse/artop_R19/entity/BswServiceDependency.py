# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswServiceDependency.py
from .ServiceDependency import ServiceDependency

class BswServiceDependency(ServiceDependency):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .BswServiceDependencyIdent import BswServiceDependencyIdent
        from .RoleBasedDataAssignment import RoleBasedDataAssignment
        from .RoleBasedBswModuleEntryAssignment import RoleBasedBswModuleEntryAssignment
        from .ServiceNeeds import ServiceNeeds
        from .VariationPoint import VariationPoint
        self._artop_bswInternalBehavior = None
        self._artop_ident = None
        self._artop_assignedData = []
        self._artop_assignedEntryRole = []
        self._artop_serviceNeeds = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswInternalBehavior': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_ident': '"BSW-SERVICE-DEPENDENCY-IDENT"', 
         '_artop_assignedData': '"ROLE-BASED-DATA-ASSIGNMENT"', 
         '_artop_assignedEntryRole': '"ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT"', 
         '_artop_serviceNeeds': '"SERVICE-NEEDS"', 
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
    def ref_ident_(self):
        return self._artop_ident

    @property
    def ident_(self):
        if self._artop_ident is not None:
            if hasattr(self._artop_ident, "uuid"):
                return self._artop_ident.uuid
        return

    @property
    def assignedDatas_RoleBasedDataAssignment(self):
        return self._artop_assignedData

    @property
    def assignedEntryRoles_RoleBasedBswModuleEntryAssignment(self):
        return self._artop_assignedEntryRole

    @property
    def ref_serviceNeeds_(self):
        return self._artop_serviceNeeds

    @property
    def serviceNeeds_(self):
        if self._artop_serviceNeeds is not None:
            if hasattr(self._artop_serviceNeeds, "uuid"):
                return self._artop_serviceNeeds.uuid
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
