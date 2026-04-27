# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DoIpEntity.py
from .ARObject import ARObject

class DoIpEntity(ARObject):

    def __init__(self):
        super().__init__()
        from .InfrastructureServices import InfrastructureServices
        self._artop_doIpEntityRole = None
        self._artop_infrastructureServices = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_infrastructureServices": "INFRASTRUCTURE-SERVICES"})

    @property
    def doIpEntityRole_(self):
        return self._artop_doIpEntityRole

    @property
    def ref_infrastructureServices_(self):
        return self._artop_infrastructureServices

    @property
    def infrastructureServices_(self):
        if self._artop_infrastructureServices is not None:
            if hasattr(self._artop_infrastructureServices, "uuid"):
                return self._artop_infrastructureServices.uuid
        return
