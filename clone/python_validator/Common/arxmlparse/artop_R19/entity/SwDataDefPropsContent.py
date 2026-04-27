# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwDataDefPropsContent.py
from .ARObject import ARObject

class SwDataDefPropsContent(ARObject):

    def __init__(self):
        super().__init__()
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        from .Annotation import Annotation
        from .SwAddrMethod import SwAddrMethod
        from .SwBaseType import SwBaseType
        from .SwBitRepresentation import SwBitRepresentation
        from .SwCalprmAxisSet import SwCalprmAxisSet
        from .SwTextProps import SwTextProps
        from .SwVariableRefProxy import SwVariableRefProxy
        from .CompuMethod import CompuMethod
        from .DataConstr import DataConstr
        from .SwDataDependency import SwDataDependency
        from .AbstractImplementationDataType import AbstractImplementationDataType
        from .ValueSpecification import ValueSpecification
        from .SwPointerTargetProps import SwPointerTargetProps
        from .SwRecordLayout import SwRecordLayout
        from .MultidimensionalTime import MultidimensionalTime
        from .Unit import Unit
        from .ApplicationPrimitiveDataType import ApplicationPrimitiveDataType
        self._artop_displayPresentation = None
        self._artop_stepSize = None
        self._artop_swAlignment = None
        self._artop_swCalibrationAccess = None
        self._artop_displayFormat = None
        self._artop_swImplPolicy = None
        self._artop_additionalNativeTypeQualifier = None
        self._artop_swIntendedResolution = None
        self._artop_swInterpolationMethod = None
        self._artop_mcFunction = None
        self._artop_swIsVirtual = None
        self._artop_swValueBlockSizeMult = []
        self._artop_annotation = []
        self._artop_swAddrMethodRef = None
        self._artop_baseTypeRef = None
        self._artop_swBitRepresentation = None
        self._artop_swValueBlockSize = None
        self._artop_swCalprmAxisSet = None
        self._artop_swTextProps = None
        self._artop_swComparisonVariable = []
        self._artop_compuMethodRef = None
        self._artop_dataConstrRef = None
        self._artop_swDataDependency = None
        self._artop_implementationDataTypeRef = None
        self._artop_swHostVariable = None
        self._artop_invalidValue = None
        self._artop_swPointerTargetProps = None
        self._artop_swRecordLayoutRef = None
        self._artop_swRefreshTiming = None
        self._artop_unitRef = None
        self._artop_valueAxisDataTypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swValueBlockSizeMult': '"NUMERICAL-VALUE-VARIATION-POINT"', 
         '_artop_annotation': '"ANNOTATION"', 
         '_artop_swAddrMethodRef': '"SW-ADDR-METHOD"', 
         '_artop_baseTypeRef': '"SW-BASE-TYPE"', 
         '_artop_swBitRepresentation': '"SW-BIT-REPRESENTATION"', 
         '_artop_swValueBlockSize': '"NUMERICAL-VALUE-VARIATION-POINT"', 
         '_artop_swCalprmAxisSet': '"SW-CALPRM-AXIS-SET"', 
         '_artop_swTextProps': '"SW-TEXT-PROPS"', 
         '_artop_swComparisonVariable': '"SW-VARIABLE-REF-PROXY"', 
         '_artop_compuMethodRef': '"COMPU-METHOD"', 
         '_artop_dataConstrRef': '"DATA-CONSTR"', 
         '_artop_swDataDependency': '"SW-DATA-DEPENDENCY"', 
         '_artop_implementationDataTypeRef': '"ABSTRACT-IMPLEMENTATION-DATA-TYPE"', 
         '_artop_swHostVariable': '"SW-VARIABLE-REF-PROXY"', 
         '_artop_invalidValue': '"VALUE-SPECIFICATION"', 
         '_artop_swPointerTargetProps': '"SW-POINTER-TARGET-PROPS"', 
         '_artop_swRecordLayoutRef': '"SW-RECORD-LAYOUT"', 
         '_artop_swRefreshTiming': '"MULTIDIMENSIONAL-TIME"', 
         '_artop_unitRef': '"UNIT"', 
         '_artop_valueAxisDataTypeRef': '"APPLICATION-PRIMITIVE-DATA-TYPE"'})

    @property
    def displayPresentation_(self):
        return self._artop_displayPresentation

    @property
    def stepSize_(self):
        if self._artop_stepSize:
            return float(self._artop_stepSize)
        return self._artop_stepSize

    @property
    def swAlignment_(self):
        return self._artop_swAlignment

    @property
    def swCalibrationAccess_(self):
        return self._artop_swCalibrationAccess

    @property
    def displayFormat_(self):
        return self._artop_displayFormat

    @property
    def swImplPolicy_(self):
        return self._artop_swImplPolicy

    @property
    def additionalNativeTypeQualifier_(self):
        return self._artop_additionalNativeTypeQualifier

    @property
    def swIntendedResolution_(self):
        return self._artop_swIntendedResolution

    @property
    def swInterpolationMethod_(self):
        return self._artop_swInterpolationMethod

    @property
    def mcFunction_(self):
        return self._artop_mcFunction

    @property
    def swIsVirtual_(self):
        if self._artop_swIsVirtual:
            if self._artop_swIsVirtual == "true":
                return True
            return False
        else:
            return self._artop_swIsVirtual

    @property
    def swValueBlockSizeMults_NumericalValueVariationPoint(self):
        return self._artop_swValueBlockSizeMult

    @property
    def annotations_Annotation(self):
        return self._artop_annotation

    @property
    def ref_swAddrMethod_(self):
        return self._artop_swAddrMethodRef

    @property
    def swAddrMethod_(self):
        if self._artop_swAddrMethodRef is not None:
            if hasattr(self._artop_swAddrMethodRef, "uuid"):
                return self._artop_swAddrMethodRef.uuid
        return

    @property
    def ref_baseType_(self):
        return self._artop_baseTypeRef

    @property
    def baseType_(self):
        if self._artop_baseTypeRef is not None:
            if hasattr(self._artop_baseTypeRef, "uuid"):
                return self._artop_baseTypeRef.uuid
        return

    @property
    def ref_swBitRepresentation_(self):
        return self._artop_swBitRepresentation

    @property
    def swBitRepresentation_(self):
        if self._artop_swBitRepresentation is not None:
            if hasattr(self._artop_swBitRepresentation, "uuid"):
                return self._artop_swBitRepresentation.uuid
        return

    @property
    def ref_swValueBlockSize_(self):
        return self._artop_swValueBlockSize

    @property
    def swValueBlockSize_(self):
        if self._artop_swValueBlockSize is not None:
            if hasattr(self._artop_swValueBlockSize, "uuid"):
                return self._artop_swValueBlockSize.uuid
        return

    @property
    def ref_swCalprmAxisSet_(self):
        return self._artop_swCalprmAxisSet

    @property
    def swCalprmAxisSet_(self):
        if self._artop_swCalprmAxisSet is not None:
            if hasattr(self._artop_swCalprmAxisSet, "uuid"):
                return self._artop_swCalprmAxisSet.uuid
        return

    @property
    def ref_swTextProps_(self):
        return self._artop_swTextProps

    @property
    def swTextProps_(self):
        if self._artop_swTextProps is not None:
            if hasattr(self._artop_swTextProps, "uuid"):
                return self._artop_swTextProps.uuid
        return

    @property
    def swComparisonVariables_SwVariableRefProxy(self):
        return self._artop_swComparisonVariable

    @property
    def ref_compuMethod_(self):
        return self._artop_compuMethodRef

    @property
    def compuMethod_(self):
        if self._artop_compuMethodRef is not None:
            if hasattr(self._artop_compuMethodRef, "uuid"):
                return self._artop_compuMethodRef.uuid
        return

    @property
    def ref_dataConstr_(self):
        return self._artop_dataConstrRef

    @property
    def dataConstr_(self):
        if self._artop_dataConstrRef is not None:
            if hasattr(self._artop_dataConstrRef, "uuid"):
                return self._artop_dataConstrRef.uuid
        return

    @property
    def ref_swDataDependency_(self):
        return self._artop_swDataDependency

    @property
    def swDataDependency_(self):
        if self._artop_swDataDependency is not None:
            if hasattr(self._artop_swDataDependency, "uuid"):
                return self._artop_swDataDependency.uuid
        return

    @property
    def ref_implementationDataType_(self):
        return self._artop_implementationDataTypeRef

    @property
    def implementationDataType_(self):
        if self._artop_implementationDataTypeRef is not None:
            if hasattr(self._artop_implementationDataTypeRef, "uuid"):
                return self._artop_implementationDataTypeRef.uuid
        return

    @property
    def ref_swHostVariable_(self):
        return self._artop_swHostVariable

    @property
    def swHostVariable_(self):
        if self._artop_swHostVariable is not None:
            if hasattr(self._artop_swHostVariable, "uuid"):
                return self._artop_swHostVariable.uuid
        return

    @property
    def ref_invalidValue_(self):
        return self._artop_invalidValue

    @property
    def invalidValue_(self):
        if self._artop_invalidValue is not None:
            if hasattr(self._artop_invalidValue, "uuid"):
                return self._artop_invalidValue.uuid
        return

    @property
    def ref_swPointerTargetProps_(self):
        return self._artop_swPointerTargetProps

    @property
    def swPointerTargetProps_(self):
        if self._artop_swPointerTargetProps is not None:
            if hasattr(self._artop_swPointerTargetProps, "uuid"):
                return self._artop_swPointerTargetProps.uuid
        return

    @property
    def ref_swRecordLayout_(self):
        return self._artop_swRecordLayoutRef

    @property
    def swRecordLayout_(self):
        if self._artop_swRecordLayoutRef is not None:
            if hasattr(self._artop_swRecordLayoutRef, "uuid"):
                return self._artop_swRecordLayoutRef.uuid
        return

    @property
    def ref_swRefreshTiming_(self):
        return self._artop_swRefreshTiming

    @property
    def swRefreshTiming_(self):
        if self._artop_swRefreshTiming is not None:
            if hasattr(self._artop_swRefreshTiming, "uuid"):
                return self._artop_swRefreshTiming.uuid
        return

    @property
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

    @property
    def ref_valueAxisDataType_(self):
        return self._artop_valueAxisDataTypeRef

    @property
    def valueAxisDataType_(self):
        if self._artop_valueAxisDataTypeRef is not None:
            if hasattr(self._artop_valueAxisDataTypeRef, "uuid"):
                return self._artop_valueAxisDataTypeRef.uuid
        return
