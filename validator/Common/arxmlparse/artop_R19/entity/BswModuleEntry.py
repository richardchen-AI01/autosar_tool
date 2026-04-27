# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleEntry.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class BswModuleEntry(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .SwServiceArg import SwServiceArg
        self._artop_functionPrototypeEmitter = None
        self._artop_serviceId = None
        self._artop_role = None
        self._artop_isReentrant = None
        self._artop_isSynchronous = None
        self._artop_callType = None
        self._artop_executionContext = None
        self._artop_swServiceImplPolicy = None
        self._artop_bswEntryKind = None
        self._artop_returnType = None
        self._artop_argument = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_returnType':"SW-SERVICE-ARG", 
         '_artop_argument':"SW-SERVICE-ARG"})

    @property
    def functionPrototypeEmitter_(self):
        return self._artop_functionPrototypeEmitter

    @property
    def serviceId_(self):
        return self._artop_serviceId

    @property
    def role_(self):
        return self._artop_role

    @property
    def isReentrant_(self):
        if self._artop_isReentrant:
            if self._artop_isReentrant == "true":
                return True
            return False
        else:
            return self._artop_isReentrant

    @property
    def isSynchronous_(self):
        if self._artop_isSynchronous:
            if self._artop_isSynchronous == "true":
                return True
            return False
        else:
            return self._artop_isSynchronous

    @property
    def callType_(self):
        return self._artop_callType

    @property
    def executionContext_(self):
        return self._artop_executionContext

    @property
    def swServiceImplPolicy_(self):
        return self._artop_swServiceImplPolicy

    @property
    def bswEntryKind_(self):
        return self._artop_bswEntryKind

    @property
    def ref_returnType_(self):
        return self._artop_returnType

    @property
    def returnType_(self):
        if self._artop_returnType is not None:
            if hasattr(self._artop_returnType, "uuid"):
                return self._artop_returnType.uuid
        return

    @property
    def arguments_SwServiceArg(self):
        return self._artop_argument
