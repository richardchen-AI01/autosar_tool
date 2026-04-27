# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ImplementationDataTypeElementInPortInterfaceRef.py
from .DataPrototypeReference import DataPrototypeReference

class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):

    def __init__(self):
        super().__init__()
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        self._artop_rootDataPrototypeRef = None
        self._artop_contextImplementationDataElementRef = []
        self._artop_targetImplementationDataTypeElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_rootDataPrototypeRef':"AUTOSAR-DATA-PROTOTYPE", 
         '_artop_contextImplementationDataElementRef':"IMPLEMENTATION-DATA-TYPE-ELEMENT", 
         '_artop_targetImplementationDataTypeElementRef':"IMPLEMENTATION-DATA-TYPE-ELEMENT"})

    @property
    def ref_rootDataPrototype_(self):
        return self._artop_rootDataPrototypeRef

    @property
    def rootDataPrototype_(self):
        if self._artop_rootDataPrototypeRef is not None:
            if hasattr(self._artop_rootDataPrototypeRef, "uuid"):
                return self._artop_rootDataPrototypeRef.uuid
        return

    @property
    def ref_contextImplementationDataElements_(self):
        return self._artop_contextImplementationDataElementRef

    @property
    def contextImplementationDataElements_(self):
        return self._artop_contextImplementationDataElementRef

    @property
    def ref_targetImplementationDataTypeElement_(self):
        return self._artop_targetImplementationDataTypeElementRef

    @property
    def targetImplementationDataTypeElement_(self):
        if self._artop_targetImplementationDataTypeElementRef is not None:
            if hasattr(self._artop_targetImplementationDataTypeElementRef, "uuid"):
                return self._artop_targetImplementationDataTypeElementRef.uuid
        return
