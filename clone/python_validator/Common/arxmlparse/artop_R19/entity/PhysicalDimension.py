# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhysicalDimension.py
from .ARElement import ARElement

class PhysicalDimension(ARElement):

    def __init__(self):
        super().__init__()
        self._artop_lengthExp = None
        self._artop_massExp = None
        self._artop_timeExp = None
        self._artop_currentExp = None
        self._artop_temperatureExp = None
        self._artop_molarAmountExp = None
        self._artop_luminousIntensityExp = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def lengthExp_(self):
        return self._artop_lengthExp

    @property
    def massExp_(self):
        return self._artop_massExp

    @property
    def timeExp_(self):
        return self._artop_timeExp

    @property
    def currentExp_(self):
        return self._artop_currentExp

    @property
    def temperatureExp_(self):
        return self._artop_temperatureExp

    @property
    def molarAmountExp_(self):
        return self._artop_molarAmountExp

    @property
    def luminousIntensityExp_(self):
        return self._artop_luminousIntensityExp
