# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AtpBlueprint.py
from .Identifiable import Identifiable

class AtpBlueprint(Identifiable):

    def __init__(self):
        super().__init__()
        from .BlueprintPolicy import BlueprintPolicy
        self._artop_shortNamePattern = None
        self._artop_blueprintPolicy = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_blueprintPolicy": "BLUEPRINT-POLICY"})

    @property
    def shortNamePattern_(self):
        return self._artop_shortNamePattern

    @property
    def blueprintPolicies_BlueprintPolicy(self):
        return self._artop_blueprintPolicy
