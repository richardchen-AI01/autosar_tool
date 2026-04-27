# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComOfferServiceGrantDesign.py
from .GrantDesign import GrantDesign

class ComOfferServiceGrantDesign(GrantDesign):

    def __init__(self):
        super().__init__()
        from .PPortPrototypeInExecutableInstanceRef import PPortPrototypeInExecutableInstanceRef
        self._artop_providedServicePortIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_providedServicePortIref": "P-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF"})

    @property
    def ref_providedServicePort_(self):
        return self._artop_providedServicePortIref

    @property
    def providedServicePort_(self):
        if self._artop_providedServicePortIref is not None:
            if hasattr(self._artop_providedServicePortIref, "uuid"):
                return self._artop_providedServicePortIref.uuid
        return
