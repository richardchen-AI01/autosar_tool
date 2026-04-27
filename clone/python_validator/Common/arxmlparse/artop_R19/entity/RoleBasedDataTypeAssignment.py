# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RoleBasedDataTypeAssignment.py
from .ARObject import ARObject

class RoleBasedDataTypeAssignment(ARObject):

    def __init__(self):
        super().__init__()
        from .ServiceDependency import ServiceDependency
        from .ImplementationDataType import ImplementationDataType
        from .VariationPoint import VariationPoint
        self._artop_role = None
        self._artop_serviceDependency = None
        self._artop_usedImplementationDataTypeRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_serviceDependency':"SERVICE-DEPENDENCY", 
         '_artop_usedImplementationDataTypeRef':"IMPLEMENTATION-DATA-TYPE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_serviceDependency_(self):
        return self._artop_serviceDependency

    @property
    def serviceDependency_(self):
        if self._artop_serviceDependency is not None:
            if hasattr(self._artop_serviceDependency, "uuid"):
                return self._artop_serviceDependency.uuid
        return

    @property
    def ref_usedImplementationDataType_(self):
        return self._artop_usedImplementationDataTypeRef

    @property
    def usedImplementationDataType_(self):
        if self._artop_usedImplementationDataTypeRef is not None:
            if hasattr(self._artop_usedImplementationDataTypeRef, "uuid"):
                return self._artop_usedImplementationDataTypeRef.uuid
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
