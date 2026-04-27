# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionEntity.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint

class BuildActionEntity(AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .AutosarEngineeringObject import AutosarEngineeringObject
        from .BuildActionInvocator import BuildActionInvocator
        self._artop_deliveryArtifact = []
        self._artop_invocation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_deliveryArtifact':"AUTOSAR-ENGINEERING-OBJECT", 
         '_artop_invocation':"BUILD-ACTION-INVOCATOR"})

    @property
    def deliveryArtifacts_AutosarEngineeringObject(self):
        return self._artop_deliveryArtifact

    @property
    def ref_invocation_(self):
        return self._artop_invocation

    @property
    def invocation_(self):
        if self._artop_invocation is not None:
            if hasattr(self._artop_invocation, "uuid"):
                return self._artop_invocation.uuid
        return
