# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ISignalGroup.py
from .FibexElement import FibexElement

class ISignalGroup(FibexElement):

    def __init__(self):
        super().__init__()
        from .DataTransformationRefConditional import DataTransformationRefConditional
        from .ISignal import ISignal
        from .SystemSignalGroup import SystemSignalGroup
        from .TransformationISignalProps import TransformationISignalProps
        self._artop_comBasedSignalGroupTransformation = []
        self._artop_iSignalRef = []
        self._artop_systemSignalGroupRef = None
        self._artop_transformationISignalProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_comBasedSignalGroupTransformation': '"DATA-TRANSFORMATION-REF-CONDITIONAL"', 
         '_artop_iSignalRef': '"I-SIGNAL"', 
         '_artop_systemSignalGroupRef': '"SYSTEM-SIGNAL-GROUP"', 
         '_artop_transformationISignalProps': '"TRANSFORMATION-I-SIGNAL-PROPS"'})

    @property
    def comBasedSignalGroupTransformations_DataTransformationRefConditional(self):
        return self._artop_comBasedSignalGroupTransformation

    @property
    def ref_iSignals_(self):
        return self._artop_iSignalRef

    @property
    def iSignals_(self):
        return self._artop_iSignalRef

    @property
    def ref_systemSignalGroup_(self):
        return self._artop_systemSignalGroupRef

    @property
    def systemSignalGroup_(self):
        if self._artop_systemSignalGroupRef is not None:
            if hasattr(self._artop_systemSignalGroupRef, "uuid"):
                return self._artop_systemSignalGroupRef.uuid
        return

    @property
    def transformationISignalProps_TransformationISignalProps(self):
        return self._artop_transformationISignalProps
