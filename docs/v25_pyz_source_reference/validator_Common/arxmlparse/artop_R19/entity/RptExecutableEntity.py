# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptExecutableEntity.py
from .Identifiable import Identifiable

class RptExecutableEntity(Identifiable):

    def __init__(self):
        super().__init__()
        from .RptComponent import RptComponent
        from .RptExecutableEntityEvent import RptExecutableEntityEvent
        from .RoleBasedMcDataAssignment import RoleBasedMcDataAssignment
        from .VariationPoint import VariationPoint
        self._artop_symbol = None
        self._artop_rptComponent = None
        self._artop_rptExecutableEntityEvent = []
        self._artop_rptRead = []
        self._artop_rptWrite = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_rptComponent': '"RPT-COMPONENT"', 
         '_artop_rptExecutableEntityEvent': '"RPT-EXECUTABLE-ENTITY-EVENT"', 
         '_artop_rptRead': '"ROLE-BASED-MC-DATA-ASSIGNMENT"', 
         '_artop_rptWrite': '"ROLE-BASED-MC-DATA-ASSIGNMENT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def ref_rptComponent_(self):
        return self._artop_rptComponent

    @property
    def rptComponent_(self):
        if self._artop_rptComponent is not None:
            if hasattr(self._artop_rptComponent, "uuid"):
                return self._artop_rptComponent.uuid
        return

    @property
    def rptExecutableEntityEvents_RptExecutableEntityEvent(self):
        return self._artop_rptExecutableEntityEvent

    @property
    def rptReads_RoleBasedMcDataAssignment(self):
        return self._artop_rptRead

    @property
    def rptWrites_RoleBasedMcDataAssignment(self):
        return self._artop_rptWrite

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
