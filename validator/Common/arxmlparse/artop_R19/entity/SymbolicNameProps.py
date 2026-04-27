# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SymbolicNameProps.py
from .ImplementationProps import ImplementationProps

class SymbolicNameProps(ImplementationProps):

    def __init__(self):
        super().__init__()
        from .ServiceDependency import ServiceDependency
        self._artop_serviceDependency = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_serviceDependency": "SERVICE-DEPENDENCY"})

    @property
    def ref_serviceDependency_(self):
        return self._artop_serviceDependency

    @property
    def serviceDependency_(self):
        if self._artop_serviceDependency is not None:
            if hasattr(self._artop_serviceDependency, "uuid"):
                return self._artop_serviceDependency.uuid
        return
