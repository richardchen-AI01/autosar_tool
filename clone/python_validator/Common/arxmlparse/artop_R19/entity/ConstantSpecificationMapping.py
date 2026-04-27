# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConstantSpecificationMapping.py
from .ARObject import ARObject

class ConstantSpecificationMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .ConstantSpecificationMappingSet import ConstantSpecificationMappingSet
        from .ConstantSpecification import ConstantSpecification
        self._artop_constantSpecificationMappingSet = None
        self._artop_applConstantRef = None
        self._artop_implConstantRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_constantSpecificationMappingSet':"CONSTANT-SPECIFICATION-MAPPING-SET", 
         '_artop_applConstantRef':"CONSTANT-SPECIFICATION", 
         '_artop_implConstantRef':"CONSTANT-SPECIFICATION"})

    @property
    def ref_constantSpecificationMappingSet_(self):
        return self._artop_constantSpecificationMappingSet

    @property
    def constantSpecificationMappingSet_(self):
        if self._artop_constantSpecificationMappingSet is not None:
            if hasattr(self._artop_constantSpecificationMappingSet, "uuid"):
                return self._artop_constantSpecificationMappingSet.uuid
        return

    @property
    def ref_applConstant_(self):
        return self._artop_applConstantRef

    @property
    def applConstant_(self):
        if self._artop_applConstantRef is not None:
            if hasattr(self._artop_applConstantRef, "uuid"):
                return self._artop_applConstantRef.uuid
        return

    @property
    def ref_implConstant_(self):
        return self._artop_implConstantRef

    @property
    def implConstant_(self):
        if self._artop_implConstantRef is not None:
            if hasattr(self._artop_implConstantRef, "uuid"):
                return self._artop_implConstantRef.uuid
        return
