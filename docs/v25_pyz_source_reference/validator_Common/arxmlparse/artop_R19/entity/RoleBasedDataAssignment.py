# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RoleBasedDataAssignment.py
from .ARObject import ARObject

class RoleBasedDataAssignment(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarVariableRef import AutosarVariableRef
        from .AutosarParameterRef import AutosarParameterRef
        from .PerInstanceMemory import PerInstanceMemory
        from .VariationPoint import VariationPoint
        self._artop_role = None
        self._artop_usedDataElement = None
        self._artop_usedParameterElement = None
        self._artop_usedPimRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_usedDataElement': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_usedParameterElement': '"AUTOSAR-PARAMETER-REF"', 
         '_artop_usedPimRef': '"PER-INSTANCE-MEMORY"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_usedDataElement_(self):
        return self._artop_usedDataElement

    @property
    def usedDataElement_(self):
        if self._artop_usedDataElement is not None:
            if hasattr(self._artop_usedDataElement, "uuid"):
                return self._artop_usedDataElement.uuid
        return

    @property
    def ref_usedParameterElement_(self):
        return self._artop_usedParameterElement

    @property
    def usedParameterElement_(self):
        if self._artop_usedParameterElement is not None:
            if hasattr(self._artop_usedParameterElement, "uuid"):
                return self._artop_usedParameterElement.uuid
        return

    @property
    def ref_usedPim_(self):
        return self._artop_usedPimRef

    @property
    def usedPim_(self):
        if self._artop_usedPimRef is not None:
            if hasattr(self._artop_usedPimRef, "uuid"):
                return self._artop_usedPimRef.uuid
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
