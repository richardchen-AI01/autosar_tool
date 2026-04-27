# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptExecutableEntityEvent.py
from .Identifiable import Identifiable

class RptExecutableEntityEvent(Identifiable):

    def __init__(self):
        super().__init__()
        from .RptExecutableEntity import RptExecutableEntity
        from .RptExecutionContext import RptExecutionContext
        from .RoleBasedMcDataAssignment import RoleBasedMcDataAssignment
        from .RptExecutableEntityProperties import RptExecutableEntityProperties
        from .RptImplPolicy import RptImplPolicy
        from .RptServicePoint import RptServicePoint
        from .VariationPoint import VariationPoint
        self._artop_rptEventId = None
        self._artop_rptExecutableEntity = None
        self._artop_executionContextRef = []
        self._artop_mcDataAssignment = []
        self._artop_rptExecutableEntityProperties = None
        self._artop_rptImplPolicy = None
        self._artop_rptServicePointPostRef = []
        self._artop_rptServicePointPreRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_rptExecutableEntity': '"RPT-EXECUTABLE-ENTITY"', 
         '_artop_executionContextRef': '"RPT-EXECUTION-CONTEXT"', 
         '_artop_mcDataAssignment': '"ROLE-BASED-MC-DATA-ASSIGNMENT"', 
         '_artop_rptExecutableEntityProperties': '"RPT-EXECUTABLE-ENTITY-PROPERTIES"', 
         '_artop_rptImplPolicy': '"RPT-IMPL-POLICY"', 
         '_artop_rptServicePointPostRef': '"RPT-SERVICE-POINT"', 
         '_artop_rptServicePointPreRef': '"RPT-SERVICE-POINT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def rptEventId_(self):
        return self._artop_rptEventId

    @property
    def ref_rptExecutableEntity_(self):
        return self._artop_rptExecutableEntity

    @property
    def rptExecutableEntity_(self):
        if self._artop_rptExecutableEntity is not None:
            if hasattr(self._artop_rptExecutableEntity, "uuid"):
                return self._artop_rptExecutableEntity.uuid
        return

    @property
    def ref_executionContexts_(self):
        return self._artop_executionContextRef

    @property
    def executionContexts_(self):
        return self._artop_executionContextRef

    @property
    def mcDataAssignments_RoleBasedMcDataAssignment(self):
        return self._artop_mcDataAssignment

    @property
    def ref_rptExecutableEntityProperties_(self):
        return self._artop_rptExecutableEntityProperties

    @property
    def rptExecutableEntityProperties_(self):
        if self._artop_rptExecutableEntityProperties is not None:
            if hasattr(self._artop_rptExecutableEntityProperties, "uuid"):
                return self._artop_rptExecutableEntityProperties.uuid
        return

    @property
    def ref_rptImplPolicy_(self):
        return self._artop_rptImplPolicy

    @property
    def rptImplPolicy_(self):
        if self._artop_rptImplPolicy is not None:
            if hasattr(self._artop_rptImplPolicy, "uuid"):
                return self._artop_rptImplPolicy.uuid
        return

    @property
    def ref_rptServicePointPosts_(self):
        return self._artop_rptServicePointPostRef

    @property
    def rptServicePointPosts_(self):
        return self._artop_rptServicePointPostRef

    @property
    def ref_rptServicePointPres_(self):
        return self._artop_rptServicePointPreRef

    @property
    def rptServicePointPres_(self):
        return self._artop_rptServicePointPreRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
