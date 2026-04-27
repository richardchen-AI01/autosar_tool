# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwDataDependency.py
from .ARObject import ARObject

class SwDataDependency(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsContent import SwDataDefPropsContent
        from .CompuGenericMath import CompuGenericMath
        from .SwDataDependencyArgs import SwDataDependencyArgs
        self._artop_swDataDefPropsContent = None
        self._artop_swDataDependencyFormula = None
        self._artop_swDataDependencyArgs = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swDataDefPropsContent':"SW-DATA-DEF-PROPS-CONTENT", 
         '_artop_swDataDependencyFormula':"COMPU-GENERIC-MATH", 
         '_artop_swDataDependencyArgs':"SW-DATA-DEPENDENCY-ARGS"})

    @property
    def ref_swDataDefPropsContent_(self):
        return self._artop_swDataDefPropsContent

    @property
    def swDataDefPropsContent_(self):
        if self._artop_swDataDefPropsContent is not None:
            if hasattr(self._artop_swDataDefPropsContent, "uuid"):
                return self._artop_swDataDefPropsContent.uuid
        return

    @property
    def ref_swDataDependencyFormula_(self):
        return self._artop_swDataDependencyFormula

    @property
    def swDataDependencyFormula_(self):
        if self._artop_swDataDependencyFormula is not None:
            if hasattr(self._artop_swDataDependencyFormula, "uuid"):
                return self._artop_swDataDependencyFormula.uuid
        return

    @property
    def ref_swDataDependencyArgs_(self):
        return self._artop_swDataDependencyArgs

    @property
    def swDataDependencyArgs_(self):
        if self._artop_swDataDependencyArgs is not None:
            if hasattr(self._artop_swDataDependencyArgs, "uuid"):
                return self._artop_swDataDependencyArgs.uuid
        return
