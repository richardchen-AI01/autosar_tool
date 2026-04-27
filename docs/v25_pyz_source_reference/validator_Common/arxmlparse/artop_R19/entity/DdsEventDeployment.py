# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsEventDeployment.py
from .ServiceEventDeployment import ServiceEventDeployment

class DdsEventDeployment(ServiceEventDeployment):

    def __init__(self):
        super().__init__()
        from .DdsFieldDeployment import DdsFieldDeployment
        self._artop_topicName = None
        self._artop_transportProtocol = None
        self._artop_ddsFieldDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ddsFieldDeployment": "DDS-FIELD-DEPLOYMENT"})

    @property
    def topicName_(self):
        return self._artop_topicName

    @property
    def transportProtocol_(self):
        return self._artop_transportProtocol

    @property
    def ref_ddsFieldDeployment_(self):
        return self._artop_ddsFieldDeployment

    @property
    def ddsFieldDeployment_(self):
        if self._artop_ddsFieldDeployment is not None:
            if hasattr(self._artop_ddsFieldDeployment, "uuid"):
                return self._artop_ddsFieldDeployment.uuid
        return
