# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignal.py
from .FibexElement import FibexElement

class ISignal(FibexElement):

    def __init__(self):
        super().__init__()
        from .DataTransformationRefConditional import DataTransformationRefConditional
        from .ISignalProps import ISignalProps
        from .ValueSpecification import ValueSpecification
        from .SwDataDefProps import SwDataDefProps
        from .SystemSignal import SystemSignal
        from .TransformationISignalProps import TransformationISignalProps
        self._artop_dataTypePolicy = None
        self._artop_iSignalType = None
        self._artop_length = None
        self._artop_dataTransformation = []
        self._artop_iSignalProps = None
        self._artop_initValue = None
        self._artop_networkRepresentationProps = None
        self._artop_systemSignalRef = None
        self._artop_timeoutSubstitutionValue = None
        self._artop_transformationISignalProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataTransformation': '"DATA-TRANSFORMATION-REF-CONDITIONAL"', 
         '_artop_iSignalProps': '"I-SIGNAL-PROPS"', 
         '_artop_initValue': '"VALUE-SPECIFICATION"', 
         '_artop_networkRepresentationProps': '"SW-DATA-DEF-PROPS"', 
         '_artop_systemSignalRef': '"SYSTEM-SIGNAL"', 
         '_artop_timeoutSubstitutionValue': '"VALUE-SPECIFICATION"', 
         '_artop_transformationISignalProps': '"TRANSFORMATION-I-SIGNAL-PROPS"'})

    @property
    def dataTypePolicy_(self):
        return self._artop_dataTypePolicy

    @property
    def iSignalType_(self):
        return self._artop_iSignalType

    @property
    def length_(self):
        if self._artop_length:
            return int(self._artop_length)
        return self._artop_length

    @property
    def dataTransformations_DataTransformationRefConditional(self):
        return self._artop_dataTransformation

    @property
    def ref_iSignalProps_(self):
        return self._artop_iSignalProps

    @property
    def iSignalProps_(self):
        if self._artop_iSignalProps is not None:
            if hasattr(self._artop_iSignalProps, "uuid"):
                return self._artop_iSignalProps.uuid
        return

    @property
    def ref_initValue_(self):
        return self._artop_initValue

    @property
    def initValue_(self):
        if self._artop_initValue is not None:
            if hasattr(self._artop_initValue, "uuid"):
                return self._artop_initValue.uuid
        return

    @property
    def ref_networkRepresentationProps_(self):
        return self._artop_networkRepresentationProps

    @property
    def networkRepresentationProps_(self):
        if self._artop_networkRepresentationProps is not None:
            if hasattr(self._artop_networkRepresentationProps, "uuid"):
                return self._artop_networkRepresentationProps.uuid
        return

    @property
    def ref_systemSignal_(self):
        return self._artop_systemSignalRef

    @property
    def systemSignal_(self):
        if self._artop_systemSignalRef is not None:
            if hasattr(self._artop_systemSignalRef, "uuid"):
                return self._artop_systemSignalRef.uuid
        return

    @property
    def ref_timeoutSubstitutionValue_(self):
        return self._artop_timeoutSubstitutionValue

    @property
    def timeoutSubstitutionValue_(self):
        if self._artop_timeoutSubstitutionValue is not None:
            if hasattr(self._artop_timeoutSubstitutionValue, "uuid"):
                return self._artop_timeoutSubstitutionValue.uuid
        return

    @property
    def transformationISignalProps_TransformationISignalProps(self):
        return self._artop_transformationISignalProps
