# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RootSwCompositionPrototype.py
from .AtpPrototype import AtpPrototype

class RootSwCompositionPrototype(AtpPrototype):

    def __init__(self):
        super().__init__()
        from .System import System
        from .CalibrationParameterValueSet import CalibrationParameterValueSet
        from .FlatMap import FlatMap
        from .CompositionSwComponentType import CompositionSwComponentType
        from .VariationPoint import VariationPoint
        self._artop_system = None
        self._artop_calibrationParameterValueSetRef = []
        self._artop_flatMapRef = None
        self._artop_softwareCompositionTref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_system': '"SYSTEM"', 
         '_artop_calibrationParameterValueSetRef': '"CALIBRATION-PARAMETER-VALUE-SET"', 
         '_artop_flatMapRef': '"FLAT-MAP"', 
         '_artop_softwareCompositionTref': '"COMPOSITION-SW-COMPONENT-TYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_system_(self):
        return self._artop_system

    @property
    def system_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_calibrationParameterValueSets_(self):
        return self._artop_calibrationParameterValueSetRef

    @property
    def calibrationParameterValueSets_(self):
        return self._artop_calibrationParameterValueSetRef

    @property
    def ref_flatMap_(self):
        return self._artop_flatMapRef

    @property
    def flatMap_(self):
        if self._artop_flatMapRef is not None:
            if hasattr(self._artop_flatMapRef, "uuid"):
                return self._artop_flatMapRef.uuid
        return

    @property
    def ref_softwareComposition_(self):
        return self._artop_softwareCompositionTref

    @property
    def softwareComposition_(self):
        if self._artop_softwareCompositionTref is not None:
            if hasattr(self._artop_softwareCompositionTref, "uuid"):
                return self._artop_softwareCompositionTref.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
