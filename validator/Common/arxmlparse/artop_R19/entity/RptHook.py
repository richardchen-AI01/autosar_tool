# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptHook.py
from .ARObject import ARObject

class RptHook(ARObject):

    def __init__(self):
        super().__init__()
        from .RptContainer import RptContainer
        from .AnyInstanceRef import AnyInstanceRef
        from .Sdg import Sdg
        from .VariationPoint import VariationPoint
        self._artop_codeLabel = None
        self._artop_mcdIdentifier = None
        self._artop_rptContainer = None
        self._artop_rptArHookIref = None
        self._artop_sdg = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_rptContainer': '"RPT-CONTAINER"', 
         '_artop_rptArHookIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_sdg': '"SDG"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def codeLabel_(self):
        return self._artop_codeLabel

    @property
    def mcdIdentifier_(self):
        return self._artop_mcdIdentifier

    @property
    def ref_rptContainer_(self):
        return self._artop_rptContainer

    @property
    def rptContainer_(self):
        if self._artop_rptContainer is not None:
            if hasattr(self._artop_rptContainer, "uuid"):
                return self._artop_rptContainer.uuid
        return

    @property
    def ref_rptArHook_(self):
        return self._artop_rptArHookIref

    @property
    def rptArHook_(self):
        if self._artop_rptArHookIref is not None:
            if hasattr(self._artop_rptArHookIref, "uuid"):
                return self._artop_rptArHookIref.uuid
        return

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
