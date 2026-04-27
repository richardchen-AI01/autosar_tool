# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TlvDataIdDefinition.py
from .ARObject import ARObject

class TlvDataIdDefinition(ARObject):

    def __init__(self):
        super().__init__()
        from .ArgumentDataPrototype import ArgumentDataPrototype
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        from .ApplicationRecordElement import ApplicationRecordElement
        from .CppImplementationDataTypeElement import CppImplementationDataTypeElement
        self._artop_id = None
        self._artop_tlvArgumentRef = None
        self._artop_tlvImplementationDataTypeElementRef = None
        self._artop_tlvRecordElementRef = None
        self._artop_tlvSubElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_tlvArgumentRef': '"ARGUMENT-DATA-PROTOTYPE"', 
         '_artop_tlvImplementationDataTypeElementRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_tlvRecordElementRef': '"APPLICATION-RECORD-ELEMENT"', 
         '_artop_tlvSubElementRef': '"CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT"'})

    @property
    def id_(self):
        return self._artop_id

    @property
    def ref_tlvArgument_(self):
        return self._artop_tlvArgumentRef

    @property
    def tlvArgument_(self):
        if self._artop_tlvArgumentRef is not None:
            if hasattr(self._artop_tlvArgumentRef, "uuid"):
                return self._artop_tlvArgumentRef.uuid
        return

    @property
    def ref_tlvImplementationDataTypeElement_(self):
        return self._artop_tlvImplementationDataTypeElementRef

    @property
    def tlvImplementationDataTypeElement_(self):
        if self._artop_tlvImplementationDataTypeElementRef is not None:
            if hasattr(self._artop_tlvImplementationDataTypeElementRef, "uuid"):
                return self._artop_tlvImplementationDataTypeElementRef.uuid
        return

    @property
    def ref_tlvRecordElement_(self):
        return self._artop_tlvRecordElementRef

    @property
    def tlvRecordElement_(self):
        if self._artop_tlvRecordElementRef is not None:
            if hasattr(self._artop_tlvRecordElementRef, "uuid"):
                return self._artop_tlvRecordElementRef.uuid
        return

    @property
    def ref_tlvSubElement_(self):
        return self._artop_tlvSubElementRef

    @property
    def tlvSubElement_(self):
        if self._artop_tlvSubElementRef is not None:
            if hasattr(self._artop_tlvSubElementRef, "uuid"):
                return self._artop_tlvSubElementRef.uuid
        return
