# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\StructuredReq.py
from .Traceable import Traceable
from .Paginateable import Paginateable
from .Identifiable import Identifiable

class StructuredReq(Identifiable, Paginateable, Traceable):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .Traceable import Traceable
        from .VariationPoint import VariationPoint
        self._artop_date = None
        self._artop_issuedBy = None
        self._artop_type = None
        self._artop_importance = None
        self._artop_appliesTo = None
        self._artop_documentationBlock = None
        self._artop_description = None
        self._artop_rationale = None
        self._artop_dependencies = None
        self._artop_useCase = None
        self._artop_conflicts = None
        self._artop_supportingMaterial = None
        self._artop_remark = None
        self._artop_testedItemRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_documentationBlock': '"DOCUMENTATION-BLOCK"', 
         '_artop_description': '"DOCUMENTATION-BLOCK"', 
         '_artop_rationale': '"DOCUMENTATION-BLOCK"', 
         '_artop_dependencies': '"DOCUMENTATION-BLOCK"', 
         '_artop_useCase': '"DOCUMENTATION-BLOCK"', 
         '_artop_conflicts': '"DOCUMENTATION-BLOCK"', 
         '_artop_supportingMaterial': '"DOCUMENTATION-BLOCK"', 
         '_artop_remark': '"DOCUMENTATION-BLOCK"', 
         '_artop_testedItemRef': '"TRACEABLE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def date_(self):
        return self._artop_date

    @property
    def issuedBy_(self):
        return self._artop_issuedBy

    @property
    def type_(self):
        return self._artop_type

    @property
    def importance_(self):
        return self._artop_importance

    @property
    def appliesTo_(self):
        return self._artop_appliesTo

    @property
    def ref_documentationBlock_(self):
        return self._artop_documentationBlock

    @property
    def documentationBlock_(self):
        if self._artop_documentationBlock is not None:
            if hasattr(self._artop_documentationBlock, "uuid"):
                return self._artop_documentationBlock.uuid
        return

    @property
    def ref_description_(self):
        return self._artop_description

    @property
    def description_(self):
        if self._artop_description is not None:
            if hasattr(self._artop_description, "uuid"):
                return self._artop_description.uuid
        return

    @property
    def ref_rationale_(self):
        return self._artop_rationale

    @property
    def rationale_(self):
        if self._artop_rationale is not None:
            if hasattr(self._artop_rationale, "uuid"):
                return self._artop_rationale.uuid
        return

    @property
    def ref_dependencies_(self):
        return self._artop_dependencies

    @property
    def dependencies_(self):
        if self._artop_dependencies is not None:
            if hasattr(self._artop_dependencies, "uuid"):
                return self._artop_dependencies.uuid
        return

    @property
    def ref_useCase_(self):
        return self._artop_useCase

    @property
    def useCase_(self):
        if self._artop_useCase is not None:
            if hasattr(self._artop_useCase, "uuid"):
                return self._artop_useCase.uuid
        return

    @property
    def ref_conflicts_(self):
        return self._artop_conflicts

    @property
    def conflicts_(self):
        if self._artop_conflicts is not None:
            if hasattr(self._artop_conflicts, "uuid"):
                return self._artop_conflicts.uuid
        return

    @property
    def ref_supportingMaterial_(self):
        return self._artop_supportingMaterial

    @property
    def supportingMaterial_(self):
        if self._artop_supportingMaterial is not None:
            if hasattr(self._artop_supportingMaterial, "uuid"):
                return self._artop_supportingMaterial.uuid
        return

    @property
    def ref_remark_(self):
        return self._artop_remark

    @property
    def remark_(self):
        if self._artop_remark is not None:
            if hasattr(self._artop_remark, "uuid"):
                return self._artop_remark.uuid
        return

    @property
    def ref_testedItems_(self):
        return self._artop_testedItemRef

    @property
    def testedItems_(self):
        return self._artop_testedItemRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
