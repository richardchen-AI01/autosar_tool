# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswServiceDependencyIdent.py
from .IdentCaption import IdentCaption

class BswServiceDependencyIdent(IdentCaption):

    def __init__(self):
        super().__init__()
        from .BswServiceDependency import BswServiceDependency
        self._artop_bswServiceDependency = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_bswServiceDependency": "BSW-SERVICE-DEPENDENCY"})

    @property
    def ref_bswServiceDependency_(self):
        return self._artop_bswServiceDependency

    @property
    def bswServiceDependency_(self):
        if self._artop_bswServiceDependency is not None:
            if hasattr(self._artop_bswServiceDependency, "uuid"):
                return self._artop_bswServiceDependency.uuid
        return
