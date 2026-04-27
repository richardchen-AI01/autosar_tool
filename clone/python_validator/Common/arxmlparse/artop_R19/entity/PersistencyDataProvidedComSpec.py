# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyDataProvidedComSpec.py
from .PPortComSpec import PPortComSpec

class PersistencyDataProvidedComSpec(PPortComSpec):

    def __init__(self):
        super().__init__()
        from .PersistencyDataElement import PersistencyDataElement
        from .ValueSpecification import ValueSpecification
        self._artop_dataElementRef = None
        self._artop_initValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElementRef':"PERSISTENCY-DATA-ELEMENT", 
         '_artop_initValue':"VALUE-SPECIFICATION"})

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
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
