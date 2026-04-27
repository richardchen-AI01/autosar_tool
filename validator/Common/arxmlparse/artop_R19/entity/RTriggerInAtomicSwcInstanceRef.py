# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RTriggerInAtomicSwcInstanceRef.py
from .TriggerInAtomicSwcInstanceRef import TriggerInAtomicSwcInstanceRef

class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):

    def __init__(self):
        super().__init__()
        from .ExternalTriggerOccurredEvent import ExternalTriggerOccurredEvent
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        from .Trigger import Trigger
        from .AtomicSwComponentType import AtomicSwComponentType
        self._artop_externalTriggerOccurredEvent = None
        self._artop_contextRPortRef = None
        self._artop_targetTriggerRef = None
        self._artop_atomicSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_externalTriggerOccurredEvent': '"EXTERNAL-TRIGGER-OCCURRED-EVENT"', 
         '_artop_contextRPortRef': '"ABSTRACT-REQUIRED-PORT-PROTOTYPE"', 
         '_artop_targetTriggerRef': '"TRIGGER"', 
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"'})

    @property
    def ref_externalTriggerOccurredEvent_(self):
        return self._artop_externalTriggerOccurredEvent

    @property
    def externalTriggerOccurredEvent_(self):
        if self._artop_externalTriggerOccurredEvent is not None:
            if hasattr(self._artop_externalTriggerOccurredEvent, "uuid"):
                return self._artop_externalTriggerOccurredEvent.uuid
        return

    @property
    def ref_contextRPort_(self):
        return self._artop_contextRPortRef

    @property
    def contextRPort_(self):
        if self._artop_contextRPortRef is not None:
            if hasattr(self._artop_contextRPortRef, "uuid"):
                return self._artop_contextRPortRef.uuid
        return

    @property
    def ref_targetTrigger_(self):
        return self._artop_targetTriggerRef

    @property
    def targetTrigger_(self):
        if self._artop_targetTriggerRef is not None:
            if hasattr(self._artop_targetTriggerRef, "uuid"):
                return self._artop_targetTriggerRef.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_atomicSwComponentType

    @property
    def base_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return
