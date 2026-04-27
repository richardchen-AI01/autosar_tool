# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucDestinationUriDef.py
from .Identifiable import Identifiable

class EcucDestinationUriDef(Identifiable):

    def __init__(self):
        super().__init__()
        from .EcucDestinationUriDefSet import EcucDestinationUriDefSet
        from .EcucDestinationUriPolicy import EcucDestinationUriPolicy
        self._artop_ecucDestinationUriDefSet = None
        self._artop_destinationUriPolicy = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ecucDestinationUriDefSet':"ECUC-DESTINATION-URI-DEF-SET", 
         '_artop_destinationUriPolicy':"ECUC-DESTINATION-URI-POLICY"})

    @property
    def ref_ecucDestinationUriDefSet_(self):
        return self._artop_ecucDestinationUriDefSet

    @property
    def ecucDestinationUriDefSet_(self):
        if self._artop_ecucDestinationUriDefSet is not None:
            if hasattr(self._artop_ecucDestinationUriDefSet, "uuid"):
                return self._artop_ecucDestinationUriDefSet.uuid
        return

    @property
    def ref_destinationUriPolicy_(self):
        return self._artop_destinationUriPolicy

    @property
    def destinationUriPolicy_(self):
        if self._artop_destinationUriPolicy is not None:
            if hasattr(self._artop_destinationUriPolicy, "uuid"):
                return self._artop_destinationUriPolicy.uuid
        return
