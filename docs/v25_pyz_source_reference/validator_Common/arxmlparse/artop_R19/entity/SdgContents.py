# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SdgContents.py
from .ARObject import ARObject

class SdgContents(ARObject):

    def __init__(self):
        super().__init__()
        from .Sdg import Sdg
        from .Referrable import Referrable
        from .ReferrableRefConditional import ReferrableRefConditional
        from .Sd import Sd
        from .Sdf import Sdf
        self._artop_mixed = None
        self._artop_sdg = None
        self._artop_sdxRef = []
        self._artop_sdxf = []
        self._artop_sd = []
        self._artop_sdg = []
        self._artop_sdf = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_sdg': '"SDG"', 
         '_artop_sdxRef': '"REFERRABLE"', 
         '_artop_sdxf': '"REFERRABLE-REF-CONDITIONAL"', 
         '_artop_sd': '"SD"', 
         '_artop_sdg': '"SDG"', 
         '_artop_sdf': '"SDF"'})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_sdg_(self):
        return self._artop_sdg

    @property
    def sdg_(self):
        if self._artop_sdg is not None:
            if hasattr(self._artop_sdg, "uuid"):
                return self._artop_sdg.uuid
        return

    @property
    def ref_sdxs_(self):
        return self._artop_sdxRef

    @property
    def sdxs_(self):
        return self._artop_sdxRef

    @property
    def sdxfs_ReferrableRefConditional(self):
        return self._artop_sdxf

    @property
    def sds_Sd(self):
        return self._artop_sd

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg

    @property
    def sdfs_Sdf(self):
        return self._artop_sdf
