# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwDataDependencyArgs.py
from .ARObject import ARObject

class SwDataDependencyArgs(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDependency import SwDataDependency
        from .SwCalprmRefProxy import SwCalprmRefProxy
        from .SwVariableRefProxy import SwVariableRefProxy
        self._artop_mixed = None
        self._artop_swDataDependency = None
        self._artop_swCalprmRef = []
        self._artop_swVariable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swDataDependency':"SW-DATA-DEPENDENCY", 
         '_artop_swCalprmRef':"SW-CALPRM-REF-PROXY", 
         '_artop_swVariable':"SW-VARIABLE-REF-PROXY"})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def ref_swDataDependency_(self):
        return self._artop_swDataDependency

    @property
    def swDataDependency_(self):
        if self._artop_swDataDependency is not None:
            if hasattr(self._artop_swDataDependency, "uuid"):
                return self._artop_swDataDependency.uuid
        return

    @property
    def swCalprmRefs_SwCalprmRefProxy(self):
        return self._artop_swCalprmRef

    @property
    def swVariables_SwVariableRefProxy(self):
        return self._artop_swVariable
