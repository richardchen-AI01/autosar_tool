# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyKeyValueDatabaseInterface.py
from .PersistencyInterface import PersistencyInterface

class PersistencyKeyValueDatabaseInterface(PersistencyInterface):

    def __init__(self):
        super().__init__()
        from .PersistencyDataElement import PersistencyDataElement
        from .AbstractImplementationDataType import AbstractImplementationDataType
        self._artop_dataElement = []
        self._artop_dataTypeForSerializationRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElement':"PERSISTENCY-DATA-ELEMENT", 
         '_artop_dataTypeForSerializationRef':"ABSTRACT-IMPLEMENTATION-DATA-TYPE"})

    @property
    def dataElements_PersistencyDataElement(self):
        return self._artop_dataElement

    @property
    def ref_dataTypeForSerializations_(self):
        return self._artop_dataTypeForSerializationRef

    @property
    def dataTypeForSerializations_(self):
        return self._artop_dataTypeForSerializationRef
