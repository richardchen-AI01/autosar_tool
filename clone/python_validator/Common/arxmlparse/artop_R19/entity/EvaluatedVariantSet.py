# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EvaluatedVariantSet.py
from .ARElement import ARElement

class EvaluatedVariantSet(ARElement):

    def __init__(self):
        super().__init__()
        from .CollectableElement import CollectableElement
        from .PredefinedVariant import PredefinedVariant
        self._artop_approvalStatus = None
        self._artop_evaluatedElementRef = []
        self._artop_evaluatedVariantRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_evaluatedElementRef':"COLLECTABLE-ELEMENT", 
         '_artop_evaluatedVariantRef':"PREDEFINED-VARIANT"})

    @property
    def approvalStatus_(self):
        return self._artop_approvalStatus

    @property
    def ref_evaluatedElements_(self):
        return self._artop_evaluatedElementRef

    @property
    def evaluatedElements_(self):
        return self._artop_evaluatedElementRef

    @property
    def ref_evaluatedVariants_(self):
        return self._artop_evaluatedVariantRef

    @property
    def evaluatedVariants_(self):
        return self._artop_evaluatedVariantRef
