# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhysicalDimensionMapping.py
from .ARObject import ARObject

class PhysicalDimensionMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .PhysicalDimensionMappingSet import PhysicalDimensionMappingSet
        from .PhysicalDimension import PhysicalDimension
        self._artop_physicalDimensionMappingSet = None
        self._artop_firstPhysicalDimensionRef = None
        self._artop_secondPhysicalDimensionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_physicalDimensionMappingSet':"PHYSICAL-DIMENSION-MAPPING-SET", 
         '_artop_firstPhysicalDimensionRef':"PHYSICAL-DIMENSION", 
         '_artop_secondPhysicalDimensionRef':"PHYSICAL-DIMENSION"})

    @property
    def ref_physicalDimensionMappingSet_(self):
        return self._artop_physicalDimensionMappingSet

    @property
    def physicalDimensionMappingSet_(self):
        if self._artop_physicalDimensionMappingSet is not None:
            if hasattr(self._artop_physicalDimensionMappingSet, "uuid"):
                return self._artop_physicalDimensionMappingSet.uuid
        return

    @property
    def ref_firstPhysicalDimension_(self):
        return self._artop_firstPhysicalDimensionRef

    @property
    def firstPhysicalDimension_(self):
        if self._artop_firstPhysicalDimensionRef is not None:
            if hasattr(self._artop_firstPhysicalDimensionRef, "uuid"):
                return self._artop_firstPhysicalDimensionRef.uuid
        return

    @property
    def ref_secondPhysicalDimension_(self):
        return self._artop_secondPhysicalDimensionRef

    @property
    def secondPhysicalDimension_(self):
        if self._artop_secondPhysicalDimensionRef is not None:
            if hasattr(self._artop_secondPhysicalDimensionRef, "uuid"):
                return self._artop_secondPhysicalDimensionRef.uuid
        return
