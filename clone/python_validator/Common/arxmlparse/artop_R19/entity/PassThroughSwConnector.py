# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PassThroughSwConnector.py
from .SwConnector import SwConnector

class PassThroughSwConnector(SwConnector):

    def __init__(self):
        super().__init__()
        from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        self._artop_providedOuterPortRef = None
        self._artop_requiredOuterPortRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providedOuterPortRef':"ABSTRACT-PROVIDED-PORT-PROTOTYPE", 
         '_artop_requiredOuterPortRef':"ABSTRACT-REQUIRED-PORT-PROTOTYPE"})

    @property
    def ref_providedOuterPort_(self):
        return self._artop_providedOuterPortRef

    @property
    def providedOuterPort_(self):
        if self._artop_providedOuterPortRef is not None:
            if hasattr(self._artop_providedOuterPortRef, "uuid"):
                return self._artop_providedOuterPortRef.uuid
        return

    @property
    def ref_requiredOuterPort_(self):
        return self._artop_requiredOuterPortRef

    @property
    def requiredOuterPort_(self):
        if self._artop_requiredOuterPortRef is not None:
            if hasattr(self._artop_requiredOuterPortRef, "uuid"):
                return self._artop_requiredOuterPortRef.uuid
        return
