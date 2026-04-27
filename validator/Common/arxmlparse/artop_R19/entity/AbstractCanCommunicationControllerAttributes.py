# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractCanCommunicationControllerAttributes.py
from .ARObject import ARObject

class AbstractCanCommunicationControllerAttributes(ARObject):

    def __init__(self):
        super().__init__()
        from .AbstractCanCommunicationControllerContent import AbstractCanCommunicationControllerContent
        from .CanControllerFdConfiguration import CanControllerFdConfiguration
        from .CanControllerFdConfigurationRequirements import CanControllerFdConfigurationRequirements
        self._artop_abstractCanCommunicationControllerContent = None
        self._artop_canControllerFdAttributes = None
        self._artop_canControllerFdRequirements = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_abstractCanCommunicationControllerContent':"ABSTRACT-CAN-COMMUNICATION-CONTROLLER-CONTENT", 
         '_artop_canControllerFdAttributes':"CAN-CONTROLLER-FD-CONFIGURATION", 
         '_artop_canControllerFdRequirements':"CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS"})

    @property
    def ref_abstractCanCommunicationControllerContent_(self):
        return self._artop_abstractCanCommunicationControllerContent

    @property
    def abstractCanCommunicationControllerContent_(self):
        if self._artop_abstractCanCommunicationControllerContent is not None:
            if hasattr(self._artop_abstractCanCommunicationControllerContent, "uuid"):
                return self._artop_abstractCanCommunicationControllerContent.uuid
        return

    @property
    def ref_canControllerFdAttributes_(self):
        return self._artop_canControllerFdAttributes

    @property
    def canControllerFdAttributes_(self):
        if self._artop_canControllerFdAttributes is not None:
            if hasattr(self._artop_canControllerFdAttributes, "uuid"):
                return self._artop_canControllerFdAttributes.uuid
        return

    @property
    def ref_canControllerFdRequirements_(self):
        return self._artop_canControllerFdRequirements

    @property
    def canControllerFdRequirements_(self):
        if self._artop_canControllerFdRequirements is not None:
            if hasattr(self._artop_canControllerFdRequirements, "uuid"):
                return self._artop_canControllerFdRequirements.uuid
        return
