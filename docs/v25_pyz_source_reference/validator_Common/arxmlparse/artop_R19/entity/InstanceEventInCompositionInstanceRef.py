# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InstanceEventInCompositionInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class InstanceEventInCompositionInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .InstantiationRTEEventProps import InstantiationRTEEventProps
        from .CompositionSwComponentType import CompositionSwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        from .RTEEvent import RTEEvent
        self._artop_instantiationRteEventProps = None
        self._artop_compositionSwComponentType = None
        self._artop_contextComponentPrototypeRef = []
        self._artop_targetEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_instantiationRteEventProps': '"INSTANTIATION-RTE-EVENT-PROPS"', 
         '_artop_compositionSwComponentType': '"COMPOSITION-SW-COMPONENT-TYPE"', 
         '_artop_contextComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetEventRef': '"RTE-EVENT"'})

    @property
    def ref_instantiationRTEEventProps_(self):
        return self._artop_instantiationRteEventProps

    @property
    def instantiationRTEEventProps_(self):
        if self._artop_instantiationRteEventProps is not None:
            if hasattr(self._artop_instantiationRteEventProps, "uuid"):
                return self._artop_instantiationRteEventProps.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_compositionSwComponentType

    @property
    def base_(self):
        if self._artop_compositionSwComponentType is not None:
            if hasattr(self._artop_compositionSwComponentType, "uuid"):
                return self._artop_compositionSwComponentType.uuid
        return

    @property
    def ref_contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def contextComponentPrototypes_(self):
        return self._artop_contextComponentPrototypeRef

    @property
    def ref_targetEvent_(self):
        return self._artop_targetEventRef

    @property
    def targetEvent_(self):
        if self._artop_targetEventRef is not None:
            if hasattr(self._artop_targetEventRef, "uuid"):
                return self._artop_targetEventRef.uuid
        return
