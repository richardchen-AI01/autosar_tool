# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerToSignalGroupMapping.py
from .DataMapping import DataMapping

class ClientServerToSignalGroupMapping(DataMapping):

    def __init__(self):
        super().__init__()
        from .ApplicationErrorMapping import ApplicationErrorMapping
        from .ClientIdMapping import ClientIdMapping
        from .ClientServerCompositeTypeMapping import ClientServerCompositeTypeMapping
        from .EmptySignalMapping import EmptySignalMapping
        from .OperationInSystemInstanceRef import OperationInSystemInstanceRef
        from .ClientServerPrimitiveTypeMapping import ClientServerPrimitiveTypeMapping
        from .SystemSignalGroup import SystemSignalGroup
        from .SequenceCounterMapping import SequenceCounterMapping
        self._artop_applicationError = None
        self._artop_clientId = None
        self._artop_compositeTypeMapping = []
        self._artop_emptySignal = None
        self._artop_mappedOperationIref = None
        self._artop_primitiveTypeMapping = []
        self._artop_requestGroupRef = None
        self._artop_responseGroupRef = None
        self._artop_sequenceCounter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_applicationError': '"APPLICATION-ERROR-MAPPING"', 
         '_artop_clientId': '"CLIENT-ID-MAPPING"', 
         '_artop_compositeTypeMapping': '"CLIENT-SERVER-COMPOSITE-TYPE-MAPPING"', 
         '_artop_emptySignal': '"EMPTY-SIGNAL-MAPPING"', 
         '_artop_mappedOperationIref': '"OPERATION-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_primitiveTypeMapping': '"CLIENT-SERVER-PRIMITIVE-TYPE-MAPPING"', 
         '_artop_requestGroupRef': '"SYSTEM-SIGNAL-GROUP"', 
         '_artop_responseGroupRef': '"SYSTEM-SIGNAL-GROUP"', 
         '_artop_sequenceCounter': '"SEQUENCE-COUNTER-MAPPING"'})

    @property
    def ref_applicationError_(self):
        return self._artop_applicationError

    @property
    def applicationError_(self):
        if self._artop_applicationError is not None:
            if hasattr(self._artop_applicationError, "uuid"):
                return self._artop_applicationError.uuid
        return

    @property
    def ref_clientID_(self):
        return self._artop_clientId

    @property
    def clientID_(self):
        if self._artop_clientId is not None:
            if hasattr(self._artop_clientId, "uuid"):
                return self._artop_clientId.uuid
        return

    @property
    def compositeTypeMappings_ClientServerCompositeTypeMapping(self):
        return self._artop_compositeTypeMapping

    @property
    def ref_emptySignal_(self):
        return self._artop_emptySignal

    @property
    def emptySignal_(self):
        if self._artop_emptySignal is not None:
            if hasattr(self._artop_emptySignal, "uuid"):
                return self._artop_emptySignal.uuid
        return

    @property
    def ref_mappedOperation_(self):
        return self._artop_mappedOperationIref

    @property
    def mappedOperation_(self):
        if self._artop_mappedOperationIref is not None:
            if hasattr(self._artop_mappedOperationIref, "uuid"):
                return self._artop_mappedOperationIref.uuid
        return

    @property
    def primitiveTypeMappings_ClientServerPrimitiveTypeMapping(self):
        return self._artop_primitiveTypeMapping

    @property
    def ref_requestGroup_(self):
        return self._artop_requestGroupRef

    @property
    def requestGroup_(self):
        if self._artop_requestGroupRef is not None:
            if hasattr(self._artop_requestGroupRef, "uuid"):
                return self._artop_requestGroupRef.uuid
        return

    @property
    def ref_responseGroup_(self):
        return self._artop_responseGroupRef

    @property
    def responseGroup_(self):
        if self._artop_responseGroupRef is not None:
            if hasattr(self._artop_responseGroupRef, "uuid"):
                return self._artop_responseGroupRef.uuid
        return

    @property
    def ref_sequenceCounter_(self):
        return self._artop_sequenceCounter

    @property
    def sequenceCounter_(self):
        if self._artop_sequenceCounter is not None:
            if hasattr(self._artop_sequenceCounter, "uuid"):
                return self._artop_sequenceCounter.uuid
        return
