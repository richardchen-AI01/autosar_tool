# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McDataInstance.py
from .Identifiable import Identifiable

class McDataInstance(Identifiable):

    def __init__(self):
        super().__init__()
        from .FlatInstanceDescriptor import FlatInstanceDescriptor
        from .ImplementationElementInParameterInstanceRef import ImplementationElementInParameterInstanceRef
        from .McDataAccessDetails import McDataAccessDetails
        from .RoleBasedMcDataAssignment import RoleBasedMcDataAssignment
        from .SwDataDefProps import SwDataDefProps
        from .RptSwPrototypingAccess import RptSwPrototypingAccess
        from .RptImplPolicy import RptImplPolicy
        from .VariationPoint import VariationPoint
        self._artop_arraySize = None
        self._artop_displayIdentifier = None
        self._artop_role = None
        self._artop_symbol = None
        self._artop_flatMapEntryRef = None
        self._artop_instanceInMemory = None
        self._artop_mcDataAccessDetails = None
        self._artop_mcDataAssignment = []
        self._artop_resultingProperties = None
        self._artop_resultingRptSwPrototypingAccess = None
        self._artop_rptImplPolicy = None
        self._artop_subElement = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flatMapEntryRef': '"FLAT-INSTANCE-DESCRIPTOR"', 
         '_artop_instanceInMemory': '"IMPLEMENTATION-ELEMENT-IN-PARAMETER-INSTANCE-REF"', 
         '_artop_mcDataAccessDetails': '"MC-DATA-ACCESS-DETAILS"', 
         '_artop_mcDataAssignment': '"ROLE-BASED-MC-DATA-ASSIGNMENT"', 
         '_artop_resultingProperties': '"SW-DATA-DEF-PROPS"', 
         '_artop_resultingRptSwPrototypingAccess': '"RPT-SW-PROTOTYPING-ACCESS"', 
         '_artop_rptImplPolicy': '"RPT-IMPL-POLICY"', 
         '_artop_subElement': '"MC-DATA-INSTANCE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def arraySize_(self):
        return self._artop_arraySize

    @property
    def displayIdentifier_(self):
        return self._artop_displayIdentifier

    @property
    def role_(self):
        return self._artop_role

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def ref_flatMapEntry_(self):
        return self._artop_flatMapEntryRef

    @property
    def flatMapEntry_(self):
        if self._artop_flatMapEntryRef is not None:
            if hasattr(self._artop_flatMapEntryRef, "uuid"):
                return self._artop_flatMapEntryRef.uuid
        return

    @property
    def ref_instanceInMemory_(self):
        return self._artop_instanceInMemory

    @property
    def instanceInMemory_(self):
        if self._artop_instanceInMemory is not None:
            if hasattr(self._artop_instanceInMemory, "uuid"):
                return self._artop_instanceInMemory.uuid
        return

    @property
    def ref_mcDataAccessDetails_(self):
        return self._artop_mcDataAccessDetails

    @property
    def mcDataAccessDetails_(self):
        if self._artop_mcDataAccessDetails is not None:
            if hasattr(self._artop_mcDataAccessDetails, "uuid"):
                return self._artop_mcDataAccessDetails.uuid
        return

    @property
    def mcDataAssignments_RoleBasedMcDataAssignment(self):
        return self._artop_mcDataAssignment

    @property
    def ref_resultingProperties_(self):
        return self._artop_resultingProperties

    @property
    def resultingProperties_(self):
        if self._artop_resultingProperties is not None:
            if hasattr(self._artop_resultingProperties, "uuid"):
                return self._artop_resultingProperties.uuid
        return

    @property
    def ref_resultingRptSwPrototypingAccess_(self):
        return self._artop_resultingRptSwPrototypingAccess

    @property
    def resultingRptSwPrototypingAccess_(self):
        if self._artop_resultingRptSwPrototypingAccess is not None:
            if hasattr(self._artop_resultingRptSwPrototypingAccess, "uuid"):
                return self._artop_resultingRptSwPrototypingAccess.uuid
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
    def subElements_McDataInstance(self):
        return self._artop_subElement

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
