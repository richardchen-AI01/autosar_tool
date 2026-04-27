# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RestAbstractNumericalPropertyDef.py
from .RestPrimitivePropertyDef import RestPrimitivePropertyDef

class RestAbstractNumericalPropertyDef(RestPrimitivePropertyDef):

    def __init__(self):
        super().__init__()
        self._artop_lowerLimit = None
        self._artop_resolution = None
        self._artop_unit = None
        self._artop_upperLimit = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def lowerLimit_(self):
        return self._artop_lowerLimit

    @property
    def resolution_(self):
        if self._artop_resolution:
            return float(self._artop_resolution)
        return self._artop_resolution

    @property
    def unit_(self):
        return self._artop_unit

    @property
    def upperLimit_(self):
        return self._artop_upperLimit
