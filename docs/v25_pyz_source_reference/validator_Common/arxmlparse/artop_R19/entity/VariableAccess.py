# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariableAccess.py
from .AbstractAccessPoint import AbstractAccessPoint

class VariableAccess(AbstractAccessPoint):

    def __init__(self):
        super().__init__()
        from .AutosarVariableRef import AutosarVariableRef
        from .VariationPoint import VariationPoint
        self._artop_scope = None
        self._artop_accessedVariable = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_accessedVariable':"AUTOSAR-VARIABLE-REF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def scope_(self):
        return self._artop_scope

    @property
    def ref_accessedVariable_(self):
        return self._artop_accessedVariable

    @property
    def accessedVariable_(self):
        if self._artop_accessedVariable is not None:
            if hasattr(self._artop_accessedVariable, "uuid"):
                return self._artop_accessedVariable.uuid
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
