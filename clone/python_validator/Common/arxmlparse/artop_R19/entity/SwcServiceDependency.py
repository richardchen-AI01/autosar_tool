# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcServiceDependency.py
from .ServiceDependency import ServiceDependency
from .AtpStructureElement import AtpStructureElement

class SwcServiceDependency(AtpStructureElement, ServiceDependency):

    def __init__(self):
        super().__init__()
        from .RoleBasedDataAssignment import RoleBasedDataAssignment
        from .RoleBasedPortAssignment import RoleBasedPortAssignment
        from .PortGroup import PortGroup
        from .ServiceNeeds import ServiceNeeds
        from .VariationPoint import VariationPoint
        self._artop_assignedData = []
        self._artop_assignedPort = []
        self._artop_representedPortGroupRef = None
        self._artop_serviceNeeds = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_assignedData': '"ROLE-BASED-DATA-ASSIGNMENT"', 
         '_artop_assignedPort': '"ROLE-BASED-PORT-ASSIGNMENT"', 
         '_artop_representedPortGroupRef': '"PORT-GROUP"', 
         '_artop_serviceNeeds': '"SERVICE-NEEDS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def assignedDatas_RoleBasedDataAssignment(self):
        return self._artop_assignedData

    @property
    def assignedPorts_RoleBasedPortAssignment(self):
        return self._artop_assignedPort

    @property
    def ref_representedPortGroup_(self):
        return self._artop_representedPortGroupRef

    @property
    def representedPortGroup_(self):
        if self._artop_representedPortGroupRef is not None:
            if hasattr(self._artop_representedPortGroupRef, "uuid"):
                return self._artop_representedPortGroupRef.uuid
        return

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
