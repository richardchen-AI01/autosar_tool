# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsServiceVersion.py
from .ARObject import ARObject

class DdsServiceVersion(ARObject):

    def __init__(self):
        super().__init__()
        from .DdsRequiredServiceInstance import DdsRequiredServiceInstance
        self._artop_majorVersion = None
        self._artop_minorVersion = None
        self._artop_ddsRequiredServiceInstance = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ddsRequiredServiceInstance": "DDS-REQUIRED-SERVICE-INSTANCE"})

    @property
    def majorVersion_(self):
        return self._artop_majorVersion

    @property
    def minorVersion_(self):
        return self._artop_minorVersion

    @property
    def ref_ddsRequiredServiceInstance_(self):
        return self._artop_ddsRequiredServiceInstance

    @property
    def ddsRequiredServiceInstance_(self):
        if self._artop_ddsRequiredServiceInstance is not None:
            if hasattr(self._artop_ddsRequiredServiceInstance, "uuid"):
                return self._artop_ddsRequiredServiceInstance.uuid
        return
