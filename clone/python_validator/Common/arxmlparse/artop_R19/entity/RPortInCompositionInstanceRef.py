# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RPortInCompositionInstanceRef.py
from .PortInCompositionTypeInstanceRef import PortInCompositionTypeInstanceRef

class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):

    def __init__(self):
        super().__init__()
        from .AssemblySwConnector import AssemblySwConnector
        from .SwComponentPrototype import SwComponentPrototype
        from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
        from .CompositionSwComponentType import CompositionSwComponentType
        self._artop_assemblySwConnector = None
        self._artop_contextComponentRef = None
        self._artop_targetRPortRef = None
        self._artop_compositionSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_assemblySwConnector': '"ASSEMBLY-SW-CONNECTOR"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetRPortRef': '"ABSTRACT-REQUIRED-PORT-PROTOTYPE"', 
         '_artop_compositionSwComponentType': '"COMPOSITION-SW-COMPONENT-TYPE"'})

    @property
    def ref_assemblySwConnector_(self):
        return self._artop_assemblySwConnector

    @property
    def assemblySwConnector_(self):
        if self._artop_assemblySwConnector is not None:
            if hasattr(self._artop_assemblySwConnector, "uuid"):
                return self._artop_assemblySwConnector.uuid
        return

    @property
    def ref_contextComponent_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponent_(self):
        if self._artop_contextComponentRef is not None:
            if hasattr(self._artop_contextComponentRef, "uuid"):
                return self._artop_contextComponentRef.uuid
        return

    @property
    def ref_targetRPort_(self):
        return self._artop_targetRPortRef

    @property
    def targetRPort_(self):
        if self._artop_targetRPortRef is not None:
            if hasattr(self._artop_targetRPortRef, "uuid"):
                return self._artop_targetRPortRef.uuid
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
