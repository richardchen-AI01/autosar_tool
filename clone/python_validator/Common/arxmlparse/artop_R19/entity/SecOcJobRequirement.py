# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecOcJobRequirement.py
from .Identifiable import Identifiable

class SecOcJobRequirement(Identifiable):

    def __init__(self):
        super().__init__()
        from .SecOcSecureComProps import SecOcSecureComProps
        self._artop_secOcJobSemantic = None
        self._artop_secOcSecureComProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_secOcSecureComProps": "SEC-OC-SECURE-COM-PROPS"})

    @property
    def secOcJobSemantic_(self):
        return self._artop_secOcJobSemantic

    @property
    def ref_secOcSecureComProps_(self):
        return self._artop_secOcSecureComProps

    @property
    def secOcSecureComProps_(self):
        if self._artop_secOcSecureComProps is not None:
            if hasattr(self._artop_secOcSecureComProps, "uuid"):
                return self._artop_secOcSecureComProps.uuid
        return
