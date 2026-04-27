# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReferrableRefConditional.py
from .ARObject import ARObject

class ReferrableRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .SdgContents import SdgContents
        from .Referrable import Referrable
        from .VariationPoint import VariationPoint
        self._artop_sdgContents = None
        self._artop_referrableRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_sdgContents':"SDG-CONTENTS", 
         '_artop_referrableRef':"REFERRABLE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_sdgContents_(self):
        return self._artop_sdgContents

    @property
    def sdgContents_(self):
        if self._artop_sdgContents is not None:
            if hasattr(self._artop_sdgContents, "uuid"):
                return self._artop_sdgContents.uuid
        return

    @property
    def ref_referrable_(self):
        return self._artop_referrableRef

    @property
    def referrable_(self):
        if self._artop_referrableRef is not None:
            if hasattr(self._artop_referrableRef, "uuid"):
                return self._artop_referrableRef.uuid
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
