# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortStructuralElement.py
from .Identifiable import Identifiable

class CouplingPortStructuralElement(Identifiable):

    def __init__(self):
        super().__init__()
        from .CouplingPortDetails import CouplingPortDetails
        self._artop_couplingPortDetails = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_couplingPortDetails": "COUPLING-PORT-DETAILS"})

    @property
    def ref_couplingPortDetails_(self):
        return self._artop_couplingPortDetails

    @property
    def couplingPortDetails_(self):
        if self._artop_couplingPortDetails is not None:
            if hasattr(self._artop_couplingPortDetails, "uuid"):
                return self._artop_couplingPortDetails.uuid
        return
