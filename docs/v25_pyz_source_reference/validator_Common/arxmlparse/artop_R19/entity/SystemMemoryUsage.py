# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SystemMemoryUsage.py
from .Identifiable import Identifiable

class SystemMemoryUsage(Identifiable):

    def __init__(self):
        super().__init__()
        from .ResourceConsumption import ResourceConsumption
        self._artop_memoryConsumption = None
        self._artop_resourceConsumption = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_resourceConsumption": "RESOURCE-CONSUMPTION"})

    @property
    def memoryConsumption_(self):
        return self._artop_memoryConsumption

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return
