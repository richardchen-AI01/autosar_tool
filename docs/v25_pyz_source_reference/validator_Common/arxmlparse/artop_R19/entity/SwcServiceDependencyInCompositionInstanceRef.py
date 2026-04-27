# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcServiceDependencyInCompositionInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class SwcServiceDependencyInCompositionInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .CompositionSwComponentType import CompositionSwComponentType
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .SwcServiceDependency import SwcServiceDependency
        self._artop_compositionSwComponentType = None
        self._artop_rootContextRef = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_targetSwcServiceDependencyRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_compositionSwComponentType': '"COMPOSITION-SW-COMPONENT-TYPE"', 
         '_artop_rootContextRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetSwcServiceDependencyRef': '"SWC-SERVICE-DEPENDENCY"'})

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
    def ref_rootContext_(self):
        return self._artop_rootContextRef

    @property
    def rootContext_(self):
        if self._artop_rootContextRef is not None:
            if hasattr(self._artop_rootContextRef, "uuid"):
                return self._artop_rootContextRef.uuid
        return

    @property
    def ref_contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def ref_targetSwcServiceDependency_(self):
        return self._artop_targetSwcServiceDependencyRef

    @property
    def targetSwcServiceDependency_(self):
        if self._artop_targetSwcServiceDependencyRef is not None:
            if hasattr(self._artop_targetSwcServiceDependencyRef, "uuid"):
                return self._artop_targetSwcServiceDependencyRef.uuid
        return
