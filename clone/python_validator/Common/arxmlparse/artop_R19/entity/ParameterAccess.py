# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ParameterAccess.py
from .AbstractAccessPoint import AbstractAccessPoint

class ParameterAccess(AbstractAccessPoint):

    def __init__(self):
        super().__init__()
        from .RunnableEntity import RunnableEntity
        from .AutosarParameterRef import AutosarParameterRef
        from .SwDataDefProps import SwDataDefProps
        from .VariationPoint import VariationPoint
        self._artop_runnableEntity = None
        self._artop_accessedParameter = None
        self._artop_swDataDefProps = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_runnableEntity': '"RUNNABLE-ENTITY"', 
         '_artop_accessedParameter': '"AUTOSAR-PARAMETER-REF"', 
         '_artop_swDataDefProps': '"SW-DATA-DEF-PROPS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_runnableEntity_(self):
        return self._artop_runnableEntity

    @property
    def runnableEntity_(self):
        if self._artop_runnableEntity is not None:
            if hasattr(self._artop_runnableEntity, "uuid"):
                return self._artop_runnableEntity.uuid
        return

    @property
    def ref_accessedParameter_(self):
        return self._artop_accessedParameter

    @property
    def accessedParameter_(self):
        if self._artop_accessedParameter is not None:
            if hasattr(self._artop_accessedParameter, "uuid"):
                return self._artop_accessedParameter.uuid
        return

    @property
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
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
