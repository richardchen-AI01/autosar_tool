# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PostBuildVariantCriterion.py
from .AtpDefinition import AtpDefinition
from .ARElement import ARElement

class PostBuildVariantCriterion(ARElement, AtpDefinition):

    def __init__(self):
        super().__init__()
        from .CompuMethod import CompuMethod
        self._artop_compuMethodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compuMethodRef": "COMPU-METHOD"})

    @property
    def ref_compuMethod_(self):
        return self._artop_compuMethodRef

    @property
    def compuMethod_(self):
        if self._artop_compuMethodRef is not None:
            if hasattr(self._artop_compuMethodRef, "uuid"):
                return self._artop_compuMethodRef.uuid
        return
