# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ForeignModelReference.py
from .ARObject import ARObject

class ForeignModelReference(ARObject):

    def __init__(self):
        super().__init__()
        from .BuildActionIoElement import BuildActionIoElement
        self._artop_base = None
        self._artop_dest = None
        self._artop_ref = None
        self._artop_buildActionIoElement = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_buildActionIoElement": "BUILD-ACTION-IO-ELEMENT"})

    @property
    def base_(self):
        return self._artop_base

    @property
    def dest_(self):
        return self._artop_dest

    @property
    def ref_(self):
        return self._artop_ref

    @property
    def ref_buildActionIoElement_(self):
        return self._artop_buildActionIoElement

    @property
    def buildActionIoElement_(self):
        if self._artop_buildActionIoElement is not None:
            if hasattr(self._artop_buildActionIoElement, "uuid"):
                return self._artop_buildActionIoElement.uuid
        return
