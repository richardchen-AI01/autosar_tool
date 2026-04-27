# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdgAggregationWithVariation.py
from .AbstractVariationRestriction import AbstractVariationRestriction
from .SdgElementWithGid import SdgElementWithGid
from .SdgAttribute import SdgAttribute

class SdgAggregationWithVariation(SdgAttribute, SdgElementWithGid, AbstractVariationRestriction):

    def __init__(self):
        super().__init__()
        from .SdgClass import SdgClass
        self._artop_subSdgRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_subSdgRef": "SDG-CLASS"})

    @property
    def ref_subSdg_(self):
        return self._artop_subSdgRef

    @property
    def subSdg_(self):
        if self._artop_subSdgRef is not None:
            if hasattr(self._artop_subSdgRef, "uuid"):
                return self._artop_subSdgRef.uuid
        return
