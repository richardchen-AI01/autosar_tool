# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Unit.py
from .ARElement import ARElement

class Unit(ARElement):

    def __init__(self):
        super().__init__()
        from .SingleLanguageUnitNames import SingleLanguageUnitNames
        from .PhysicalDimension import PhysicalDimension
        self._artop_factorSiToUnit = None
        self._artop_offsetSiToUnit = None
        self._artop_displayName = None
        self._artop_physicalDimensionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_displayName':"SINGLE-LANGUAGE-UNIT-NAMES", 
         '_artop_physicalDimensionRef':"PHYSICAL-DIMENSION"})

    @property
    def factorSiToUnit_(self):
        if self._artop_factorSiToUnit:
            return float(self._artop_factorSiToUnit)
        return self._artop_factorSiToUnit

    @property
    def offsetSiToUnit_(self):
        if self._artop_offsetSiToUnit:
            return float(self._artop_offsetSiToUnit)
        return self._artop_offsetSiToUnit

    @property
    def ref_displayName_(self):
        return self._artop_displayName

    @property
    def displayName_(self):
        if self._artop_displayName is not None:
            if hasattr(self._artop_displayName, "uuid"):
                return self._artop_displayName.uuid
        return

    @property
    def ref_physicalDimension_(self):
        return self._artop_physicalDimensionRef

    @property
    def physicalDimension_(self):
        if self._artop_physicalDimensionRef is not None:
            if hasattr(self._artop_physicalDimensionRef, "uuid"):
                return self._artop_physicalDimensionRef.uuid
        return
