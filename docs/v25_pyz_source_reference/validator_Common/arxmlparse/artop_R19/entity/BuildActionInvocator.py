# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionInvocator.py
from .ARObject import ARObject

class BuildActionInvocator(ARObject):

    def __init__(self):
        super().__init__()
        from .BuildActionEntity import BuildActionEntity
        from .Sdg import Sdg
        self._artop_command = None
        self._artop_buildActionEntity = None
        self._artop_sdg = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_buildActionEntity':"BUILD-ACTION-ENTITY", 
         '_artop_sdg':"SDG"})

    @property
    def command_(self):
        return self._artop_command

    @property
    def ref_buildActionEntity_(self):
        return self._artop_buildActionEntity

    @property
    def buildActionEntity_(self):
        if self._artop_buildActionEntity is not None:
            if hasattr(self._artop_buildActionEntity, "uuid"):
                return self._artop_buildActionEntity.uuid
        return

    @property
    def sdgs_Sdg(self):
        return self._artop_sdg
