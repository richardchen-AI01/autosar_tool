# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswDebugInfo.py
from .Identifiable import Identifiable

class BswDebugInfo(Identifiable):

    def __init__(self):
        super().__init__()
        from .BswImplementation import BswImplementation
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        from .ParameterDataPrototype import ParameterDataPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .VariationPoint import VariationPoint
        self._artop_bswImplementation = None
        self._artop_localDebugData = []
        self._artop_parameterAccessedForDebugRef = []
        self._artop_variableAccessedForDebugRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswImplementation': '"BSW-IMPLEMENTATION"', 
         '_artop_localDebugData': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_parameterAccessedForDebugRef': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_variableAccessedForDebugRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_bswImplementation_(self):
        return self._artop_bswImplementation

    @property
    def bswImplementation_(self):
        if self._artop_bswImplementation is not None:
            if hasattr(self._artop_bswImplementation, "uuid"):
                return self._artop_bswImplementation.uuid
        return

    @property
    def localDebugDatas_ImplementationDataTypeElement(self):
        return self._artop_localDebugData

    @property
    def ref_parameterAccessedForDebugs_(self):
        return self._artop_parameterAccessedForDebugRef

    @property
    def parameterAccessedForDebugs_(self):
        return self._artop_parameterAccessedForDebugRef

    @property
    def ref_variableAccessedForDebugs_(self):
        return self._artop_variableAccessedForDebugRef

    @property
    def variableAccessedForDebugs_(self):
        return self._artop_variableAccessedForDebugRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
