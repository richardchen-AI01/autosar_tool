# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcToEcuMapping.py
from .Identifiable import Identifiable

class SwcToEcuMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .ComponentInSystemInstanceRef import ComponentInSystemInstanceRef
        from .HwElement import HwElement
        from .EcuInstance import EcuInstance
        from .EcuPartition import EcuPartition
        from .VariationPoint import VariationPoint
        self._artop_systemMapping = None
        self._artop_componentIref = []
        self._artop_controlledHwElementRef = None
        self._artop_ecuInstanceRef = None
        self._artop_partitionRef = None
        self._artop_processingUnitRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_componentIref': '"COMPONENT-IN-SYSTEM-INSTANCE-REF-IREF"', 
         '_artop_controlledHwElementRef': '"HW-ELEMENT"', 
         '_artop_ecuInstanceRef': '"ECU-INSTANCE"', 
         '_artop_partitionRef': '"ECU-PARTITION"', 
         '_artop_processingUnitRef': '"HW-ELEMENT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_systemMapping_(self):
        return self._artop_systemMapping

    @property
    def systemMapping_(self):
        if self._artop_systemMapping is not None:
            if hasattr(self._artop_systemMapping, "uuid"):
                return self._artop_systemMapping.uuid
        return

    @property
    def components_ComponentInSystemInstanceRef(self):
        return self._artop_componentIref

    @property
    def ref_controlledHwElement_(self):
        return self._artop_controlledHwElementRef

    @property
    def controlledHwElement_(self):
        if self._artop_controlledHwElementRef is not None:
            if hasattr(self._artop_controlledHwElementRef, "uuid"):
                return self._artop_controlledHwElementRef.uuid
        return

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
        return

    @property
    def ref_partition_(self):
        return self._artop_partitionRef

    @property
    def partition_(self):
        if self._artop_partitionRef is not None:
            if hasattr(self._artop_partitionRef, "uuid"):
                return self._artop_partitionRef.uuid
        return

    @property
    def ref_processingUnit_(self):
        return self._artop_processingUnitRef

    @property
    def processingUnit_(self):
        if self._artop_processingUnitRef is not None:
            if hasattr(self._artop_processingUnitRef, "uuid"):
                return self._artop_processingUnitRef.uuid
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
