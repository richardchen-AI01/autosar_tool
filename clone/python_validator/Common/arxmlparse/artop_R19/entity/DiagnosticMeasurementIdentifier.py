# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticMeasurementIdentifier.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticMeasurementIdentifier(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_obdMid = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_obdMid": "POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def ref_obdMid_(self):
        return self._artop_obdMid

    @property
    def obdMid_(self):
        if self._artop_obdMid is not None:
            if hasattr(self._artop_obdMid, "uuid"):
                return self._artop_obdMid.uuid
        return
