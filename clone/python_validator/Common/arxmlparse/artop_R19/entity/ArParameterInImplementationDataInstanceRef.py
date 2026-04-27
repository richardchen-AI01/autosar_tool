# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ArParameterInImplementationDataInstanceRef.py
from .ARObject import ARObject

class ArParameterInImplementationDataInstanceRef(ARObject):

    def __init__(self):
        super().__init__()
        from .ImplementationDataTypeSubElementRef import ImplementationDataTypeSubElementRef
        from .ImplementationDataTypeElement import ImplementationDataTypeElement
        from .PortPrototype import PortPrototype
        from .ParameterDataPrototype import ParameterDataPrototype
        self._artop_implementationDataTypeSubElementRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_portPrototypeRef = None
        self._artop_rootParameterDataPrototypeRef = None
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_implementationDataTypeSubElementRef': '"IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF"', 
         '_artop_contextDataPrototypeRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"', 
         '_artop_portPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_rootParameterDataPrototypeRef': '"PARAMETER-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"IMPLEMENTATION-DATA-TYPE-ELEMENT"'})

    @property
    def ref_implementationDataTypeSubElementRef_(self):
        return self._artop_implementationDataTypeSubElementRef

    @property
    def implementationDataTypeSubElementRef_(self):
        if self._artop_implementationDataTypeSubElementRef is not None:
            if hasattr(self._artop_implementationDataTypeSubElementRef, "uuid"):
                return self._artop_implementationDataTypeSubElementRef.uuid
        return

    @property
    def ref_contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototypeRef

    @property
    def portPrototype_(self):
        if self._artop_portPrototypeRef is not None:
            if hasattr(self._artop_portPrototypeRef, "uuid"):
                return self._artop_portPrototypeRef.uuid
        return

    @property
    def ref_rootParameterDataPrototype_(self):
        return self._artop_rootParameterDataPrototypeRef

    @property
    def rootParameterDataPrototype_(self):
        if self._artop_rootParameterDataPrototypeRef is not None:
            if hasattr(self._artop_rootParameterDataPrototypeRef, "uuid"):
                return self._artop_rootParameterDataPrototypeRef.uuid
        return

    @property
    def ref_targetDataPrototype_(self):
        return self._artop_targetDataPrototypeRef

    @property
    def targetDataPrototype_(self):
        if self._artop_targetDataPrototypeRef is not None:
            if hasattr(self._artop_targetDataPrototypeRef, "uuid"):
                return self._artop_targetDataPrototypeRef.uuid
        return
