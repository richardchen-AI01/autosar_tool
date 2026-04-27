# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractEvent.py
from .Identifiable import Identifiable

class AbstractEvent(Identifiable):

    def __init__(self):
        super().__init__()
        from .ExecutableEntityActivationReason import ExecutableEntityActivationReason
        self._artop_activationReasonRepresentationRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_activationReasonRepresentationRef": "EXECUTABLE-ENTITY-ACTIVATION-REASON"})

    @property
    def ref_activationReasonRepresentation_(self):
        return self._artop_activationReasonRepresentationRef

    @property
    def activationReasonRepresentation_(self):
        if self._artop_activationReasonRepresentationRef is not None:
            if hasattr(self._artop_activationReasonRepresentationRef, "uuid"):
                return self._artop_activationReasonRepresentationRef.uuid
        return
