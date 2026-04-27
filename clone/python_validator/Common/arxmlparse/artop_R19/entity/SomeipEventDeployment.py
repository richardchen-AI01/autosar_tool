# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipEventDeployment.py
from .ServiceEventDeployment import ServiceEventDeployment

class SomeipEventDeployment(ServiceEventDeployment):

    def __init__(self):
        super().__init__()
        from .SomeipFieldDeployment import SomeipFieldDeployment
        self._artop_eventId = None
        self._artop_maximumSegmentLength = None
        self._artop_separationTime = None
        self._artop_serializer = None
        self._artop_transportProtocol = None
        self._artop_someipFieldDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_someipFieldDeployment": "SOMEIP-FIELD-DEPLOYMENT"})

    @property
    def eventId_(self):
        return self._artop_eventId

    @property
    def maximumSegmentLength_(self):
        return self._artop_maximumSegmentLength

    @property
    def separationTime_(self):
        return self._artop_separationTime

    @property
    def serializer_(self):
        return self._artop_serializer

    @property
    def transportProtocol_(self):
        return self._artop_transportProtocol

    @property
    def ref_someipFieldDeployment_(self):
        return self._artop_someipFieldDeployment

    @property
    def someipFieldDeployment_(self):
        if self._artop_someipFieldDeployment is not None:
            if hasattr(self._artop_someipFieldDeployment, "uuid"):
                return self._artop_someipFieldDeployment.uuid
        return
