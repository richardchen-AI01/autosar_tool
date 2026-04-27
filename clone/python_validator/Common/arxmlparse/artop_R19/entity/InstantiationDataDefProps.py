# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InstantiationDataDefProps.py
from .ARObject import ARObject

class InstantiationDataDefProps(ARObject):

    def __init__(self):
        super().__init__()
        from .AutosarParameterRef import AutosarParameterRef
        from .SwDataDefProps import SwDataDefProps
        from .AutosarVariableRef import AutosarVariableRef
        from .VariationPoint import VariationPoint
        self._artop_parameterInstance = None
        self._artop_swDataDefProps = None
        self._artop_variableInstance = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_parameterInstance': '"AUTOSAR-PARAMETER-REF"', 
         '_artop_swDataDefProps': '"SW-DATA-DEF-PROPS"', 
         '_artop_variableInstance': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_parameterInstance_(self):
        return self._artop_parameterInstance

    @property
    def parameterInstance_(self):
        if self._artop_parameterInstance is not None:
            if hasattr(self._artop_parameterInstance, "uuid"):
                return self._artop_parameterInstance.uuid
        return

    @property
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
        return

    @property
    def ref_variableInstance_(self):
        return self._artop_variableInstance

    @property
    def variableInstance_(self):
        if self._artop_variableInstance is not None:
            if hasattr(self._artop_variableInstance, "uuid"):
                return self._artop_variableInstance.uuid
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
