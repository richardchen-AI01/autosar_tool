# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ParameterInAtomicSWCTypeInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .AutosarParameterRef import AutosarParameterRef
        from .AtomicSwComponentType import AtomicSwComponentType
        from .PortPrototype import PortPrototype
        from .DataPrototype import DataPrototype
        from .ApplicationCompositeElementDataPrototype import ApplicationCompositeElementDataPrototype
        self._artop_autosarParameterRef = None
        self._artop_atomicSwComponentType = None
        self._artop_portPrototypeRef = None
        self._artop_rootParameterDataPrototypeRef = None
        self._artop_contextDataPrototypeRef = []
        self._artop_targetDataPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_autosarParameterRef': '"AUTOSAR-PARAMETER-REF"', 
         '_artop_atomicSwComponentType': '"ATOMIC-SW-COMPONENT-TYPE"', 
         '_artop_portPrototypeRef': '"PORT-PROTOTYPE"', 
         '_artop_rootParameterDataPrototypeRef': '"DATA-PROTOTYPE"', 
         '_artop_contextDataPrototypeRef': '"APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"', 
         '_artop_targetDataPrototypeRef': '"DATA-PROTOTYPE"'})

    @property
    def ref_autosarParameterRef_(self):
        return self._artop_autosarParameterRef

    @property
    def autosarParameterRef_(self):
        if self._artop_autosarParameterRef is not None:
            if hasattr(self._artop_autosarParameterRef, "uuid"):
                return self._artop_autosarParameterRef.uuid
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
    def ref_rootParameterDataPrototype_(self):
        return self._artop_rootParameterDataPrototypeRef

    @property
    def rootParameterDataPrototype_(self):
        if self._artop_rootParameterDataPrototypeRef is not None:
            if hasattr(self._artop_rootParameterDataPrototypeRef, "uuid"):
                return self._artop_rootParameterDataPrototypeRef.uuid
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
