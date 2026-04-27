# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AutosarParameterRef.py
from .ARObject import ARObject

class AutosarParameterRef(ARObject):

    def __init__(self):
        super().__init__()
        from .ParameterInAtomicSWCTypeInstanceRef import ParameterInAtomicSWCTypeInstanceRef
        from .DataPrototype import DataPrototype
        self._artop_autosarParameterIref = None
        self._artop_localParameterRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_autosarParameterIref':"PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF-IREF", 
         '_artop_localParameterRef':"DATA-PROTOTYPE"})

    @property
    def ref_autosarParameter_(self):
        return self._artop_autosarParameterIref

    @property
    def autosarParameter_(self):
        if self._artop_autosarParameterIref is not None:
            if hasattr(self._artop_autosarParameterIref, "uuid"):
                return self._artop_autosarParameterIref.uuid
        return

    @property
    def ref_localParameter_(self):
        return self._artop_localParameterRef

    @property
    def localParameter_(self):
        if self._artop_localParameterRef is not None:
            if hasattr(self._artop_localParameterRef, "uuid"):
                return self._artop_localParameterRef.uuid
        return
