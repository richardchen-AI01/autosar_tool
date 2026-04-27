# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VariableInAtomicSWCTypeInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AutosarVariableRef import AutosarVariableRef
        from .AtomicSwComponentType import AtomicSwComponentType
        from .PortPrototype import PortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        from .DataPrototype import DataPrototype
        self._artop_autosarVariableRef = None
        self._artop_atomicSwComponentType = None
        self._artop_portPrototypeRef = None
        self._artop_rootVariableDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_autosarVariableRef': '"AUTOSAR-VARIABLE-REF"', 
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"', 
         '_artop_portPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_rootVariableDataPrototypeRef': '"VARIABLE-DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_autosarVariableRef_(self):
        return self._artop_autosarVariableRef

    @property
    def autosarVariableRef_(self):
        if self._artop_autosarVariableRef is not None:
            if hasattr(self._artop_autosarVariableRef, "uuid"):
                return self._artop_autosarVariableRef.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_atomicSwComponentType

    @property
    def base_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return

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
    def ref_rootVariableDataPrototype_(self):
        return self._artop_rootVariableDataPrototypeRef

    @property
    def rootVariableDataPrototype_(self):
        if self._artop_rootVariableDataPrototypeRef is not None:
            if hasattr(self._artop_rootVariableDataPrototypeRef, "uuid"):
                return self._artop_rootVariableDataPrototypeRef.uuid
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
