# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SenderRecRecordElementMapping.py
from .ARObject import ARObject

class SenderRecRecordElementMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .SenderRecRecordTypeMapping import SenderRecRecordTypeMapping
        from .ApplicationRecordElement import ApplicationRecordElement
        from .SenderRecCompositeTypeMapping import SenderRecCompositeTypeMapping
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        from .SystemSignal import SystemSignal
        self._artop_senderRecRecordTypeMapping = None
        self._artop_applicationRecordElementRef = None
        self._artop_complexTypeMapping = None
        self._artop_implementationRecordElementRef = None
        self._artop_systemSignalRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_senderRecRecordTypeMapping': '"SENDER-REC-RECORD-TYPE-MAPPING"', 
         '_artop_applicationRecordElementRef': '"APPLICATION-RECORD-ELEMENT"', 
         '_artop_complexTypeMapping': '"SENDER-REC-COMPOSITE-TYPE-MAPPING"', 
         '_artop_implementationRecordElementRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_systemSignalRef': '"SYSTEM-SIGNAL"'})

    @property
    def ref_senderRecRecordTypeMapping_(self):
        return self._artop_senderRecRecordTypeMapping

    @property
    def senderRecRecordTypeMapping_(self):
        if self._artop_senderRecRecordTypeMapping is not None:
            if hasattr(self._artop_senderRecRecordTypeMapping, "uuid"):
                return self._artop_senderRecRecordTypeMapping.uuid
        return

    @property
    def ref_applicationRecordElement_(self):
        return self._artop_applicationRecordElementRef

    @property
    def applicationRecordElement_(self):
        if self._artop_applicationRecordElementRef is not None:
            if hasattr(self._artop_applicationRecordElementRef, "uuid"):
                return self._artop_applicationRecordElementRef.uuid
        return

    @property
    def ref_complexTypeMapping_(self):
        return self._artop_complexTypeMapping

    @property
    def complexTypeMapping_(self):
        if self._artop_complexTypeMapping is not None:
            if hasattr(self._artop_complexTypeMapping, "uuid"):
                return self._artop_complexTypeMapping.uuid
        return

    @property
    def ref_implementationRecordElement_(self):
        return self._artop_implementationRecordElementRef

    @property
    def implementationRecordElement_(self):
        if self._artop_implementationRecordElementRef is not None:
            if hasattr(self._artop_implementationRecordElementRef, "uuid"):
                return self._artop_implementationRecordElementRef.uuid
        return

    @property
    def ref_systemSignal_(self):
        return self._artop_systemSignalRef

    @property
    def systemSignal_(self):
        if self._artop_systemSignalRef is not None:
            if hasattr(self._artop_systemSignalRef, "uuid"):
                return self._artop_systemSignalRef.uuid
        return
