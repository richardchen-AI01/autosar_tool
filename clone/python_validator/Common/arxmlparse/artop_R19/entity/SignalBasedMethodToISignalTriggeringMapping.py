# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SignalBasedMethodToISignalTriggeringMapping.py
from .AbstractSignalBasedToISignalTriggeringMapping import AbstractSignalBasedToISignalTriggeringMapping

class SignalBasedMethodToISignalTriggeringMapping(AbstractSignalBasedToISignalTriggeringMapping):

    def __init__(self):
        super().__init__()
        from .ServiceInstanceToSignalMapping import ServiceInstanceToSignalMapping
        from .ISignalTriggering import ISignalTriggering
        from .ClientServerOperation import ClientServerOperation
        self._artop_serviceInstanceToSignalMapping = None
        self._artop_callSignalTriggeringRef = None
        self._artop_methodRef = None
        self._artop_returnSignalTriggeringRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_serviceInstanceToSignalMapping': '"SERVICE-INSTANCE-TO-SIGNAL-MAPPING"', 
         '_artop_callSignalTriggeringRef': '"I-SIGNAL-TRIGGERING"', 
         '_artop_methodRef': '"CLIENT-SERVER-OPERATION"', 
         '_artop_returnSignalTriggeringRef': '"I-SIGNAL-TRIGGERING"'})

    @property
    def ref_serviceInstanceToSignalMapping_(self):
        return self._artop_serviceInstanceToSignalMapping

    @property
    def serviceInstanceToSignalMapping_(self):
        if self._artop_serviceInstanceToSignalMapping is not None:
            if hasattr(self._artop_serviceInstanceToSignalMapping, "uuid"):
                return self._artop_serviceInstanceToSignalMapping.uuid
        return

    @property
    def ref_callSignalTriggering_(self):
        return self._artop_callSignalTriggeringRef

    @property
    def callSignalTriggering_(self):
        if self._artop_callSignalTriggeringRef is not None:
            if hasattr(self._artop_callSignalTriggeringRef, "uuid"):
                return self._artop_callSignalTriggeringRef.uuid
        return

    @property
    def ref_method_(self):
        return self._artop_methodRef

    @property
    def method_(self):
        if self._artop_methodRef is not None:
            if hasattr(self._artop_methodRef, "uuid"):
                return self._artop_methodRef.uuid
        return

    @property
    def ref_returnSignalTriggering_(self):
        return self._artop_returnSignalTriggeringRef

    @property
    def returnSignalTriggering_(self):
        if self._artop_returnSignalTriggeringRef is not None:
            if hasattr(self._artop_returnSignalTriggeringRef, "uuid"):
                return self._artop_returnSignalTriggeringRef.uuid
        return
