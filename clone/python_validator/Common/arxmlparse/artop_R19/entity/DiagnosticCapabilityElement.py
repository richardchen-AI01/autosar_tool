# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticCapabilityElement.py
from .ServiceNeeds import ServiceNeeds

class DiagnosticCapabilityElement(ServiceNeeds):

    def __init__(self):
        super().__init__()
        self._artop_audience = None
        self._artop_diagRequirement = None
        self._artop_securityAccessLevel = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def audience_(self):
        return self._artop_audience

    @property
    def diagRequirement_(self):
        return self._artop_diagRequirement

    @property
    def securityAccessLevel_(self):
        return self._artop_securityAccessLevel
