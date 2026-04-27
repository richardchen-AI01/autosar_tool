# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipMethodDeployment.py
from .ServiceMethodDeployment import ServiceMethodDeployment

class SomeipMethodDeployment(ServiceMethodDeployment):

    def __init__(self):
        super().__init__()
        self._artop_maximumSegmentLengthRequest = None
        self._artop_maximumSegmentLengthResponse = None
        self._artop_methodId = None
        self._artop_separationTimeRequest = None
        self._artop_separationTimeResponse = None
        self._artop_transportProtocol = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def maximumSegmentLengthRequest_(self):
        return self._artop_maximumSegmentLengthRequest

    @property
    def maximumSegmentLengthResponse_(self):
        return self._artop_maximumSegmentLengthResponse

    @property
    def methodId_(self):
        return self._artop_methodId

    @property
    def separationTimeRequest_(self):
        return self._artop_separationTimeRequest

    @property
    def separationTimeResponse_(self):
        return self._artop_separationTimeResponse

    @property
    def transportProtocol_(self):
        return self._artop_transportProtocol
