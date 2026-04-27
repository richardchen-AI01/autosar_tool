# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptContainer.py
from .Identifiable import Identifiable

class RptContainer(Identifiable):

    def __init__(self):
        super().__init__()
        from .AnyInstanceRef import AnyInstanceRef
        from .RptProfile import RptProfile
        from .RptExecutableEntityProperties import RptExecutableEntityProperties
        from .RptHook import RptHook
        from .RptImplPolicy import RptImplPolicy
        from .RptSwPrototypingAccess import RptSwPrototypingAccess
        from .VariationPoint import VariationPoint
        self._artop_byPassPointIref = []
        self._artop_explicitRptProfileSelectionRef = []
        self._artop_rptContainer = []
        self._artop_rptExecutableEntityProperties = None
        self._artop_rptHook = []
        self._artop_rptImplPolicy = None
        self._artop_rptSwPrototypingAccess = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_byPassPointIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_explicitRptProfileSelectionRef': '"RPT-PROFILE"', 
         '_artop_rptContainer': '"RPT-CONTAINER"', 
         '_artop_rptExecutableEntityProperties': '"RPT-EXECUTABLE-ENTITY-PROPERTIES"', 
         '_artop_rptHook': '"RPT-HOOK"', 
         '_artop_rptImplPolicy': '"RPT-IMPL-POLICY"', 
         '_artop_rptSwPrototypingAccess': '"RPT-SW-PROTOTYPING-ACCESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def byPassPoints_AnyInstanceRef(self):
        return self._artop_byPassPointIref

    @property
    def ref_explicitRptProfileSelections_(self):
        return self._artop_explicitRptProfileSelectionRef

    @property
    def explicitRptProfileSelections_(self):
        return self._artop_explicitRptProfileSelectionRef

    @property
    def rptContainers_RptContainer(self):
        return self._artop_rptContainer

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
    def rptHooks_RptHook(self):
        return self._artop_rptHook

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
    def ref_rptSwPrototypingAccess_(self):
        return self._artop_rptSwPrototypingAccess

    @property
    def rptSwPrototypingAccess_(self):
        if self._artop_rptSwPrototypingAccess is not None:
            if hasattr(self._artop_rptSwPrototypingAccess, "uuid"):
                return self._artop_rptSwPrototypingAccess.uuid
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
