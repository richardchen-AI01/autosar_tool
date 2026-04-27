# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiscoveryTechnology.py
from .ARObject import ARObject

class DiscoveryTechnology(ARObject):

    def __init__(self):
        super().__init__()
        from .ApplicationEndpoint import ApplicationEndpoint
        self._artop_name = None
        self._artop_version = None
        self._artop_applicationEndpoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_applicationEndpoint": "APPLICATION-ENDPOINT"})

    @property
    def name_(self):
        return self._artop_name

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_applicationEndpoint_(self):
        return self._artop_applicationEndpoint

    @property
    def applicationEndpoint_(self):
        if self._artop_applicationEndpoint is not None:
            if hasattr(self._artop_applicationEndpoint, "uuid"):
                return self._artop_applicationEndpoint.uuid
        return
