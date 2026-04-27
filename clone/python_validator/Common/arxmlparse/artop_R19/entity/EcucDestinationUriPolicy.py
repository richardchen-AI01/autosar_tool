# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucDestinationUriPolicy.py
from .ARObject import ARObject

class EcucDestinationUriPolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .EcucDestinationUriDef import EcucDestinationUriDef
        from .EcucContainerDef import EcucContainerDef
        from .EcucParameterDef import EcucParameterDef
        from .EcucAbstractReferenceDef import EcucAbstractReferenceDef
        self._artop_destinationUriNestingContract = None
        self._artop_ecucDestinationUriDef = None
        self._artop_container = []
        self._artop_parameter = []
        self._artop_reference = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ecucDestinationUriDef': '"ECUC-DESTINATION-URI-DEF"', 
         '_artop_container': '"ECUC-CONTAINER-DEF"', 
         '_artop_parameter': '"ECUC-PARAMETER-DEF"', 
         '_artop_reference': '"ECUC-ABSTRACT-REFERENCE-DEF"'})

    @property
    def destinationUriNestingContract_(self):
        return self._artop_destinationUriNestingContract

    @property
    def ref_ecucDestinationUriDef_(self):
        return self._artop_ecucDestinationUriDef

    @property
    def ecucDestinationUriDef_(self):
        if self._artop_ecucDestinationUriDef is not None:
            if hasattr(self._artop_ecucDestinationUriDef, "uuid"):
                return self._artop_ecucDestinationUriDef.uuid
        return

    @property
    def containers_EcucContainerDef(self):
        return self._artop_container

    @property
    def parameters_EcucParameterDef(self):
        return self._artop_parameter

    @property
    def references_EcucAbstractReferenceDef(self):
        return self._artop_reference
