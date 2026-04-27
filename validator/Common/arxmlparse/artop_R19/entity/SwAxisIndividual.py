# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwAxisIndividual.py
from .SwCalprmAxisTypeProps import SwCalprmAxisTypeProps

class SwAxisIndividual(SwCalprmAxisTypeProps):

    def __init__(self):
        super().__init__()
        from .ApplicationPrimitiveDataType import ApplicationPrimitiveDataType
        from .SwVariableRefProxy import SwVariableRefProxy
        from .CompuMethod import CompuMethod
        from .Unit import Unit
        from .IntegerValueVariationPoint import IntegerValueVariationPoint
        from .DataConstr import DataConstr
        from .SwAxisGeneric import SwAxisGeneric
        self._artop_inputVariableTypeRef = None
        self._artop_swVariableRef = []
        self._artop_compuMethodRef = None
        self._artop_unitRef = None
        self._artop_swMaxAxisPoints = None
        self._artop_swMinAxisPoints = None
        self._artop_dataConstrRef = None
        self._artop_swAxisGeneric = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_inputVariableTypeRef': '"APPLICATION-PRIMITIVE-DATA-TYPE"', 
         '_artop_swVariableRef': '"SW-VARIABLE-REF-PROXY"', 
         '_artop_compuMethodRef': '"COMPU-METHOD"', 
         '_artop_unitRef': '"UNIT"', 
         '_artop_swMaxAxisPoints': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_swMinAxisPoints': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_dataConstrRef': '"DATA-CONSTR"', 
         '_artop_swAxisGeneric': '"SW-AXIS-GENERIC"'})

    @property
    def ref_inputVariableType_(self):
        return self._artop_inputVariableTypeRef

    @property
    def inputVariableType_(self):
        if self._artop_inputVariableTypeRef is not None:
            if hasattr(self._artop_inputVariableTypeRef, "uuid"):
                return self._artop_inputVariableTypeRef.uuid
        return

    @property
    def swVariableRefs_SwVariableRefProxy(self):
        return self._artop_swVariableRef

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
    def ref_unit_(self):
        return self._artop_unitRef

    @property
    def unit_(self):
        if self._artop_unitRef is not None:
            if hasattr(self._artop_unitRef, "uuid"):
                return self._artop_unitRef.uuid
        return

    @property
    def ref_swMaxAxisPoints_(self):
        return self._artop_swMaxAxisPoints

    @property
    def swMaxAxisPoints_(self):
        if self._artop_swMaxAxisPoints is not None:
            if hasattr(self._artop_swMaxAxisPoints, "uuid"):
                return self._artop_swMaxAxisPoints.uuid
        return

    @property
    def ref_swMinAxisPoints_(self):
        return self._artop_swMinAxisPoints

    @property
    def swMinAxisPoints_(self):
        if self._artop_swMinAxisPoints is not None:
            if hasattr(self._artop_swMinAxisPoints, "uuid"):
                return self._artop_swMinAxisPoints.uuid
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
    def ref_swAxisGeneric_(self):
        return self._artop_swAxisGeneric

    @property
    def swAxisGeneric_(self):
        if self._artop_swAxisGeneric is not None:
            if hasattr(self._artop_swAxisGeneric, "uuid"):
                return self._artop_swAxisGeneric.uuid
        return
