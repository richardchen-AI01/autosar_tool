# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AutosarVariableRef.py
from .ARObject import ARObject

class AutosarVariableRef(ARObject):

    def __init__(self):
        super().__init__()
        from .ArVariableInImplementationDataInstanceRef import ArVariableInImplementationDataInstanceRef
        from .VariableInAtomicSWCTypeInstanceRef import VariableInAtomicSWCTypeInstanceRef
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_autosarVariableInImplDatatype = None
        self._artop_autosarVariableIref = None
        self._artop_localVariableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_autosarVariableInImplDatatype':"AR-VARIABLE-IN-IMPLEMENTATION-DATA-INSTANCE-REF", 
         '_artop_autosarVariableIref':"VARIABLE-IN-ATOMIC-SWC-TYPE-INSTANCE-REF-IREF", 
         '_artop_localVariableRef':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def ref_autosarVariableInImplDatatype_(self):
        return self._artop_autosarVariableInImplDatatype

    @property
    def autosarVariableInImplDatatype_(self):
        if self._artop_autosarVariableInImplDatatype is not None:
            if hasattr(self._artop_autosarVariableInImplDatatype, "uuid"):
                return self._artop_autosarVariableInImplDatatype.uuid
        return

    @property
    def ref_autosarVariable_(self):
        return self._artop_autosarVariableIref

    @property
    def autosarVariable_(self):
        if self._artop_autosarVariableIref is not None:
            if hasattr(self._artop_autosarVariableIref, "uuid"):
                return self._artop_autosarVariableIref.uuid
        return

    @property
    def ref_localVariable_(self):
        return self._artop_localVariableRef

    @property
    def localVariable_(self):
        if self._artop_localVariableRef is not None:
            if hasattr(self._artop_localVariableRef, "uuid"):
                return self._artop_localVariableRef.uuid
        return
