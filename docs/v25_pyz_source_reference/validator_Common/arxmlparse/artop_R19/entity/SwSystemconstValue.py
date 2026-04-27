# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwSystemconstValue.py
from .ARObject import ARObject

class SwSystemconstValue(ARObject):

    def __init__(self):
        super().__init__()
        from .SwSystemconstantValueSet import SwSystemconstantValueSet
        from .SwSystemconst import SwSystemconst
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        from .Annotation import Annotation
        self._artop_swSystemconstantValueSet = None
        self._artop_swSystemconstRef = None
        self._artop_value = None
        self._artop_annotation = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swSystemconstantValueSet': '"SW-SYSTEMCONSTANT-VALUE-SET"', 
         '_artop_swSystemconstRef': '"SW-SYSTEMCONST"', 
         '_artop_value': '"NUMERICAL-VALUE-VARIATION-POINT"', 
         '_artop_annotation': '"ANNOTATION"'})

    @property
    def ref_swSystemconstantValueSet_(self):
        return self._artop_swSystemconstantValueSet

    @property
    def swSystemconstantValueSet_(self):
        if self._artop_swSystemconstantValueSet is not None:
            if hasattr(self._artop_swSystemconstantValueSet, "uuid"):
                return self._artop_swSystemconstantValueSet.uuid
        return

    @property
    def ref_swSystemconst_(self):
        return self._artop_swSystemconstRef

    @property
    def swSystemconst_(self):
        if self._artop_swSystemconstRef is not None:
            if hasattr(self._artop_swSystemconstRef, "uuid"):
                return self._artop_swSystemconstRef.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
        return

    @property
    def annotations_Annotation(self):
        return self._artop_annotation
