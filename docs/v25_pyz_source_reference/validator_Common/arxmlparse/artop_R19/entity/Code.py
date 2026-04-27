# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Code.py
from .Identifiable import Identifiable

class Code(Identifiable):

    def __init__(self):
        super().__init__()
        from .Implementation import Implementation
        from .AutosarEngineeringObject import AutosarEngineeringObject
        from .ServiceNeeds import ServiceNeeds
        self._artop_implementation = None
        self._artop_artifactDescriptor = []
        self._artop_callbackHeaderRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_implementation':"IMPLEMENTATION", 
         '_artop_artifactDescriptor':"AUTOSAR-ENGINEERING-OBJECT", 
         '_artop_callbackHeaderRef':"SERVICE-NEEDS"})

    @property
    def ref_implementation_(self):
        return self._artop_implementation

    @property
    def implementation_(self):
        if self._artop_implementation is not None:
            if hasattr(self._artop_implementation, "uuid"):
                return self._artop_implementation.uuid
        return

    @property
    def artifactDescriptors_AutosarEngineeringObject(self):
        return self._artop_artifactDescriptor

    @property
    def ref_callbackHeaders_(self):
        return self._artop_callbackHeaderRef

    @property
    def callbackHeaders_(self):
        return self._artop_callbackHeaderRef
