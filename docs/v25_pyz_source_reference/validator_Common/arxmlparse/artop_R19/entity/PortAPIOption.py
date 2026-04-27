# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortAPIOption.py
from .ARObject import ARObject

class PortAPIOption(ARObject):

    def __init__(self):
        super().__init__()
        from .SwcInternalBehavior import SwcInternalBehavior
        from .PortDefinedArgumentValue import PortDefinedArgumentValue
        from .PortPrototype import PortPrototype
        from .SwcSupportedFeature import SwcSupportedFeature
        from .VariationPoint import VariationPoint
        self._artop_enableTakeAddress = None
        self._artop_errorHandling = None
        self._artop_indirectApi = None
        self._artop_transformerStatusForwarding = None
        self._artop_swcInternalBehavior = None
        self._artop_portArgValue = []
        self._artop_portRef = None
        self._artop_supportedFeature = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcInternalBehavior': '"SWC-INTERNAL-BEHAVIOR"', 
         '_artop_portArgValue': '"PORT-DEFINED-ARGUMENT-VALUE"', 
         '_artop_portRef': '"PORT-PROTOTYPE"', 
         '_artop_supportedFeature': '"SWC-SUPPORTED-FEATURE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def enableTakeAddress_(self):
        if self._artop_enableTakeAddress:
            if self._artop_enableTakeAddress == "true":
                return True
            return False
        else:
            return self._artop_enableTakeAddress

    @property
    def errorHandling_(self):
        return self._artop_errorHandling

    @property
    def indirectApi_(self):
        if self._artop_indirectApi:
            if self._artop_indirectApi == "true":
                return True
            return False
        else:
            return self._artop_indirectApi

    @property
    def transformerStatusForwarding_(self):
        return self._artop_transformerStatusForwarding

    @property
    def ref_swcInternalBehavior_(self):
        return self._artop_swcInternalBehavior

    @property
    def swcInternalBehavior_(self):
        if self._artop_swcInternalBehavior is not None:
            if hasattr(self._artop_swcInternalBehavior, "uuid"):
                return self._artop_swcInternalBehavior.uuid
        return

    @property
    def portArgValues_PortDefinedArgumentValue(self):
        return self._artop_portArgValue

    @property
    def ref_port_(self):
        return self._artop_portRef

    @property
    def port_(self):
        if self._artop_portRef is not None:
            if hasattr(self._artop_portRef, "uuid"):
                return self._artop_portRef.uuid
        return

    @property
    def supportedFeatures_SwcSupportedFeature(self):
        return self._artop_supportedFeature

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
