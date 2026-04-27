# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcToEcuMappingConstraint.py
from .MappingConstraint import MappingConstraint

class SwcToEcuMappingConstraint(MappingConstraint):

    def __init__(self):
        super().__init__()
        from .ComponentInSystemInstanceRef import ComponentInSystemInstanceRef
        from .EcuInstance import EcuInstance
        self._artop_swcToEcuMappingConstraintType = None
        self._artop_componentIref = None
        self._artop_ecuInstanceRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_componentIref':"COMPONENT-IN-SYSTEM-INSTANCE-REF-IREF", 
         '_artop_ecuInstanceRef':"ECU-INSTANCE"})

    @property
    def swcToEcuMappingConstraintType_(self):
        return self._artop_swcToEcuMappingConstraintType

    @property
    def ref_component_(self):
        return self._artop_componentIref

    @property
    def component_(self):
        if self._artop_componentIref is not None:
            if hasattr(self._artop_componentIref, "uuid"):
                return self._artop_componentIref.uuid
        return

    @property
    def ref_ecuInstances_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstances_(self):
        return self._artop_ecuInstanceRef
