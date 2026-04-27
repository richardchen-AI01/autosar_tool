# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataMapping.py
from .ARObject import ARObject

class DataMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .SystemMapping import SystemMapping
        from .ConsumedEventGroup import ConsumedEventGroup
        from .EventHandler import EventHandler
        from .DocumentationBlock import DocumentationBlock
        from .AbstractServiceInstance import AbstractServiceInstance
        from .VariationPoint import VariationPoint
        self._artop_communicationDirection = None
        self._artop_systemMapping = None
        self._artop_eventGroupRef = []
        self._artop_eventHandlerRef = []
        self._artop_introduction = None
        self._artop_serviceInstanceRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemMapping': '"SYSTEM-MAPPING"', 
         '_artop_eventGroupRef': '"CONSUMED-EVENT-GROUP"', 
         '_artop_eventHandlerRef': '"EVENT-HANDLER"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_serviceInstanceRef': '"ABSTRACT-SERVICE-INSTANCE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def communicationDirection_(self):
        return self._artop_communicationDirection

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
    def ref_eventGroups_(self):
        return self._artop_eventGroupRef

    @property
    def eventGroups_(self):
        return self._artop_eventGroupRef

    @property
    def ref_eventHandlers_(self):
        return self._artop_eventHandlerRef

    @property
    def eventHandlers_(self):
        return self._artop_eventHandlerRef

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
    def ref_serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstances_(self):
        return self._artop_serviceInstanceRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
