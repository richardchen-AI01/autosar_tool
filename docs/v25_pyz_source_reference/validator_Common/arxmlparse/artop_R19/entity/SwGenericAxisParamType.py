# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwGenericAxisParamType.py
from .Identifiable import Identifiable

class SwGenericAxisParamType(Identifiable):

    def __init__(self):
        super().__init__()
        from .SwAxisType import SwAxisType
        from .DataConstr import DataConstr
        self._artop_swAxisType = None
        self._artop_dataConstrRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swAxisType':"SW-AXIS-TYPE", 
         '_artop_dataConstrRef':"DATA-CONSTR"})

    @property
    def ref_swAxisType_(self):
        return self._artop_swAxisType

    @property
    def swAxisType_(self):
        if self._artop_swAxisType is not None:
            if hasattr(self._artop_swAxisType, "uuid"):
                return self._artop_swAxisType.uuid
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
