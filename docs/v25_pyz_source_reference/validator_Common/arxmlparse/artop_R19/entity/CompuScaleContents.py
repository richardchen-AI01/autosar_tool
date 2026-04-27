# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompuScaleContents.py
from .ARObject import ARObject

class CompuScaleContents(ARObject):

    def __init__(self):
        super().__init__()
        from .CompuScale import CompuScale
        self._artop_compuScale = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_compuScale": "COMPU-SCALE"})

    @property
    def ref_compuScale_(self):
        return self._artop_compuScale

    @property
    def compuScale_(self):
        if self._artop_compuScale is not None:
            if hasattr(self._artop_compuScale, "uuid"):
                return self._artop_compuScale.uuid
        return
