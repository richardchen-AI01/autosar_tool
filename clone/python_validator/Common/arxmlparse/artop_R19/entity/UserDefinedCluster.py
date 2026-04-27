# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UserDefinedCluster.py
from .CommunicationCluster import CommunicationCluster

class UserDefinedCluster(CommunicationCluster):

    def __init__(self):
        super().__init__()
        from .UserDefinedClusterConditional import UserDefinedClusterConditional
        self._artop_userDefinedClusterVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_userDefinedClusterVariant": "USER-DEFINED-CLUSTER-CONDITIONAL"})

    @property
    def UserDefinedClusterVariants_UserDefinedClusterConditional(self):
        return self._artop_userDefinedClusterVariant
