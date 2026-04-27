# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsRpcServiceDeployment.py
from .Identifiable import Identifiable

class DdsRpcServiceDeployment(Identifiable):

    def __init__(self):
        super().__init__()
        from .DdsServiceInterfaceDeployment import DdsServiceInterfaceDeployment
        self._artop_replyTopicName = None
        self._artop_requestTopicName = None
        self._artop_ddsServiceInterfaceDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ddsServiceInterfaceDeployment": "DDS-SERVICE-INTERFACE-DEPLOYMENT"})

    @property
    def replyTopicName_(self):
        return self._artop_replyTopicName

    @property
    def requestTopicName_(self):
        return self._artop_requestTopicName

    @property
    def ref_ddsServiceInterfaceDeployment_(self):
        return self._artop_ddsServiceInterfaceDeployment

    @property
    def ddsServiceInterfaceDeployment_(self):
        if self._artop_ddsServiceInterfaceDeployment is not None:
            if hasattr(self._artop_ddsServiceInterfaceDeployment, "uuid"):
                return self._artop_ddsServiceInterfaceDeployment.uuid
        return
