# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TriggerMapping.py
from .ARObject import ARObject

class TriggerMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .TriggerInterfaceMapping import TriggerInterfaceMapping
        from .Trigger import Trigger
        self._artop_triggerInterfaceMapping = None
        self._artop_firstTriggerRef = None
        self._artop_secondTriggerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_triggerInterfaceMapping':"TRIGGER-INTERFACE-MAPPING", 
         '_artop_firstTriggerRef':"TRIGGER", 
         '_artop_secondTriggerRef':"TRIGGER"})

    @property
    def ref_triggerInterfaceMapping_(self):
        return self._artop_triggerInterfaceMapping

    @property
    def triggerInterfaceMapping_(self):
        if self._artop_triggerInterfaceMapping is not None:
            if hasattr(self._artop_triggerInterfaceMapping, "uuid"):
                return self._artop_triggerInterfaceMapping.uuid
        return

    @property
    def ref_firstTrigger_(self):
        return self._artop_firstTriggerRef

    @property
    def firstTrigger_(self):
        if self._artop_firstTriggerRef is not None:
            if hasattr(self._artop_firstTriggerRef, "uuid"):
                return self._artop_firstTriggerRef.uuid
        return

    @property
    def ref_secondTrigger_(self):
        return self._artop_secondTriggerRef

    @property
    def secondTrigger_(self):
        if self._artop_secondTriggerRef is not None:
            if hasattr(self._artop_secondTriggerRef, "uuid"):
                return self._artop_secondTriggerRef.uuid
        return
