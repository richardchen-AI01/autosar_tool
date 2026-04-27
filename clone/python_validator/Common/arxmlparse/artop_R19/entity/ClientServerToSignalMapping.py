# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerToSignalMapping.py
from .DataMapping import DataMapping

class ClientServerToSignalMapping(DataMapping):

    def __init__(self):
        super().__init__()
        from .SystemSignal import SystemSignal
        from .OperationInSystemInstanceRef import OperationInSystemInstanceRef
        from .SerializationTechnology import SerializationTechnology
        self._artop_lengthClientId = None
        self._artop_lengthSequenceCounter = None
        self._artop_callSignalRef = None
        self._artop_clientServerOperationIref = None
        self._artop_returnSignalRef = None
        self._artop_serializerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_callSignalRef': '"SYSTEM-SIGNAL"', 
         '_artop_clientServerOperationIref': '"OPERATION-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_returnSignalRef': '"SYSTEM-SIGNAL"', 
         '_artop_serializerRef': '"SERIALIZATION-TECHNOLOGY"'})

    @property
    def lengthClientId_(self):
        return self._artop_lengthClientId

    @property
    def lengthSequenceCounter_(self):
        return self._artop_lengthSequenceCounter

    @property
    def ref_callSignal_(self):
        return self._artop_callSignalRef

    @property
    def callSignal_(self):
        if self._artop_callSignalRef is not None:
            if hasattr(self._artop_callSignalRef, "uuid"):
                return self._artop_callSignalRef.uuid
        return

    @property
    def ref_clientServerOperation_(self):
        return self._artop_clientServerOperationIref

    @property
    def clientServerOperation_(self):
        if self._artop_clientServerOperationIref is not None:
            if hasattr(self._artop_clientServerOperationIref, "uuid"):
                return self._artop_clientServerOperationIref.uuid
        return

    @property
    def ref_returnSignal_(self):
        return self._artop_returnSignalRef

    @property
    def returnSignal_(self):
        if self._artop_returnSignalRef is not None:
            if hasattr(self._artop_returnSignalRef, "uuid"):
                return self._artop_returnSignalRef.uuid
        return

    @property
    def ref_serializer_(self):
        return self._artop_serializerRef

    @property
    def serializer_(self):
        if self._artop_serializerRef is not None:
            if hasattr(self._artop_serializerRef, "uuid"):
                return self._artop_serializerRef.uuid
        return
