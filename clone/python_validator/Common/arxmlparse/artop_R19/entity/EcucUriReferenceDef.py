# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucUriReferenceDef.py
from .EcucAbstractInternalReferenceDef import EcucAbstractInternalReferenceDef

class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):

    def __init__(self):
        super().__init__()
        from .EcucDestinationUriDef import EcucDestinationUriDef
        self._artop_destinationUriRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_destinationUriRef": "ECUC-DESTINATION-URI-DEF"})

    @property
    def ref_destinationUri_(self):
        return self._artop_destinationUriRef

    @property
    def destinationUri_(self):
        if self._artop_destinationUriRef is not None:
            if hasattr(self._artop_destinationUriRef, "uuid"):
                return self._artop_destinationUriRef.uuid
        return
