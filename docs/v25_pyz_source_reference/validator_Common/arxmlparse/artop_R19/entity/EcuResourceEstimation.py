# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcuResourceEstimation.py
from .ARObject import ARObject

class EcuResourceEstimation(ARObject):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .DocumentationBlock import DocumentationBlock
        from .ResourceConsumption import ResourceConsumption
        from .EcuInstance import EcuInstance
        from .SwcToEcuMapping import SwcToEcuMapping
        from .VariationPoint import VariationPoint
        self._artop_systemMapping = None
        self._artop_introduction = None
        self._artop_bswResourceEstimation = None
        self._artop_ecuInstanceRef = None
        self._artop_rteResourceEstimation = None
        self._artop_swCompToEcuMappingRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_bswResourceEstimation': '"RESOURCE-CONSUMPTION"', 
         '_artop_ecuInstanceRef': '"ECU-INSTANCE"', 
         '_artop_rteResourceEstimation': '"RESOURCE-CONSUMPTION"', 
         '_artop_swCompToEcuMappingRef': '"SWC-TO-ECU-MAPPING"', 
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
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return

    @property
    def ref_bswResourceEstimation_(self):
        return self._artop_bswResourceEstimation

    @property
    def bswResourceEstimation_(self):
        if self._artop_bswResourceEstimation is not None:
            if hasattr(self._artop_bswResourceEstimation, "uuid"):
                return self._artop_bswResourceEstimation.uuid
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
    def ref_rteResourceEstimation_(self):
        return self._artop_rteResourceEstimation

    @property
    def rteResourceEstimation_(self):
        if self._artop_rteResourceEstimation is not None:
            if hasattr(self._artop_rteResourceEstimation, "uuid"):
                return self._artop_rteResourceEstimation.uuid
        return

    @property
    def ref_swCompToEcuMappings_(self):
        return self._artop_swCompToEcuMappingRef

    @property
    def swCompToEcuMappings_(self):
        return self._artop_swCompToEcuMappingRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
