# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInClientServerInterfaceInstanceRef.py
from .DataPrototypeInPortInterfaceInstanceRef import DataPrototypeInPortInterfaceInstanceRef

class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):

    def __init__(self):
        super().__init__()
        from .ClientServerInterface import ClientServerInterface
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_clientServerInterface = None
        self._artop_rootDataPrototypeInCsRef = None
        self._artop_contextDataPrototypeInCsRef = []
        self._artop_targetDataPrototypeInCsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_clientServerInterface': '"CLIENT-SERVER-INTERFACE"', 
         '_artop_rootDataPrototypeInCsRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeInCsRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeInCsRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_base_(self):
        return self._artop_clientServerInterface

    @property
    def base_(self):
        if self._artop_clientServerInterface is not None:
            if hasattr(self._artop_clientServerInterface, "uuid"):
                return self._artop_clientServerInterface.uuid
        return

    @property
    def ref_rootDataPrototypeInCs_(self):
        return self._artop_rootDataPrototypeInCsRef

    @property
    def rootDataPrototypeInCs_(self):
        if self._artop_rootDataPrototypeInCsRef is not None:
            if hasattr(self._artop_rootDataPrototypeInCsRef, "uuid"):
                return self._artop_rootDataPrototypeInCsRef.uuid
        return

    @property
    def ref_contextDataPrototypeInCs_(self):
        return self._artop_contextDataPrototypeInCsRef

    @property
    def contextDataPrototypeInCs_(self):
        return self._artop_contextDataPrototypeInCsRef

    @property
    def ref_targetDataPrototypeInCs_(self):
        return self._artop_targetDataPrototypeInCsRef

    @property
    def targetDataPrototypeInCs_(self):
        if self._artop_targetDataPrototypeInCsRef is not None:
            if hasattr(self._artop_targetDataPrototypeInCsRef, "uuid"):
                return self._artop_targetDataPrototypeInCsRef.uuid
        return
