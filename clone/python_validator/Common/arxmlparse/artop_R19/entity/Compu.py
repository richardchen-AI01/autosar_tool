# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Compu.py
from .ARObject import ARObject

class Compu(ARObject):

    def __init__(self):
        super().__init__()
        from .CompuContent import CompuContent
        from .CompuConst import CompuConst
        self._artop_compuContent = None
        self._artop_compuDefaultValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_compuContent':"COMPU-CONTENT", 
         '_artop_compuDefaultValue':"COMPU-CONST"})

    @property
    def ref_compuContent_(self):
        return self._artop_compuContent

    @property
    def compuContent_(self):
        if self._artop_compuContent is not None:
            if hasattr(self._artop_compuContent, "uuid"):
                return self._artop_compuContent.uuid
        return

    @property
    def ref_compuDefaultValue_(self):
        return self._artop_compuDefaultValue

    @property
    def compuDefaultValue_(self):
        if self._artop_compuDefaultValue is not None:
            if hasattr(self._artop_compuDefaultValue, "uuid"):
                return self._artop_compuDefaultValue.uuid
        return
