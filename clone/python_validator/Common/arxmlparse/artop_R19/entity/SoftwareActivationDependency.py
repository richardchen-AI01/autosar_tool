# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareActivationDependency.py
from .ARElement import ARElement

class SoftwareActivationDependency(ARElement):

    def __init__(self):
        super().__init__()
        from .SoftwareActivationDependencyFormula import SoftwareActivationDependencyFormula
        self._artop_conflictsTo = None
        self._artop_dependsOn = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_conflictsTo':"SOFTWARE-ACTIVATION-DEPENDENCY-FORMULA", 
         '_artop_dependsOn':"SOFTWARE-ACTIVATION-DEPENDENCY-FORMULA"})

    @property
    def ref_conflictsTo_(self):
        return self._artop_conflictsTo

    @property
    def conflictsTo_(self):
        if self._artop_conflictsTo is not None:
            if hasattr(self._artop_conflictsTo, "uuid"):
                return self._artop_conflictsTo.uuid
        return

    @property
    def ref_dependsOn_(self):
        return self._artop_dependsOn

    @property
    def dependsOn_(self):
        if self._artop_dependsOn is not None:
            if hasattr(self._artop_dependsOn, "uuid"):
                return self._artop_dependsOn.uuid
        return
