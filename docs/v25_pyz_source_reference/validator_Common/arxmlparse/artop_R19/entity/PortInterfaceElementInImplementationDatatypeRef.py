# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortInterfaceElementInImplementationDatatypeRef.py
from .ARObject import ARObject

class PortInterfaceElementInImplementationDatatypeRef(ARObject):

    def __init__(self):
        super().__init__()
        from .DataPrototypeInServiceInterfaceRef import DataPrototypeInServiceInterfaceRef
        from .CppImplementationDataTypeContextTarget import CppImplementationDataTypeContextTarget
        from .PortInterface import PortInterface
        from .AutosarDataPrototype import AutosarDataPrototype
        self._artop_dataPrototypeInServiceInterfaceRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_portInterfaceRef = None
        self._artop_rootDataPrototypeRef = None
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataPrototypeInServiceInterfaceRef': '"DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF"', 
         '_artop_contextDataPrototypeRef': '"CPP-IMPLEMENTATION-DATA-TYPE-CONTEXT-TARGET"', 
         '_artop_portInterfaceRef': '"PORT-INTERFACE"', 
         '_artop_rootDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"CPP-IMPLEMENTATION-DATA-TYPE-CONTEXT-TARGET"'})

    @property
    def ref_dataPrototypeInServiceInterfaceRef_(self):
        return self._artop_dataPrototypeInServiceInterfaceRef

    @property
    def dataPrototypeInServiceInterfaceRef_(self):
        if self._artop_dataPrototypeInServiceInterfaceRef is not None:
            if hasattr(self._artop_dataPrototypeInServiceInterfaceRef, "uuid"):
                return self._artop_dataPrototypeInServiceInterfaceRef.uuid
        return

    @property
    def ref_contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def ref_portInterface_(self):
        return self._artop_portInterfaceRef

    @property
    def portInterface_(self):
        if self._artop_portInterfaceRef is not None:
            if hasattr(self._artop_portInterfaceRef, "uuid"):
                return self._artop_portInterfaceRef.uuid
        return

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
    def ref_targetDataPrototype_(self):
        return self._artop_targetDataPrototypeRef

    @property
    def targetDataPrototype_(self):
        if self._artop_targetDataPrototypeRef is not None:
            if hasattr(self._artop_targetDataPrototypeRef, "uuid"):
                return self._artop_targetDataPrototypeRef.uuid
        return
