# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticParameter.py
from .ARObject import ARObject

class DiagnosticParameter(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataElement import DiagnosticDataElement
        from .DiagnosticParameterSupportInfo import DiagnosticParameterSupportInfo
        from .VariationPoint import VariationPoint
        self._artop_bitOffset = None
        self._artop_dataElement = []
        self._artop_supportInfo = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElement':"DIAGNOSTIC-DATA-ELEMENT", 
         '_artop_supportInfo':"DIAGNOSTIC-PARAMETER-SUPPORT-INFO", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def bitOffset_(self):
        return self._artop_bitOffset

    @property
    def dataElements_DiagnosticDataElement(self):
        return self._artop_dataElement

    @property
    def ref_supportInfo_(self):
        return self._artop_supportInfo

    @property
    def supportInfo_(self):
        if self._artop_supportInfo is not None:
            if hasattr(self._artop_supportInfo, "uuid"):
                return self._artop_supportInfo.uuid
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
