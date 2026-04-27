# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyRedundancyHandling.py
from .ARObject import ARObject

class PersistencyRedundancyHandling(ARObject):

    def __init__(self):
        super().__init__()
        from .PersistencyDeployment import PersistencyDeployment
        self._artop_scope = None
        self._artop_persistencyDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_persistencyDeployment": "PERSISTENCY-DEPLOYMENT"})

    @property
    def scope_(self):
        return self._artop_scope

    @property
    def ref_persistencyDeployment_(self):
        return self._artop_persistencyDeployment

    @property
    def persistencyDeployment_(self):
        if self._artop_persistencyDeployment is not None:
            if hasattr(self._artop_persistencyDeployment, "uuid"):
                return self._artop_persistencyDeployment.uuid
        return
