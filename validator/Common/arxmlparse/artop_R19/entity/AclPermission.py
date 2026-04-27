# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AclPermission.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class AclPermission(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .AclObjectSet import AclObjectSet
        from .AclOperation import AclOperation
        from .AclRole import AclRole
        self._artop_aclContext = None
        self._artop_aclScope = None
        self._artop_aclObjectRef = []
        self._artop_aclOperationRef = []
        self._artop_aclRoleRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_aclObjectRef':"ACL-OBJECT-SET", 
         '_artop_aclOperationRef':"ACL-OPERATION", 
         '_artop_aclRoleRef':"ACL-ROLE"})

    @property
    def aclContext_(self):
        return self._artop_aclContext

    @property
    def aclScope_(self):
        return self._artop_aclScope

    @property
    def ref_aclObjects_(self):
        return self._artop_aclObjectRef

    @property
    def aclObjects_(self):
        return self._artop_aclObjectRef

    @property
    def ref_aclOperations_(self):
        return self._artop_aclOperationRef

    @property
    def aclOperations_(self):
        return self._artop_aclOperationRef

    @property
    def ref_aclRoles_(self):
        return self._artop_aclRoleRef

    @property
    def aclRoles_(self):
        return self._artop_aclRoleRef
