# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InitialSdDelayConfig.py
from .ARObject import ARObject

class InitialSdDelayConfig(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_initialDelayMaxValue = None
        self._artop_initialDelayMinValue = None
        self._artop_initialRepetitionsBaseDelay = None
        self._artop_initialRepetitionsMax = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def initialDelayMaxValue_(self):
        return self._artop_initialDelayMaxValue

    @property
    def initialDelayMinValue_(self):
        return self._artop_initialDelayMinValue

    @property
    def initialRepetitionsBaseDelay_(self):
        return self._artop_initialRepetitionsBaseDelay

    @property
    def initialRepetitionsMax_(self):
        return self._artop_initialRepetitionsMax
