# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SenderReceiverCompositeElementToSignalMapping.py
from .DataMapping import DataMapping

class SenderReceiverCompositeElementToSignalMapping(DataMapping):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototypeInSystemInstanceRef import VariableDataPrototypeInSystemInstanceRef
        from .SystemSignal import SystemSignal
        from .SenderRecCompositeTypeMapping import SenderRecCompositeTypeMapping
        self._artop_dataElementIref = None
        self._artop_systemSignalRef = None
        self._artop_typeMapping = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElementIref':"VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF", 
         '_artop_systemSignalRef':"SYSTEM-SIGNAL", 
         '_artop_typeMapping':"SENDER-REC-COMPOSITE-TYPE-MAPPING"})

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementIref

    @property
    def dataElement_(self):
        if self._artop_dataElementIref is not None:
            if hasattr(self._artop_dataElementIref, "uuid"):
                return self._artop_dataElementIref.uuid
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

    @property
    def ref_typeMapping_(self):
        return self._artop_typeMapping

    @property
    def typeMapping_(self):
        if self._artop_typeMapping is not None:
            if hasattr(self._artop_typeMapping, "uuid"):
                return self._artop_typeMapping.uuid
        return
