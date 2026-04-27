# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CalibrationParameterValue.py
from .ARObject import ARObject

class CalibrationParameterValue(ARObject):

    def __init__(self):
        super().__init__()
        from .CalibrationParameterValueSet import CalibrationParameterValueSet
        from .ValueSpecification import ValueSpecification
        from .FlatInstanceDescriptor import FlatInstanceDescriptor
        from .VariationPoint import VariationPoint
        self._artop_calibrationParameterValueSet = None
        self._artop_applInitValue = None
        self._artop_implInitValue = None
        self._artop_initializedParameterRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_calibrationParameterValueSet': '"CALIBRATION-PARAMETER-VALUE-SET"', 
         '_artop_applInitValue': '"VALUE-SPECIFICATION"', 
         '_artop_implInitValue': '"VALUE-SPECIFICATION"', 
         '_artop_initializedParameterRef': '"FLAT-INSTANCE-DESCRIPTOR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_calibrationParameterValueSet_(self):
        return self._artop_calibrationParameterValueSet

    @property
    def calibrationParameterValueSet_(self):
        if self._artop_calibrationParameterValueSet is not None:
            if hasattr(self._artop_calibrationParameterValueSet, "uuid"):
                return self._artop_calibrationParameterValueSet.uuid
        return

    @property
    def ref_applInitValue_(self):
        return self._artop_applInitValue

    @property
    def applInitValue_(self):
        if self._artop_applInitValue is not None:
            if hasattr(self._artop_applInitValue, "uuid"):
                return self._artop_applInitValue.uuid
        return

    @property
    def ref_implInitValue_(self):
        return self._artop_implInitValue

    @property
    def implInitValue_(self):
        if self._artop_implInitValue is not None:
            if hasattr(self._artop_implInitValue, "uuid"):
                return self._artop_implInitValue.uuid
        return

    @property
    def ref_initializedParameter_(self):
        return self._artop_initializedParameterRef

    @property
    def initializedParameter_(self):
        if self._artop_initializedParameterRef is not None:
            if hasattr(self._artop_initializedParameterRef, "uuid"):
                return self._artop_initializedParameterRef.uuid
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
