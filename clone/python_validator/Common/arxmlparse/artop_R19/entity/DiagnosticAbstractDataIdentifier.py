# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticAbstractDataIdentifier.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_id = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_id": "POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def ref_id_(self):
        return self._artop_id

    @property
    def id_(self):
        if self._artop_id is not None:
            if hasattr(self._artop_id, "uuid"):
                return self._artop_id.uuid
        return
