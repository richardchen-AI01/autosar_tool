# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComFindServiceGrant.py
from .Grant import Grant

class ComFindServiceGrant(Grant):

    def __init__(self):
        super().__init__()
        from .ComFindServiceGrantDesign import ComFindServiceGrantDesign
        from .AdaptivePlatformServiceInstance import AdaptivePlatformServiceInstance
        self._artop_designRef = None
        self._artop_serviceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_designRef':"COM-FIND-SERVICE-GRANT-DESIGN", 
         '_artop_serviceInstanceRef':"ADAPTIVE-PLATFORM-SERVICE-INSTANCE"})

    @property
    def ref_design_(self):
        return self._artop_designRef

    @property
    def design_(self):
        if self._artop_designRef is not None:
            if hasattr(self._artop_designRef, "uuid"):
                return self._artop_designRef.uuid
        return

    @property
    def ref_serviceInstance_(self):
        return self._artop_serviceInstanceRef

    @property
    def serviceInstance_(self):
        if self._artop_serviceInstanceRef is not None:
            if hasattr(self._artop_serviceInstanceRef, "uuid"):
                return self._artop_serviceInstanceRef.uuid
        return
