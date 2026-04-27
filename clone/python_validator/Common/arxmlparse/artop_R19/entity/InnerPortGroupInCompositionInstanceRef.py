# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InnerPortGroupInCompositionInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class InnerPortGroupInCompositionInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .PortGroup import PortGroup
        from .CompositionSwComponentType import CompositionSwComponentType
        from .SwComponentPrototype import SwComponentPrototype
        self._artop_portGroup = None
        self._artop_compositionSwComponentType = None
        self._artop_contextRef = []
        self._artop_targetRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_portGroup': '"PORT-GROUP"', 
         '_artop_compositionSwComponentType': '"COMPOSITION-SW-COMPONENT-TYPE"', 
         '_artop_contextRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetRef': '"PORT-GROUP"'})

    @property
    def ref_portGroup_(self):
        return self._artop_portGroup

    @property
    def portGroup_(self):
        if self._artop_portGroup is not None:
            if hasattr(self._artop_portGroup, "uuid"):
                return self._artop_portGroup.uuid
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
    def ref_contexts_(self):
        return self._artop_contextRef

    @property
    def contexts_(self):
        return self._artop_contextRef

    @property
    def ref_target_(self):
        return self._artop_targetRef

    @property
    def target_(self):
        if self._artop_targetRef is not None:
            if hasattr(self._artop_targetRef, "uuid"):
                return self._artop_targetRef.uuid
        return
