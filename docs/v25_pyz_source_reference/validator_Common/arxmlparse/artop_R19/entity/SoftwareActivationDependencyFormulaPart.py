# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareActivationDependencyFormulaPart.py
from .ARObject import ARObject

class SoftwareActivationDependencyFormulaPart(ARObject):

    def __init__(self):
        super().__init__()
        from .SoftwareActivationDependencyFormula import SoftwareActivationDependencyFormula
        self._artop_softwareActivationDependencyFormula = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_softwareActivationDependencyFormula": "SOFTWARE-ACTIVATION-DEPENDENCY-FORMULA"})

    @property
    def ref_softwareActivationDependencyFormula_(self):
        return self._artop_softwareActivationDependencyFormula

    @property
    def softwareActivationDependencyFormula_(self):
        if self._artop_softwareActivationDependencyFormula is not None:
            if hasattr(self._artop_softwareActivationDependencyFormula, "uuid"):
                return self._artop_softwareActivationDependencyFormula.uuid
        return
