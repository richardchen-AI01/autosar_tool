# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationPartitionToEcuPartitionMapping.py
from .Identifiable import Identifiable

class ApplicationPartitionToEcuPartitionMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .ApplicationPartition import ApplicationPartition
        from .EcuPartition import EcuPartition
        from .VariationPoint import VariationPoint
        self._artop_systemMapping = None
        self._artop_applicationPartitionRef = []
        self._artop_ecuPartitionRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_applicationPartitionRef': '"APPLICATION-PARTITION"', 
         '_artop_ecuPartitionRef': '"ECU-PARTITION"', 
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
    def ref_applicationPartitions_(self):
        return self._artop_applicationPartitionRef

    @property
    def applicationPartitions_(self):
        return self._artop_applicationPartitionRef

    @property
    def ref_ecuPartition_(self):
        return self._artop_ecuPartitionRef

    @property
    def ecuPartition_(self):
        if self._artop_ecuPartitionRef is not None:
            if hasattr(self._artop_ecuPartitionRef, "uuid"):
                return self._artop_ecuPartitionRef.uuid
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
