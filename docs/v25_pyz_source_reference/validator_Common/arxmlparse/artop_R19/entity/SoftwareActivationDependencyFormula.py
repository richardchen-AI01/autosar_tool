# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareActivationDependencyFormula.py
from .SoftwareActivationDependencyFormulaPart import SoftwareActivationDependencyFormulaPart

class SoftwareActivationDependencyFormula(SoftwareActivationDependencyFormulaPart):

    def __init__(self):
        super().__init__()
        from .SoftwareActivationDependencyFormulaPart import SoftwareActivationDependencyFormulaPart
        self._artop_operator = None
        self._artop_part = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_part": "SOFTWARE-ACTIVATION-DEPENDENCY-FORMULA-PART"})

    @property
    def operator_(self):
        return self._artop_operator

    @property
    def parts_SoftwareActivationDependencyFormulaPart(self):
        return self._artop_part
