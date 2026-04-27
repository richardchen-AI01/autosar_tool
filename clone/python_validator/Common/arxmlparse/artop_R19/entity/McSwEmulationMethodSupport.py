# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\McSwEmulationMethodSupport.py
from .ARObject import ARObject

class McSwEmulationMethodSupport(ARObject):

    def __init__(self):
        super().__init__()
        from .McSupportData import McSupportData
        from .VariableDataPrototype import VariableDataPrototype
        from .McParameterElementGroup import McParameterElementGroup
        from .VariationPoint import VariationPoint
        self._artop_shortLabel = None
        self._artop_category = None
        self._artop_mcSupportData = None
        self._artop_baseReferenceRef = None
        self._artop_elementGroup = []
        self._artop_referenceTableRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_mcSupportData': '"MC-SUPPORT-DATA"', 
         '_artop_baseReferenceRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_elementGroup': '"MC-PARAMETER-ELEMENT-GROUP"', 
         '_artop_referenceTableRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def category_(self):
        return self._artop_category

    @property
    def ref_mcSupportData_(self):
        return self._artop_mcSupportData

    @property
    def mcSupportData_(self):
        if self._artop_mcSupportData is not None:
            if hasattr(self._artop_mcSupportData, "uuid"):
                return self._artop_mcSupportData.uuid
        return

    @property
    def ref_baseReference_(self):
        return self._artop_baseReferenceRef

    @property
    def baseReference_(self):
        if self._artop_baseReferenceRef is not None:
            if hasattr(self._artop_baseReferenceRef, "uuid"):
                return self._artop_baseReferenceRef.uuid
        return

    @property
    def elementGroups_McParameterElementGroup(self):
        return self._artop_elementGroup

    @property
    def ref_referenceTable_(self):
        return self._artop_referenceTableRef

    @property
    def referenceTable_(self):
        if self._artop_referenceTableRef is not None:
            if hasattr(self._artop_referenceTableRef, "uuid"):
                return self._artop_referenceTableRef.uuid
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
