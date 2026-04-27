# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RtePluginProps.py
from .ARObject import ARObject

class RtePluginProps(ARObject):

    def __init__(self):
        super().__init__()
        from .FlatInstanceDescriptor import FlatInstanceDescriptor
        from .EcucContainerValue import EcucContainerValue
        self._artop_flatInstanceDescriptor = None
        self._artop_associatedRtePluginRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flatInstanceDescriptor':"FLAT-INSTANCE-DESCRIPTOR", 
         '_artop_associatedRtePluginRef':"ECUC-CONTAINER-VALUE"})

    @property
    def ref_flatInstanceDescriptor_(self):
        return self._artop_flatInstanceDescriptor

    @property
    def flatInstanceDescriptor_(self):
        if self._artop_flatInstanceDescriptor is not None:
            if hasattr(self._artop_flatInstanceDescriptor, "uuid"):
                return self._artop_flatInstanceDescriptor.uuid
        return

    @property
    def ref_associatedRtePlugin_(self):
        return self._artop_associatedRtePluginRef

    @property
    def associatedRtePlugin_(self):
        if self._artop_associatedRtePluginRef is not None:
            if hasattr(self._artop_associatedRtePluginRef, "uuid"):
                return self._artop_associatedRtePluginRef.uuid
        return
