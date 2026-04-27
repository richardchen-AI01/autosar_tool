# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ResourceGroup.py
from .Identifiable import Identifiable

class ResourceGroup(Identifiable):

    def __init__(self):
        super().__init__()
        from .OsModuleInstantiation import OsModuleInstantiation
        self._artop_cpuUsage = None
        self._artop_memUsage = None
        self._artop_osModuleInstantiation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_osModuleInstantiation": "OS-MODULE-INSTANTIATION"})

    @property
    def cpuUsage_(self):
        return self._artop_cpuUsage

    @property
    def memUsage_(self):
        return self._artop_memUsage

    @property
    def ref_osModuleInstantiation_(self):
        return self._artop_osModuleInstantiation

    @property
    def osModuleInstantiation_(self):
        if self._artop_osModuleInstantiation is not None:
            if hasattr(self._artop_osModuleInstantiation, "uuid"):
                return self._artop_osModuleInstantiation.uuid
        return
