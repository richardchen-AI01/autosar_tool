# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintGenerator.py
from .ARObject import ARObject

class BlueprintGenerator(ARObject):

    def __init__(self):
        super().__init__()
        from .VariationPoint import VariationPoint
        from .DocumentationBlock import DocumentationBlock
        self._artop_expression = None
        self._artop_variationPoint = None
        self._artop_introduction = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_variationPoint':"VARIATION-POINT", 
         '_artop_introduction':"DOCUMENTATION-BLOCK"})

    @property
    def expression_(self):
        return self._artop_expression

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return

    @property
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return
