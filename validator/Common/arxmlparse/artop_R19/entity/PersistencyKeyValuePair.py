# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyKeyValuePair.py
from .Identifiable import Identifiable

class PersistencyKeyValuePair(Identifiable):

    def __init__(self):
        super().__init__()
        from .PersistencyKeyValueDatabase import PersistencyKeyValueDatabase
        from .ValueSpecification import ValueSpecification
        from .AbstractImplementationDataType import AbstractImplementationDataType
        self._artop_updateStrategy = None
        self._artop_persistencyKeyValueDatabase = None
        self._artop_initValue = None
        self._artop_valueDataTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_persistencyKeyValueDatabase':"PERSISTENCY-KEY-VALUE-DATABASE", 
         '_artop_initValue':"VALUE-SPECIFICATION", 
         '_artop_valueDataTypeRef':"ABSTRACT-IMPLEMENTATION-DATA-TYPE"})

    @property
    def updateStrategy_(self):
        return self._artop_updateStrategy

    @property
    def ref_persistencyKeyValueDatabase_(self):
        return self._artop_persistencyKeyValueDatabase

    @property
    def persistencyKeyValueDatabase_(self):
        if self._artop_persistencyKeyValueDatabase is not None:
            if hasattr(self._artop_persistencyKeyValueDatabase, "uuid"):
                return self._artop_persistencyKeyValueDatabase.uuid
        return

    @property
    def ref_initValue_(self):
        return self._artop_initValue

    @property
    def initValue_(self):
        if self._artop_initValue is not None:
            if hasattr(self._artop_initValue, "uuid"):
                return self._artop_initValue.uuid
        return

    @property
    def ref_valueDataType_(self):
        return self._artop_valueDataTypeRef

    @property
    def valueDataType_(self):
        if self._artop_valueDataTypeRef is not None:
            if hasattr(self._artop_valueDataTypeRef, "uuid"):
                return self._artop_valueDataTypeRef.uuid
        return
