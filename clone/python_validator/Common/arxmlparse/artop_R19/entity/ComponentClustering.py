# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComponentClustering.py
from .MappingConstraint import MappingConstraint

class ComponentClustering(MappingConstraint):

    def __init__(self):
        super().__init__()
        from .ComponentInSystemInstanceRef import ComponentInSystemInstanceRef
        self._artop_mappingScope = None
        self._artop_clusteredComponentIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_clusteredComponentIref": "COMPONENT-IN-SYSTEM-INSTANCE-REF-IREF"})

    @property
    def mappingScope_(self):
        return self._artop_mappingScope

    @property
    def clusteredComponents_ComponentInSystemInstanceRef(self):
        return self._artop_clusteredComponentIref
