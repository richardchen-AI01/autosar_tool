# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintPolicyModifiable.py
from .BlueprintPolicy import BlueprintPolicy

class BlueprintPolicyModifiable(BlueprintPolicy):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        self._artop_blueprintDerivationGuide = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_blueprintDerivationGuide": "DOCUMENTATION-BLOCK"})

    @property
    def ref_blueprintDerivationGuide_(self):
        return self._artop_blueprintDerivationGuide

    @property
    def blueprintDerivationGuide_(self):
        if self._artop_blueprintDerivationGuide is not None:
            if hasattr(self._artop_blueprintDerivationGuide, "uuid"):
                return self._artop_blueprintDerivationGuide.uuid
        return
