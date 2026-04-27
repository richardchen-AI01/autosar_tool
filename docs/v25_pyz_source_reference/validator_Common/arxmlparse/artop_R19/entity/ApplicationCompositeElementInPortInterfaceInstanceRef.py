# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationCompositeElementInPortInterfaceInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ApplicationCompositeElementInPortInterfaceInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DataInterface import DataInterface
        from .AutosarDataPrototype import AutosarDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        self._artop_dataInterface = None
        self._artop_rootDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataInterface': '"DATA-INTERFACE"', 
         '_artop_rootDataPrototypeRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"'})

    @property
    def ref_base_(self):
        return self._artop_dataInterface

    @property
    def base_(self):
        if self._artop_dataInterface is not None:
            if hasattr(self._artop_dataInterface, "uuid"):
                return self._artop_dataInterface.uuid
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
    def ref_contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def contextDataPrototypes_(self):
        return self._artop_contextDataPrototypeRef

    @property
    def ref_targetDataPrototype_(self):
        return self._artop_targetDataPrototypeRef

    @property
    def targetDataPrototype_(self):
        if self._artop_targetDataPrototypeRef is not None:
            if hasattr(self._artop_targetDataPrototypeRef, "uuid"):
                return self._artop_targetDataPrototypeRef.uuid
        return
