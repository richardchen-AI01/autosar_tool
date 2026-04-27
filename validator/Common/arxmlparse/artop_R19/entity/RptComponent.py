# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptComponent.py
from .Identifiable import Identifiable

class RptComponent(Identifiable):

    def __init__(self):
        super().__init__()
        from .RptSupportData import RptSupportData
        from .RoleBasedMcDataAssignment import RoleBasedMcDataAssignment
        from .RptImplPolicy import RptImplPolicy
        from .RptExecutableEntity import RptExecutableEntity
        from .VariationPoint import VariationPoint
        self._artop_rptSupportData = None
        self._artop_mcDataAssignment = []
        self._artop_rpImplPolicy = None
        self._artop_rptExecutableEntity = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_rptSupportData': '"RPT-SUPPORT-DATA"', 
         '_artop_mcDataAssignment': '"ROLE-BASED-MC-DATA-ASSIGNMENT"', 
         '_artop_rpImplPolicy': '"RPT-IMPL-POLICY"', 
         '_artop_rptExecutableEntity': '"RPT-EXECUTABLE-ENTITY"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_rptSupportData_(self):
        return self._artop_rptSupportData

    @property
    def rptSupportData_(self):
        if self._artop_rptSupportData is not None:
            if hasattr(self._artop_rptSupportData, "uuid"):
                return self._artop_rptSupportData.uuid
        return

    @property
    def mcDataAssignments_RoleBasedMcDataAssignment(self):
        return self._artop_mcDataAssignment

    @property
    def ref_rpImplPolicy_(self):
        return self._artop_rpImplPolicy

    @property
    def rpImplPolicy_(self):
        if self._artop_rpImplPolicy is not None:
            if hasattr(self._artop_rpImplPolicy, "uuid"):
                return self._artop_rpImplPolicy.uuid
        return

    @property
    def rptExecutableEntities_RptExecutableEntity(self):
        return self._artop_rptExecutableEntity

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
