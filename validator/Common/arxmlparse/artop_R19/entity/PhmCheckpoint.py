# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmCheckpoint.py
from .AtpFeature import AtpFeature

class PhmCheckpoint(AtpFeature):

    def __init__(self):
        super().__init__()
        from .PhmSupervisedEntityInterface import PhmSupervisedEntityInterface
        self._artop_checkpointId = None
        self._artop_phmSupervisedEntityInterface = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_phmSupervisedEntityInterface": "PHM-SUPERVISED-ENTITY-INTERFACE"})

    @property
    def checkpointId_(self):
        return self._artop_checkpointId

    @property
    def ref_phmSupervisedEntityInterface_(self):
        return self._artop_phmSupervisedEntityInterface

    @property
    def phmSupervisedEntityInterface_(self):
        if self._artop_phmSupervisedEntityInterface is not None:
            if hasattr(self._artop_phmSupervisedEntityInterface, "uuid"):
                return self._artop_phmSupervisedEntityInterface.uuid
        return
