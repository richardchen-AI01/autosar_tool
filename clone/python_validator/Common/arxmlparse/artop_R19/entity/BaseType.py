# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BaseType.py
from .ARElement import ARElement

class BaseType(ARElement):

    def __init__(self):
        super().__init__()
        from .BaseTypeDefinition import BaseTypeDefinition
        self._artop_baseTypeDefinition = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_baseTypeDefinition": "BASE-TYPE-DEFINITION"})

    @property
    def ref_baseTypeDefinition_(self):
        return self._artop_baseTypeDefinition

    @property
    def baseTypeDefinition_(self):
        if self._artop_baseTypeDefinition is not None:
            if hasattr(self._artop_baseTypeDefinition, "uuid"):
                return self._artop_baseTypeDefinition.uuid
        return
