# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AttributeValueVariationPoint.py
from .SwSystemconstDependentFormula import SwSystemconstDependentFormula

class AttributeValueVariationPoint(SwSystemconstDependentFormula):

    def __init__(self):
        super().__init__()
        from .VariationPointProxy import VariationPointProxy
        self._artop_bindingTime = None
        self._artop_blueprintValue = None
        self._artop_sd = None
        self._artop_shortLabel = None
        self._artop_variationPointProxy = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_variationPointProxy": "VARIATION-POINT-PROXY"})

    @property
    def bindingTime_(self):
        return self._artop_bindingTime

    @property
    def blueprintValue_(self):
        return self._artop_blueprintValue

    @property
    def sd_(self):
        return self._artop_sd

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_variationPointProxy_(self):
        return self._artop_variationPointProxy

    @property
    def variationPointProxy_(self):
        if self._artop_variationPointProxy is not None:
            if hasattr(self._artop_variationPointProxy, "uuid"):
                return self._artop_variationPointProxy.uuid
        return
