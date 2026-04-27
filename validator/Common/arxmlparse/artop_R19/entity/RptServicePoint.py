# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptServicePoint.py
from .Identifiable import Identifiable

class RptServicePoint(Identifiable):

    def __init__(self):
        super().__init__()
        from .RptSupportData import RptSupportData
        from .VariationPoint import VariationPoint
        self._artop_serviceId = None
        self._artop_symbol = None
        self._artop_rptSupportData = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_rptSupportData':"RPT-SUPPORT-DATA", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def serviceId_(self):
        return self._artop_serviceId

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def ref_rptSupportData_(self):
        return self._artop_rptSupportData

    @property
    def rptSupportData_(self):
        if self._artop_rptSupportData is not None:
            if hasattr(self._artop_rptSupportData, "uuid"):
                return self._artop_rptSupportData.uuid
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
