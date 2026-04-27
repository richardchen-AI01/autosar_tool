# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceDependency.py
from .ARObject import ARObject

class ServiceDependency(ARObject):

    def __init__(self):
        super().__init__()
        from .RoleBasedDataTypeAssignment import RoleBasedDataTypeAssignment
        from .SymbolicNameProps import SymbolicNameProps
        self._artop_assignedDataType = []
        self._artop_symbolicNameProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_assignedDataType':"ROLE-BASED-DATA-TYPE-ASSIGNMENT", 
         '_artop_symbolicNameProps':"SYMBOLIC-NAME-PROPS"})

    @property
    def assignedDataTypes_RoleBasedDataTypeAssignment(self):
        return self._artop_assignedDataType

    @property
    def ref_symbolicNameProps_(self):
        return self._artop_symbolicNameProps

    @property
    def symbolicNameProps_(self):
        if self._artop_symbolicNameProps is not None:
            if hasattr(self._artop_symbolicNameProps, "uuid"):
                return self._artop_symbolicNameProps.uuid
        return
