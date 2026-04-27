# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticMemoryIdentifier.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticMemoryIdentifier(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticAccessPermission import DiagnosticAccessPermission
        self._artop_id = None
        self._artop_memoryHighAddress = None
        self._artop_memoryHighAddressLabel = None
        self._artop_memoryLowAddress = None
        self._artop_memoryLowAddressLabel = None
        self._artop_accessPermissionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_accessPermissionRef": "DIAGNOSTIC-ACCESS-PERMISSION"})

    @property
    def id_(self):
        return self._artop_id

    @property
    def memoryHighAddress_(self):
        return self._artop_memoryHighAddress

    @property
    def memoryHighAddressLabel_(self):
        return self._artop_memoryHighAddressLabel

    @property
    def memoryLowAddress_(self):
        return self._artop_memoryLowAddress

    @property
    def memoryLowAddressLabel_(self):
        return self._artop_memoryLowAddressLabel

    @property
    def ref_accessPermission_(self):
        return self._artop_accessPermissionRef

    @property
    def accessPermission_(self):
        if self._artop_accessPermissionRef is not None:
            if hasattr(self._artop_accessPermissionRef, "uuid"):
                return self._artop_accessPermissionRef.uuid
        return
